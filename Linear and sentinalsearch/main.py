import array as arr
def getrno():
  a=arr.array('I',[])
  nstud=int(input("Enter total number of student = "))
  for i in range(0,nstud):
    a.append(int(input("enter the roll no=")))
  print("Array of students: ",a)
  return a

def linear_search(a,x):
  for i in range(len(a)):
    if(a[i]==x):
      return i
  return -1

def sentinel_search(arr,n,key):
  # Last element of the array
  last = arr[n - 1]

  # Element to be searched is
  # placed at the last index
  arr[n - 1] = key
  i = 0

  while (arr[i] != key):
    i += 1

  # Put the last element back
  arr[n - 1] = last

  if ((i < n - 1) or (arr[n - 1] == key)):
    return i
  else:
    return -1

flag=1
while flag==1:
  print("1.Enter & display roll no.")
  print("2.Linear search")
  print("3.Sentinel search")
  ch=int(input("Enter your choice:"))
  if(ch==1):
    l1=getrno()
  elif(ch==2):
    roll=int(input("Enter a roll no to search: "))
    index=linear_search(l1,roll)
    if(index!=-1):
      print("Roll no ",roll," has attended the program.")
    else:
      print("Roll no ", roll, " has not attended the program.")
  elif (ch == 3):
    roll = int(input("Enter a roll no to search: "))
    l=len(l1)
    index = sentinel_search(l1,l,roll)
    if (index != -1):
      print("Roll no ", roll, " has attended the program.")
    else:
      print("Roll no ", roll, " has not attended the program.")
  else:
    print("Invalid choice.\nProgram Terminated.")
    flag=0