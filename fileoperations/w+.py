f1=open("file2.txt","w+")

f1.write("hi")
print(f1.tell())
f1.write("this is python tutor")
print(f1.tell())
f1.seek(0)
data=f1.read()
print(data)