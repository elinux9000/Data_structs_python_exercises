import sys
import subprocess
import os


def usage():
	print("\nusage:\n python monitor.py PYTHON_FILE [OPTIONS]\n")
	raise SystemExit


def run_process(full_command):
	command = full_command.split()
	output = subprocess.check_output(command, stderr=subprocess.STDOUT)
	print(output.decode("utf-8"))


def get_python_files():
	all_files = []
	files = []
	for (dirpath, dirnames, filenames) in os.walk("."):
		all_files.extend(filenames)
		break  #Collect only the files in the current dir
	for f in all_files:
		if f[-3:] == ".py":
			files.append(f)
	return files


def inotify_wait():
	python_files = get_python_files()
	command = "inotifywait -e modify "
	for f in python_files:
		command = command + f + " "
	print(command)
	run_process(command)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	#run yapf on all python files in current directory
	while True:
		try:
			files = get_python_files()
			for f in files:
				command = "yapf --style ../style.yapf -i " + f
				run_process(command)
		except subprocess.CalledProcessError as e:
			print("Error")
			print(e.output.decode("utf-8"))
			if input("Error running yapf.  Proceed?(y)") != "y":
				continue
		command = "python "
		for arg in sys.argv[1:]:
			command += arg
		print(command)
		run_process(command)
		try:
			inotify_wait()
		except subprocess.CalledProcessError as e:
			print(e.output.decode("utf-8"))
