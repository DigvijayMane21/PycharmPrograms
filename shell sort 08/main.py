import array as arr

def getperc():
    a = arr.array('f', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(float(input("Enter the Second Year % of Student : ")))
    print("Array of percentage of students: ",a)
    return a

def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    print("Sorted array of percentage: ",a)
    return a

# Top 5 Score
def top_five(a):
    print("Top five score are : ")
    cnt = len(a)
    if cnt < 5:
        start, stop = cnt - 1, -1 # stop set to -1 as we want to print the 0th element
    else:
        start, stop = cnt - 1, cnt - 6
    for i in range(start, stop, -1):
        print(a[i],end=",")
# Driver program
unsort_A=arr.array('f',[])
sort_A=arr.array('f',[])
flag = 1
while flag == 1:
    print("\n 1. Accept & display array elements \n 2. Sort the Elements \n 3.Display top five scores.")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        unsort_A = getperc()
    elif choice == 2:
        print("Elements after sorting using Shell Sort :")
        sort_A = shell_sort(unsort_A)
    elif choice==3:
        top_five(sort_A)
    else:
        print("Wrong choice")
        exit(0)
        flag=0

