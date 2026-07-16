def towers(disk, start, mid, end):
    if disk>0:
        towers(disk-1, start, mid, end)
        print("move disk", disk, "from peg")
        towers(disk-1, mid, start, end)
towers(3, 1, 2, 3)