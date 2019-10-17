import sys
import subprocess
import os



def usage():
	print("usage: python monitor.py PYTHON_FILE [OPTIONS]")


if __name__=="__main__":
	if len(sys.argv)<2:
		usage()
	else:
		try:
			f=[]
			for (dirpath, dirnames, filenames) in os.walk("."):
				f.extend(filenames)
				break #Collect only the files in the current dir
			print(f)

			output = subprocess.check_output(["yapf","--style.yapf style.yapf -i *.py"],stderr=subprocess.STDOUT)
			print(output.decode("utf-8"))
		except subprocess.CalledProcessError as e:
			print("Error")
			print(e.output.decode("utf-8"))


