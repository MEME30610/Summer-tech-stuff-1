#take a word or a phrase as an input
#check if the word is a palinrome
#say if it is a palindrome or not
while True:
    print("input a word or phrase")
    word=input()
    word=word.replace(" ", "")
    word=word.replace(".", "")
    word=word.replace(",", "")
    wtv=[]
    vtw=[]
    for x in range(len(word)):
        wtv.append(word[x])
    for y in range(len(word), 0, -1):
        vtw.append(word[y-1])
    if wtv==vtw:
        print("the word is a palindrome")
    else:
        print("not a palindrome")
    
    print('do you want to exit?')
    exit=input()
    if exit=="yes":
        break