import os

path = "C:\Users\lamhuynh\Desktop\README.md"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile(path):
        print("that is a file!")
    elif os.path.isdir(path):
        print("that is a directory!") #for folder

else:
    print("That location does not exist")