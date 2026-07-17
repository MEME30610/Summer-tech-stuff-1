list=[]
from random import randint
for x in range(10):
    list.append(randint(0,100))
def insertsort(list):
    for y in range(1,10):
        z=y
        while z>0 and list[z]<list[z-1]:
            temp=list[z]
            list[z]=list[z-1]
            list[z-1]=temp
            z=z-1
print(list)
insertsort(list)
print(list)