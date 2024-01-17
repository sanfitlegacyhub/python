import os
folder=input("enter the fodler name - : ")

with os.scandir(folder) as fodlers:
    for flrd in fodlers:
        if flrd.is_file():
            print(flrd.name)