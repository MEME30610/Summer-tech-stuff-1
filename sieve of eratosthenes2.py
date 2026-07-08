#ask the user how many primes they want, make a list that will hold the primes
#have a loop that generates primes until it find enough primes
#print the list
prmnum=[]
candidate=2
print("How many prime numbers do you want?")
number=int(input())
while len(prmnum)<number:
    prime=True
    for x in range(2,candidate):
        if candidate%x==0:
            prime=False
            break
    if prime:
        prmnum.append(candidate)
    candidate+=1
print(prmnum)