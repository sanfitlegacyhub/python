import os

folders=input("enter the directories: ").split()

for folder in folders:
#we have to use the listdir() module foe list files in python unlike ls in linux
    try:
        files=os.scandir(folder)
    except FileNotFoundError:
        print("please enter the valid directory name, looks like the foler is not exist - " +folder)
        break
    except PermissonError:
        break
        print("no access to this folder")
    print("listing the files for the folder -" + folder)
   # print(files)
    for file in files:
        print(file)
#to avoid the exceptions for invalid direcoires given by uses , we uses the Exceptionhandling usecase try except :
