size=int(input())
for x in range(size):
    for y in range(size):
        print("*", end=" ")
    print()
print()
for x in range(size):
    for y in range(x+1):
        print("*", end=" ")
    print()
print()
for x in range(size, 0, -1):
    for y in range(x):
        print("*", end=" ")
    print()
print()
for x in range(size, -1, -1):
    for y in range(x):
        print(" ", end=" ")
    for z in range(x, size):
        print("*", end=" ")
    print()
print()
for x in range(size):
    for y in range(size):
        if x==0 or x==size-1 or y==0 or y==size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()