#import statistics
#from statistics import mode
only_marks = []
def avg_marks(marks):
    for i in marks:
        if(i!='ab'):
            only_marks.append(i)

    sum=0
    for i in range (0,len(only_marks)):
        sum=sum+int(only_marks[i])
    print("Total marks: ",sum)
    avg=sum/len(marks)
    print("Average of class :",avg)

def high_low_marks(marks):

    def high_score():
        score=0
        for i in marks:
            if i=='ab':
                continue
            elif score==0:
                score=i
            elif score<i:
                score=i
        print("Highest Score : ",score)
    high_score()

    def low_score():
        score=0
        for i in marks:
            if i=='ab':
                continue
            elif score==0:
                score=i
            elif score>i:
                score=i
        print("Lowest Score : ",score)
    low_score()

def count_ab(marks):
    cnt=0
    for i in marks :
        if i=='ab':
            cnt=cnt+1
    print("Count of absent student : ",cnt)

def high_freq(marks):
    max=0
    res=marks[0]
    for i in marks:
        freq=marks.count(i)
        if freq>max:
            max=freq
            res=i
    print("Marks with highest frequency : ",str(res))


no_of_students=int(input("Enter total number of students : "))
marks=[]
print("\nEnter Marks of students :")

for i in range (no_of_students):
    score=marks.append(input())
print("MARKS OBTAINED : ",marks,"\n")

flag=1

while(flag==1):
    print("*****MENU*****")
    print("1.Average marks\n2.Highest and lowest mark\n3.Count of absent student\n4.Display marks with highest frequency")
    print("\nEnter choice : ")
    ch=int(input())
    if(ch==1):
        avg_marks(marks)
    elif(ch==2):
        high_low_marks(marks)
    elif(ch==3):
        count_ab(marks)
    elif(ch==4):
        high_freq(marks)
    else:
        print("Invalid choice   !!")
        flag=0
