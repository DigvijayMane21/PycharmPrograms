def menu():
    print("****MENU****")
    print("Enter your choice:")
    print("1.The average score of the class")
    print("2.highest and lowest score of the class")
    print("3.count of students who were absent for the class")
    print("display marks with highest frequency")
    print("5.exit")

if __name__=='__marks__':
    t_std=int(input("Enter total number of the students"))
    p_std = int(input("enter the present number of students"))
    a_std=t_std-p_std

    marks = [int(input(f" {i + 1})Enter marks: ")) for i in range(p_stud)]

    while run :
        menu()
        ch=int(input("Enter your choice:"))
        if ch==1:
            print(sum(marks)/a_std)
        elif ch==2:
            print(f"highest marks:{max_(marks)}")
            print(f"lowest marks: {min(marks)}")
        elif ch==3:
            print(sum(t_std-p_std))
        elif ch==4:
            print(f'{m_freq(p_std)}')
        elif ch==5:
            print("END")
            run=False

