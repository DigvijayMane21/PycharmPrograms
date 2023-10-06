import array as arr
def getrno():
  a=[]
  nstud=int(input("enter total number of student="))
  for i in range(0,nstud):
    a.append(int(input("enter the roll no=")))
  print("Array of students: ",a)
  return a

def binary_search_R(a, l, r, x):
  if r >= l:
    mid= l + (r-l)//2
    if a[mid] == x:
      return mid
    elif a[mid]> x:
      return binary_search_R(a, l, mid - 1, x)
    else:
      return binary_search_R(a, mid+ 1, r, x)
  else:
    return -1

unsortA=getrno()
roll = int(input("Enter the Roll Number to be search : "))
index = binary_search_R(unsortA, 0, len(unsortA) - 1, roll)
if index == -1:
  print("Roll number", roll, "has not Attended the training program")
else:
  print("Roll number", roll, " at the index", index, "has Attended the training program")