def longest_word(sentence):
    longest = max(sentence.split(), key=len)
    print(sentence)
    print("The longest word in the sentence is : ", longest)
    print("Length of the longest word is: ",len(longest))

def freq_of_char(sentence):
    cnt=0
    l=[]
    l.extend(sentence)
    ch=input("Enter a character from the sentence to find its frequency: ")
    for i in l:
        if(i==ch):
            cnt=cnt+1
    print("Frequency of character ",ch," is: ",cnt)

def palindrome(sentence):
    l1=[]
    l1.extend(sentence)
    for i in range(0,len(l1)):
        if(sentence[i]==sentence[len(sentence)-i-1]):
            print("Sentence is a palindrome.")
            break
        else:
            print("Sentence is not a palindrome.")
            break

def first_apperance(sentence):
    substring=input("Entera substring fromthe sentence: ")
    index=sentence.find(substring)
    print("The substring is at index: ",index)

def word_count(sentence):
    print("Frequeny of each word.")
    l = sentence.split(" ")
    for i in l:
        cnt=0
        for j in l:
            if(i==j):
                cnt=cnt+1
        print("Frequency of ",i," is ",cnt)

sentence=input("Enter the sentence: ")
flag=1
while(flag==1):
    print("\n*******MENU********\n")
    print("1.Find the longest word.\n2.Frequency of a given character.\n3.To check if the sentence is palindrome.")
    print("4.Index of first apperance of given substring.\n5.No of occurance of a given word.\n")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        longest_word(sentence)
    elif(ch==2):
        freq_of_char(sentence)
    elif(ch==3):
        palindrome(sentence)
    elif(ch==4):
        first_apperance(sentence)
    elif(ch==5):
        word_count(sentence)
    else:
        print("Invalid choice.\nProgramm terminated.")
        flag=0