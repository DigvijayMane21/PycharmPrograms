Set_A=set()
Set_B=set()
def add_element():
    n=int(input("Enter total no of elements you want to add in Set A: "))
    for i in range(n):
        ele=int(input("enter the element: "))
        if ele not in Set_A:
            Set_A.add(ele)
    print("Set_A= ",Set_A)

    m=int(input("Enter total no of elements you want to add in Set B: "))
    for i in range(m):
        ele1=int(input("enter the element: "))
        if ele1 not in Set_B:
            Set_B.add(ele1)
    print("Set_B= ",Set_B)

def remove_element():
    ch=input("Enter the set from which you want to remove an element (A/B): ")
    if ch=='A':
        rem=int(input("Enter the element you want to remove: "))
        if rem in Set_A:
            Set_A.remove(rem)
            print("Set A= ",Set_A)
        else:
            print("\nElement not present in Set A.")

    elif ch=='B':
        rem1=int(input("Enter the element you want to remove: "))
        if rem1 in Set_B:
            Set_B.remove(rem1)
            print("Set B= ",Set_B)
        else:
            print("\nElement not present in Set B.")

    else:
        print("\nInvalid choice!!")

def contains_element():
    ch = input("Enter the set from which you want to search an element (A/B): ")
    if ch=='A':
        ele=input("Enter the element to search: ")
        if ele in Set_A:
            print(ele," is present in Set A.")
        else:
            print(ele," is not present in Set A.")

    elif ch=='B':
        ele1=input("Enter the element to search: ")
        if ele1 in Set_B:
            print(ele1," is present in Set B.")
        else:
            print(ele1," is not present in Set B.")

    else:
        print("Invalid choice!!!")

def size():
    lenA=len(Set_A)
    lenB=len(Set_B)
    print("\nSize of Set A is : ",lenA)
    print("Size of Set A is : ", lenA,"\n")

def set_iter():
    iter1=iter(Set_A)
    iter2=iter(Set_B)
    print("\nIterating over Set A...")
    for i in iter1:
        print(i,end=" ")
    print("\nIterating over Set B...")
    for i in iter2:
        print(i, end=" ")
    print("\n")

def intersection():
    set3=set()
    for i in Set_A:
        if i in Set_B:
            set3.add(i)
    print("Set A= ",Set_A)
    print("Set B= ",Set_B)
    print("Intersection = ",set3)

def union():
    set4=Set_A.copy()
    for i in Set_B:
        if i not in set4:
            set4.add(i)
    print("Set A= ", Set_A)
    print("Set B= ", Set_B)
    print("Union = ", set4)

def difference():
    ch=input("Engter A for (A-B) & B for (B-A): ")
    if ch=='A':
        set5=set()
        for i in Set_A:
            if i not in Set_B:
                set5.add(i)
        print("Set A= ", Set_A)
        print("Set B= ", Set_B)
        print("(A-B) = ", set5)

    elif ch=='B':
        set6 = set()
        for i in Set_B:
            if i not in Set_A:
                set6.add(i)
        print("Set A = ", Set_A)
        print("Set B = ", Set_B)
        print("Difference (B-A) : ", set6)


def subset():
    if Set_A.issubset(Set_B):
        print("Set A is subset of Set B.")
    elif Set_B.issubset(Set_A):
        print("Set B is subset of Set A.")
    else:
        print("Niether Set A nor St B are subsets of each other.")

flag=1
while (flag==1):
    print("\n********MAIN MENU*******")
    print("1.Insert an element in a set.")
    print("2.Remove an element from a set.")
    print("3.Search for an element from a set.")
    print("4.Intersection of the two sets.")
    print("5.Union of two sets.")
    print("6.Difference between the sets.")
    print("7.Check for subset.")
    print("8.Size of the sets.")
    print("9.Iter over sets.")
    print("10.Exit.")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        add_element()
    elif(ch==2):
        remove_element()
    elif(ch==3):
        contains_element()
    elif(ch==4):
        intersection()
    elif(ch==5):
        union()
    elif(ch==6):
        difference()
    elif(ch==7):
        subset()
    elif(ch==8):
        size()
    elif(ch==9):
        set_iter()
    elif(ch==10):
        print("Exiting...")
        flag=0
    else:
        print("\nInvalid choice...")