f=input("enter the file name: " )
open(f,"r")
words=0
chars=0
lines=0
for line in f:
    lines+=1
    line=line.strip("\n")
    chars+=len(line)
    list1=line.split()
    words+=len(list1)


print("total lines:", lines)
print("total chars:", chars)
print("total words:", words)