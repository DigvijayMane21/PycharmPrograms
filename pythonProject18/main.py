def linear_search(arr,key):
    for i in range(len(arr)):
        if (arr[i]==key):
            return i
    return -1

def binary_search(arr,key,l,r):
    while (l<=r):
        mid=(l+r)//2

        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            return binary_search(arr,key,l,mid-1)
        elif(arr[mid]>key):
            return binary_search(arr,key,mid+1,r)
        else:
            return -1
l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print(l)
key=int(input("Enter the element you want to search: "))

print("******MAIN MENU*****")
print("1.Linear Search\n2.Binary Search")
ch=int(input("Enter your choice: "))
if(ch==1):
    res=linear_search(l,key)
    if (res!=-1):
        print("Element is present at index ",res)
    else:
        print("Element is not present.")

elif(ch==2):
    res=binary_search(l,key,0,len(l))
    if (res!=-1):
        print("Element is present at index ",str(res))
    else:
        print("Element is not present.")