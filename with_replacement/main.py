table = {}

for i in range(0, 10):
    table[i] = [0, -1]

print(table)


def hash_function(value):
    return value % 10


def Insert(key, value):
    if table[key][0] == 0:
        table[key][0] = value
    elif table[key][0] % 10 != key:
        while table[key][0] != 0:
            key = (key + 1) % 10
        table[key][0] = value
    else:
        while table[key][0] != 0:
            key = (key + 1) % 10
        table[key][0] = value

        old_loc = hash_function(value)
        while table[old_loc][1] != -1:
            old_loc = table[old_loc][1]
        table[old_loc][1] = key


def find(key):
    for i in range(0, 10):
        if table[i][0] == key:
            return i
    return 0


RUNNING = True

while RUNNING:
    print("\n\nWhat do you want to do: \n1.Insert Number\n2.Find Number\n3.Delete number\n4.Print Table")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter a number: "))
        loc = hash_function(number)
        Insert(loc, number)

    elif choice == 2:
        key = int(input("Enter the key to be found: "))
        x = find(key)
        if x != 0:
            print("Key found at loc: ", x)
        else:
            print("Key not present")

    elif choice == 3:
        pass
    elif choice == 4:
        for key, value in table.items():
            print(key, ": ", value)

    else:
        print("Invalid Input. Please try again.")

    ch = input("Do you want to continue? (Y/N): ")
    if ch.upper() != 'Y':
        RUNNING=False