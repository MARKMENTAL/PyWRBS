import os
print("Launched by pylaunch")
os.system("python3 pywrbs.py")
choice = input("Would you like to go again?(Y/N)")
if choice.lower() == "y":
	os.system("python3 pywrbs.py")
else:
	print("Exiting...")
