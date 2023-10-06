set1=set()
set2=set()
def add_element():
    n=int(input("Enter Total Number of Elements to add in Set A : "))
    for i in range (n):
        element=int(input("Enter element : "))
        if element not in set1 :
            set1.add(element)
    print("Set A = ",set1)
    m=int(input("Enter Total Number of Elements to add in Set B : "))
    for i in range (m):
        value=int(input("Enter Element : "))
        if value not in set2 :
            set2.add(value)
    print("Set B = ",set2)

def remove_element():
    choice=(input("From which set you want to remove (A|B)  : "))
    if choice =='A':
        rem_ele=int(input("Enter Element to remove from Set A : "))
        if rem_ele in set1 :
            set1.remove(rem_ele)
            print("Set A = ",set1)
            print("\n")
        else :
            print(rem_ele," not found !!\n\n")
    elif choice == 'B':
        rem= int(input("Enter Element to remove from Set B : "))
        if rem in set2:
            set2.remove(rem)
            print("Set B = ", set2)
            print("\n")
        else:
            print(rem, " not found !!\n")
    else :
        print("Invalid Choice !!!\n")

def contain_element():
    con=input("Search Element in SET(A|B) : ")
    if con=='A':
        s1=int(input("Enter Element to Search in Set A : "))
        if s1 in set1 :
            print(s1," is present in Set A \n")
        else :
            print(s1," is absent in Set A \n")
    elif con=='B':
        s2 = int(input("Enter Element to Search in Set B : "))
        if s2 in set1:
            print(s2, " is present in Set B \n")
        else:
            print(s2, " is absent in Set B \n")
    else:
        print("Invalid Choice !!!\n")

def size() :
    length_A=len(set1)
    length_B=len(set2)
    print("\n")
    print("Size of Set A : ", length_A)
    print("Size of Set B : ",length_B)
    print("\n")

def set_iter() :
    iter_A = iter(set1)
    iter_B = iter(set2)
    print("\n")
    print("Iterating over Set A:")
    for element in iter_A:
        print(element, end=" ")
    print("\n")
    print("Iterating over Set B:")
    for element in iter_B:
        print(element, end=" ")
    print("\n")

def intersection():
    set3=set()
    for i in set1 :
        if i in set2 :
            set3.add(i)
    print("Set A = ", set1)
    print("Set B = ", set2)
    print("\n")
    print("Intersection of Set A and Set B : ",set3)
    print("\n")

def union():
    set4=set1.copy()
    for i in set2 :
        if i not in set4 :
            set4.add(i)
    print("Set A = ", set1)
    print("Set B = ", set2)
    print("\n")
    print("Union of Set A and Set  B : ",set4)

def difference():
    ch1=int(input("Enter 1 for (A-B) , 2 for (B-A) : "))
    if ch1==1:
        set5=set()
        for i in set1 :
            if i not in set2 :
                set5.add(i)
        print("Set A = ", set1)
        print("Set B = ", set2)
        print("\n")
        print("Difference (A-B) : ",set5)
        print("\n")
    else :
        set6 = set()
        for i in set2:
            if i not in set1:
                set6.add(i)
        print("Set A = ",set1)
        print("Set B = ",set2)
        print("\n")
        print("Difference (B-A) : ", set6)
        print("\n")

def subset():
    if set1.issubset(set2):
        print("Set A is a subset of Set B")
    elif set2.issubset(set1):
        print("Set B is a subset of Set A")
    else:
        print("Neither Set A nor Set B is a subset of the other")

flag=1
while(flag==1):
    print("******MENU*******")
    print("1.Add Element in Set .")
    print("2.Remove Element from Set .")
    print("3.Search Element in Set .")
    print("4.Size of Sets .")
    print("5.Intersection of Sets .")
    print("6.Union of Sets .")
    print("7.Difference of Set . ")
    print("8.Check For Subset .")
    print("9. Iterate over Sets .")
    print("10.Exit")
    ch=int(input("Enter Your Choice : "))
    if(ch==1):
        add_element()

    elif(ch==2):
        remove_element()

    elif(ch==3):
        contain_element()

    elif(ch==4):
        size()

    elif(ch==5):
        intersection()

    elif(ch==6):
        union()

    elif(ch==7):
        difference()

    elif(ch==8):
        subset()

    elif(ch==9):
        set_iter()

    elif(ch==10):
        print("Thank You !!!\n")
        flag=0
    else :
        print("Invalid Choice !!\n")

