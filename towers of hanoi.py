towers=[[], [], []]
discs=[["1"], ["2"], ["3"]]
discinpt=input("choose a disc")
towerinpt=input("choose a tower")
if discinpt=="1" or discinpt=="disc 1":
    if towerinpt=="1" or towerinpt=="tower 1":
        towers[0].append(discs[0])
print(towers)