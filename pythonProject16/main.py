def cric_and_bad(listC,listB):
    both_cric_bad=[]
    for i in listC:
        if i in listB:
            both_cric_bad.append(i)
    print("List of students who play cricket: ",listC)
    print("List of students who play badminton: ",listB)
    print("List of students who play both cricket and badminton:\n",both_cric_bad)

def cric_or_bad(listC,listB):
    either_cric_bad=[]
    for i in listC:
        if i not in listB:
            either_cric_bad.append(i)
    for i in listB:
        if i not in listC:
            either_cric_bad.append(i)
    print("List of students who play cricket: ", listC)
    print("List of students who play badminton: ", listB)
    print("List of students who play either cricket or badminton:\n",either_cric_bad)

def neither_cric_bad(listC,listB,listF):
    only_football=[]
    for i in listF:
        if i not in listC and listB:
            only_football.append(i)
    print("List of students who play cricket: ", listC)
    print("List of students who play badminton: ", listB)
    print("List of students who play football: ",listF)
    print("List of students who neither play cricket nor badminton:\n",only_football)
    print("No of students who neither play cricket nor badminton:\n",len(only_football))


listC=[]
listB=[]
listF=[]
C=int(input("Enter no of students who play cricket: "))
for i in range(0,C):
    listC.append(input("Enter the name of student: "))
B=int(input("Enter no of students who play badminton: "))
for i in range(0,B):
    listB.append(input("Enter the name of student: "))
F=int(input("Enter no of students who play football: "))
for i in range(0,F):
    listF.append(input("Enter the name of student: "))

flag=1
while(flag==1):
    print("*********MENU**********")
    print("1.List of students who play both cricket and badminton.")
    print("2.List of students who play either cricket or badminton.")
    print("3.List of students who neither play cricket nor badminton.")
    ch=int(input("Enter our choice: "))
    if(ch==1):
        cric_and_bad(listC,listB)
    elif(ch==2):
        cric_or_bad(listC,listB)
    elif(ch==3):
        neither_cric_bad(listC, listB, listF)
    else:
        print("Invalid choice.\nProgram terminated")
        flag=0