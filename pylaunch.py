import os 
status = 0
print("Launched by pylaunch")
try:
    status = int(input("1.Python Version\n2.Python3 Version(Suggested for Ubuntu)\n"))
except ValueError:
    print("An error occurred, invalid input.\nlauncher shutting down...")
while status != 0:
    if status == 1:
        os.system("python pywrbs.py")
        try:
            status = int(input("Press 0 to exit or 1 to keep playing:\n"))
            if status == 1:
                status = 1
            else:
                print("launcher shutting down...")
        except ValueError:
            print("An error occurred, invalid input...\nlauncher shutting down...")
            status = 0
        except KeyboardInterrupt:
            print("launcher shutting down...")
            status = 0

    elif status == 2:
        os.system("python3 pywrbs.py")
        try:
            status = int(input("Press 0 to exit or 1 to keep playing:\n"))
            if status == 1:
                status = 2
            else:
                print("launcher shutting down...")
        except ValueError:
            print("An error occurred, invalid input...\nlauncher shutting down...")
            status = 0
        except KeyboardInterrupt:
            print("\nlauncher shutting down...")
            status = 0

    else:
         status = 0
         print("launcher shutting down...")
