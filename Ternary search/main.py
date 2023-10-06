def getroll():
    roll_no=[]
    n=int(input("Enter total number of students :"))
    for i in range(0,n):
        roll_no.append(int(input("Enter Roll No of Student : ")))
    print("list of roll nos: ",roll_no)
    return roll_no

def sort(roll_no):
    for i in range(0,len(roll_no)):
        for j in range(i+1,len(roll_no)):
            if(roll_no[i]>roll_no[j]):
                temp=roll_no[i]
                roll_no[i]=roll_no[j]
                roll_no[j]=temp
    print("Sorted list of roll nos: ",roll_no)
    return roll_no

def Ternary_Search(roll,roll_find):
    left=0
    right=len(roll)-1
    while left <= right :
        mid1= left + (right-left)//3
        mid2= left + 2*(right-left)//3
        if roll_find==roll[left]:
            return left
        elif roll_find==roll[right]:
            return right
        elif roll_find < roll[left] or roll_find > roll[right]:
            return -1
        elif roll_find <= roll[mid1]:
            return mid1
        elif roll_find > mid1 and roll_find<=roll[mid2]:
            left = mid1 + 1
            right = mid2
        else:
            left=mid2+1
    return -1

unsorted=[]
sorted=[]
flag=1
while flag==1:
    print("\n************Menu************")
    print("1.Accept & display Roll Number ")
    print("2. Sort Roll Numbers from the list")
    print("3. Perform  Ternary Search")
    ch = int(input("Enter your choice (from 1 to 3) : "))
    if ch==1:
        unsorted=getroll()
    elif ch==2:
        print("Elements after performing Sorting : \n")
        sorted = sort(unsorted)
    elif ch == 3:
        find_roll = int(input("Enter the Roll Number to be searched : "))
        index = Ternary_Search(sorted, find_roll)
        if index != -1:
            print("The Roll Number", find_roll, "is found at position", index )
        else:
            print("Roll Number", find_roll, "not found!!")
    else:
        print("Invalid choice.\nProgram terminated")
        flag = 0