only_marks=[]
def avg_marks(marks):
    for i in marks:
        if (i!='ab'):
            only_marks.append(i)

    sum=0
    for i in range(0,len(only_marks)):
        sum=sum+int(only_marks[i])
    avg=sum/len(only_marks)
    print("Average marks of the class are: ",avg)


def high_low_marks(marks):
    def high_marks():
        score=0
        for i in marks:
            if(i=="ab"or i=="AB"):
                continue
            elif(score==0):
                score=i
            elif(score<i):
                score=i
        print("Higest score is: ",score)
    high_marks()

    def low_marks():
        score=0
        for i in marks:
            if(i=="ab"or i=="AB"):
                continue
            elif(score==0):
                score=i
            elif(score>i):
                score=i
        print("Lowest score is: ",score)
    low_marks()

def absent_cnt(marks):
    count=0
    for i in marks:
        if(i=="ab" or i=="AB"):
            count=count+1
    print("Totalnumber of absent students = ",count)

def freq(marks):
    max=0
    res=marks[0]
    for i in marks:
        freq=marks.count(i)
        if(freq>max):
            max=freq
            res=i
    print("Marks with higest frequency are: ",str(res))

n=int(input("Enter the noof students in class: "))
marks=[]
print("Enter marks obtained: ")
for i in range(n):
    marks.append(input())
print("Marks obtained: ",marks,"\n")
flag=1
while(flag==1):
    print("*****MENU*****\n")
    print("1.Average marks.\n2.Higest and Lowest marks.\n3.Count of absent students.\n4.Marks with higest frequency.\n")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        avg_marks(marks)
    elif(ch==2):
        high_low_marks(marks)
    elif(ch==3):
        absent_cnt(marks)
    elif(ch==4):
        freq(marks)
    else:
        print("Invalid choice.\nProgram terminated.")
        flag=0