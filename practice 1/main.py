table1=[None]*10
print("Hash table 1= ",table1)

def replacement_hash_insert(l):
    for item in l:
        table1[item[0]%10]=item

def replacement_search(key):
    k=key%10
    if table1[k]!=None and table1[k][0]==key:
        print("Key found:\nName = ",table1[k][1],"Roll No = ",table1[k][0])
        return True
    else:
        print("Key not found.")
        return False

def replacement_hash_delete(key):
    k=key%10
    if replacement_search(key):
        table1[k]=None
        print(key," Deleted!!!!")
    else:
        print(key," Not found to be deleted.")

if __name__=="__main__":
    print("Insertion with replacement=\n")
    n=int(input("Enter the number of entries you want to insert: "))
    for i in range(n):
        roll=int(input("\nEnter the roll: "))
        name=input("Enter the name: ")
        replacement_hash_insert([[roll,name]])
    print("Hash table 1 after insertions:\n",table1)

    m=int(input("\nEnter the number of colliding entries you want to insert: "))
    for i in range(m):
        roll1=int(input("\nEnter the roll: "))
        name1=input("Enter the name: ")
        replacement_hash_insert([[roll1,name1]])
    print("After insertion of few more data values=\n",table1)

    print("Applying search operation..\n")
    srch=int(input("Enter a roll to search for the value: "))
    replacement_search(srch)

    print("Applying deletion operation..\n")
    Del=int(input("Enter a roll to delete a value: "))
    replacement_hash_delete(Del)
    print("Hash table after deletion =\n",table1)