x=input("Celsius to Farenheit or Farenheit to Celsius ")
y=int(input("input your temperature "))
def temp(x, y):
    if x=="c" or x=="C" or x=="Celsius" or x=="celsius":
        return(y*1.8+32)
    elif x=="f" or x=="F" or x=="farenheit" or x=="Farenheit":
        return((y-32)*0.5556)
print(temp(x,y))