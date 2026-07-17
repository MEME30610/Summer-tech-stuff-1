list=[]
from random import randint
for x in range(10):
    list.append(randint(0,100))
def selectsort(list):
    smallest=0
    for y in range(10):
        for z in range(y,10):
            if list[z]<list[smallest]:
                smallest=z
        temp=list[y]
        list[y]=list[smallest]
        list[smallest]=temp
        smallest=y+1
print(list)
selectsort(list)
print(list)