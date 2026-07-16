list=[]
from random import randint
for x in range(10):
    list.append(randint(0,100))
print(list)
for y in range(10):
    for z in range(10-1):
        if list[z]>list[z+1]:
            temp=list[z]
            list[z]=list[z+1]
            list[z+1]=temp
print(list)