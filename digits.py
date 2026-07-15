x=int(input("input a number "))
def num(x):
    digits=1
    while x>=10:
        x/=10
        digits+=1
    return(digits)
print(num(x))
