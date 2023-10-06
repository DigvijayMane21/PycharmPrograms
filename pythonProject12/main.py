string = input("Enter a string:")
list = []


def longword():
    a = (string.split(" "))
    print(a)
    b = sorted(a, key=len)
    print("Longest word present in the string is: ", b[-1])


longword()


def occurance():
    str = input("Enter a character which is how many times occured in string:")
    print(string.count(str))


occurance()


def palindrome():
    print("\nGiven string is palindrome or not:")
    if string == string[::-1]:
        print("Given string is Palindrome.")
    else:
        print("Given string is not Palindrome.")


palindrome()


def indsub():
    substring = input("Enter a substring:")
    print("index of substring is :", string.index(substring))


indsub()


def wordcount():
    wordc = 0
    a = (string.split(" "))
    word = input("enter word which you want to count:")
    for i in range(0, len(a)):
        if (word == a[i]):
            wordc += 1
    print("count of given word is", wordc)


wordcount()
