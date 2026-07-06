print("type a number")
number1=float(input())
print("type another number")
number2=float(input())
print("input an operation")
operation=input()
if operation=="+":
    print(number1+number2)
elif operation=="-":
    print(number1-number2)
elif operation=="*":
    print(number1*number2)
elif operation=="/":
    print(number1/number2)
elif operation=="%":
    print(number1%number2)
else:
    print("input invalid")