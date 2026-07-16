def binarysearch(list, start, end, target):
    mid=(end-start)/2+start
    if list[int(mid)]==target:
        return(int(mid))
    elif list[int(mid)]>target:
        return(binarysearch(list, start, mid-1, target))
    elif list[int(mid)]<target:
        return(binarysearch(list, mid+1, end, target))
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binarysearch(list, 0, 9, 7)