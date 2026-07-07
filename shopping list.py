#implement functionality to add or remove items from the list
#print the list using a forloop
#run forever until the user wants to stop
#use append or remove (to add use variable then a dot
shop=[]
while True:
    print("Do you want to add to the list, remove from the list, or exit?")
    answer=input()
    if answer.lower()=="add" or answer.lower()=="a":
        print("What do you want to add to the list?")
        add=input()
        shop.append(add)
        print(shop)
    elif answer.lower()=="remove" or answer.lower()=="r":
        print("What do you want to remove?")
        remove=input()
        if remove in shop:
            shop.remove(remove)
            print(shop)
        else:
            print("input invalid")
    elif answer.lower()=="exit" or answer.lower()=="e":
        print("your shopping list is", end=" ")
        print(shop)
        break
