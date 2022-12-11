f=open("car.txt",'a')
car={}
n=int(input())
for i in range(n):
    brand=input("enter brand name:")
    colour=input("enter colour:")
    car[brand]=colour
print("cars:",car)
f.write(str(car))
f.close()   
    