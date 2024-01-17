f1=open("file1.txt","r+")
print(f1.tell())
f1.write("hi")
print(f1.tell())
print(f1.read())
print(f1.tell())


""""
i/p

hiis is write methond operation

o/p =PS C:\Devops\python-for-devops\fileoperations> python .\rw.py      
is is write methond operation

to find the position of pointer u can use tell() method 

o/p = of tell() method 0
2
is is write methond operation
31

"""