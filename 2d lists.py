
wtv=[["a","b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]]
for x in range(len(wtv)):
    for y in range(len(wtv[x])):
        print(wtv[x][y], end=" ")
    print()