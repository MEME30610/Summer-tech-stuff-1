def countdown(x):
    if x>=0:
        print(x)
        countdown(x-1)
countdown(10)
print()
def count(y):
    if y<=10:
        print(y)
        count(y+1)
count(0)
print()
def factorial(z):
    if z==0:
        return(1)
    return(factorial(z-1)*z)
print(factorial(10))