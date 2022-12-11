f=open("n.txt",'a')

n1=int(input("enter value1:"))
n2=int(input("enter value2:"))
n3=int(input("enter value3:"))
n4=int(input("enter value4:"))
n5=int(input("enter value5:"))


if (n1>0 and n2>0 and n3>0 and n4>0 or n5>0 ):
    total=n1+n2+n3+n4+n5
    print(total)
    f.write(str(total))

else:
    print("enter +ve value")

f.close()