#take the input of a number that you want to check is prime
#divide the number by every interger smaller than the number, and check if any of the numbers produce a remainder that is not equal to zero
#tell the user whether or not it is prime
prime=True
print("input a number to check if it's prime")
number=int(input())
for x in range(2, number):
    (number%x)
    if number%x==0:
        prime=False
        break
if prime==False:
    print("Not a prime number")
else:
    print("It is a prime number")