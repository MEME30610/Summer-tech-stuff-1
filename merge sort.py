list=[]
from random import randint
for x in range(10):
    list.append(randint(0,100))
def mrgsort(list, left, right):
    sorted=[]
    mid=(left+right)/2
    i=left
    j=mid+1
    while i<mid+1 and j<right+1:
        if list[i]<=list[int(j)]:
            sorted.append(list[i])
            i+=1
        else:
            sorted.append(list[int(j)])
            j+=1
    while j<right+1:
        sorted.append(list[int(j)])
        j+=1
    while i<mid+1:
        sorted.append(list[i])
        i+=1
    for y in range(len(sorted)):
        list[left+y]=sorted[y]

def split(list, left, right):
    mid=(left+right)/2
    if right-left==0:
        return()
    else:
        split(list, left, right)
        split(list, mid-1, right)
        mrgsort(list, left, right)
print(list)
mrgsort(list, 0, 10-1)
print(list)