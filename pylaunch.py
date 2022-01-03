import os
status = 1
print("Launched by pylaunch")
status = int(input("1.Python Version\n2.Python3 Version\n"))
while status != 0:
	if status == 1:
		os.system("python pywrbs.py")
		status = int(input("Press 0 to exit or 1 to keep playing:"))
		if status != 1:
			status = 0
	elif status == 2:
		os.system("python3 pywrbs.py")
		status = int(input("Press 0 to exit or 1 to keep playing:"))
		if status != 1:
			 status = 0
		elif status == 1:
			status = 2
	else:
		status = 0
		print("Exiting...")
