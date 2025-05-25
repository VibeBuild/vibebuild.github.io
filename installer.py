#!/usr/bin/env python3

from time import sleep
from subprocess import run
from os.path import exists


colors = [
    "\033[38;2;100;200;255m",  # Azul claro
    "\033[38;2;140;160;255m",  # Azul arroxeado
    "\033[38;2;180;120;255m",  # Roxo claro
    "\033[38;2;220;80;255m",   # Magenta
    "\033[38;2;255;120;180m",  # Rosa
    "\033[38;2;255;180;180m",  # Rosa claro
    "\033[38;2;255;255;255m"   # Branco
]
reset = "\033[0m"

lines = [
	"┌─────────────────────────────────────────────────┐",
	"│      O       Idealized By:       Programmed By  │",
	"│     _|_   Renato Lóis M. Silva     ChatGPT4o    │",
	"│    /   \\                                        │",
	"│    () ()                                        │",
	"│   ,|_ _|,                                       │",
	"│ _/_______\\_ ....          VibeBuild             │",
	"│ \\  < / >  / |--|)                               │",
	"│  \\_______/  |__|  One script to build them all  │",
	"│                                                 │",
	"│       https://github.com/rlois4/vibebuild/      │",
	"└─────────────────────────────────────────────────┘"
]

def install():
	r = run("sudo -v", shell=True)
	if r.returncode != 0:
		print("error: root access permission denied")
		exit(1)
	r = run("chmod +x ./VibeBuild", shell=True)
	if r.returncode != 0:
		print("error: couldn't do: 'chmod +x ./VibeBuild'")
		exit(1)
	r = run("sudo cp ./VibeBuild /usr/bin/vibe", shell=True)
	if r.returncode != 0:
		print("error: couldn't copy file to /usr/bin")
		exit(1)




	for i, line in enumerate(lines):
		color = colors[i * len(colors) // len(lines)]
		print(f"{color}{line}{reset}")


	print("VibeBuilder was installed succefully\n"
	      "use 'vibe' to run")



if exists("/usr/bin/vibe"):
	print("vibe is already installed.\n"
			  "use 'vibe' to run!")
	
	while True:
		ch = input("\nDo you want to reinstall? [y/n]: ").strip().lower()
		if ch == 'y':
			install()
			break
		elif ch == 'n':
			print("Canceled.")
			break
		else:
			print("Please enter 'y' to reinstall or 'n' to cancel.")

else:
	install()
	
