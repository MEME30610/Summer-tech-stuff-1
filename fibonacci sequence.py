#make a list and add 0 and 1 to it in the begining
#ask the user how many terms of the fibonacci sequence they want
#use previous terms to generate new ones until we have enough
#print or use forloop
sequence=[0, 1]
print("How many terms of the fibonacci sequance do you want?")
answer=input()
if answer=="1":
    print([0])
elif answer=="0":
    print([])
else:
    for x in range(2, int(answer)):
        sequence.append(sequence[x-1]+sequence[x-2])
    print(sequence)