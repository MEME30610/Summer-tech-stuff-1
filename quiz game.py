score=0
print("what is my name?")
name=input()
if name=="Alain" or name=="alain":
    print("correct")
    score=score+1
else:
    print("incorrect")
print()

print("where is summer tech located?")
location=input()
if location=="NY" or location=="New York" or location=="Purchase College":
    print("correct")
    score+=1
else:
    print("incorrect")
print()

print("what is my favorite color?")
print("a. Blue")
print("b. Red")
print("c. Yellow")
print("d. Green")
color=input()
if color=="Blue" or color=="blue" or color=="a" or color=="A":
    print("correct")
    score+=1
else:
    print("incorrect")
print()

print("what am I writing with?")
thing=input()
if thing=="keyboard" or thing=="Keyboard":
    print("correct")
    score+=1
else:
    print("incorrect")
print()

print("what is another name for precipitation?")
precipitation=input()
if precipitation in ["rain", "Rain", "Snow", "snow", "hail", "Hail"]:
    print("correct")
    score+=1
else:
    print("incorrect")
print()

print("Your score is "+str(score))