cabinet=[["clothes", " ", "cable"],
        ["games", "usb ", " "],
        [" ", " ", "controler"]]
print(cabinet)
cabinet[2][0]="mouse"
print(cabinet)
print()
for x in range(len(cabinet)):
    for y in range(len(cabinet[x])):
        print(cabinet[x][y], end=" ")
    print()