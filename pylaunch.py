import os
status = 1
print("Launched by pylaunch")
os.system("python3 pywrbs.py")
choice = input("Would you like to go again?(Y/N)")
while status == 1:
	if os.name == "nt" and choice.lower() == "y" and status ==1:
		os.system("python pywrbs.py")
		status = int(input("Press 0 to exit or 1 to keep playing:"))
		if status != 1:
			status = 0
	elif choice.lower() == "y" and status == 1:
		os.system("python3 pywrbs.py")
		status = int(input("Press 0 to exit or 1 to keep playing:"))
		if status != 1:
			 status = 0
	else:
		status = 0
		print("Exiting...")
