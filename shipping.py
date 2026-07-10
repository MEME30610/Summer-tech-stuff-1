items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
storage=[]
vert=0
horz=0
vert2=0
horz2=0
for x in range(6):
    storage.append([])
    for y in range(4):
        storage[x].append("")
print(storage)
print()
for z in items:
    storage[vert][horz]=z
    horz+=1
    if horz==4:
        horz=0
        vert+=1
print(storage)
print()
for i in range(0, 3):
    for j in range(0, 4):
        storage[5-i][j]=storage[i][j]
print(storage)