def insert(set1, num):
    for i in range(num):
        ele = int(input("Enter Number : "))
        if ele not in set1:
            set1.add(ele)
    print("Set A : ", set1)

def prob(set1):
    p = 0
    for i in set1:
        if i % 3 == 0 and i % 5 == 0: p = p + 1
    print("Set A : ", set1)
    print("Probability of number divisible by 3 and 5 are:", p / len(set1))

def prime(set1):
    prob_p = 0
    for i in set1:
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt = cnt + 1
        if cnt == 2:
            prob_p = prob_p + 1
    print("Set A : ", set1)
    print("Probability of prime numbers in the set is:", prob_p / len(set1))

def even(set1):
    even_cnt = 0
    for i in set1:
        if i % 2 == 0:
            even_cnt = even_cnt + 1
    print("Set A : ", set1)
    print("Probability of Even Number in the set is : ", even_cnt / len(set1))

set1 = set()
flag = 0
while flag == 0:
    print("\n******MENU******")
    print("1. Insert Element in set")
    print("2. Find Probability of numbers divisible by 3 and 5")
    print("3. Find Probability of prime numbers")
    print("4. Find Probability of even numbers")
    print("5. Exit")
    ch = int(input("Enter choice : "))
    if ch == 1:
        num = int(input("Enter Total number of Elements : "))
        insert(set1, num)
    elif ch == 2:
        prob(set1)
    elif ch == 3:
        prime(set1)
    elif ch == 4:
        even(set1)
    elif ch == 5:
        print("Thank You !!\n")
        flag = 1
    else:
        print("Invalid choice! Please try again.\n")
