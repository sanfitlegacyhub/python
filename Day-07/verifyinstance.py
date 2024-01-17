import sys

type= sys.argv[1]

if type == "t2.micro":
    print("cost 2 dollers")
elif type == "t2.medium":
    print("cost 4 dollers")
elif type == "t2.xlarge":
    print("costs 8 dollers")
else:
    print("the given instance is not t2.micro , cant create instance")