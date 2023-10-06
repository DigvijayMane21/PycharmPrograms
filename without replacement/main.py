table=[[]for i in range(10)]

def insert(l):
    for item in l:
        table[item[0]%10].append(item)

def search(key):
    k=key%10
    for item in table[k]:
        if item[0]==key:
            print("Item Found..\nName= ",item[1],"\nRoll= ",item[0])
            return item
    print("\nItem not found.")
    return False

def delet(key):
    k = key % 10
    i=0
    for item in table[k]:
        if item[0]==key:
            del table[k][i]
        i+=1

if __name__ == "__main__":
    n=int(inp)