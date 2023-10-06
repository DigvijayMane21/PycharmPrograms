table1= [[] for i in range(10)]
print("Hash table is = \n",table1)

# without_replacement_hash
def without_replacement_hash_insert(l):
    for item in l:
        table1[item[0] % 10].append(item)

def without_replacement_hash_search(key):
    k = key % 10
    for item in table1[k]:
        if item[0] == key:
            print("Key found:\nName= ",item[1],"\nRoll= ",item[0])
            return item
    print("Key not found!!!!!!")
    return False

def without_replacement_hash_del(key):
    k = key % 10
    i = 0
    for item in table1[k]:
        if item[0] == key:
            del table1[k][i]
        i += 1

if __name__ == "__main__":
    print("Insertion without replacement=\n")
    n=int(input("Enter the number of entries you want to insert: "))
    for i in range(n):
        roll=int(input("\nEnter the roll: "))
        name=input("Enter the name: ")
        without_replacement_hash_insert([[roll,name]])
    print("Hash table after insertions:\n",table1)

    co = int(input("\nEnter the number of colliding entries you want to insert: "))
    for i in range(co):
        roll1 = int(input("\nEnter the roll: "))
        name1 = input("Enter the name: ")
        without_replacement_hash_insert([[roll1, name1]])
    print("After insertion of few more data values=\n", table1)

    print("\nApplying search operation..")
    m=int(input("\nEnter the number of times you want to search: "))
    for i in range(m):
        sr=int(input("Enter the key you want to search : "))
        without_replacement_hash_search(sr)

    print("\nApplying deletion operation..\n")
    Del=int(input("Enter a roll to delete a value: "))
    without_replacement_hash_del(Del)
    print("Hash table after deletion =\n",table1)