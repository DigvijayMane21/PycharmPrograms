# Simple Calculator:
print('''At this initial stage the calculator can perform:
Addition(+)
Substraction(-)
Multiplication(*)
Division(/)
Exponents(**)
Get the remainder of a division(%)
Get the quotient of a division(//)
''')
n1=float(input("Enter the first number:"))
opr=input("Enter the operator which you want to run:")
n2=float(input("Enter the second number:"))
if (opr=="+"):
    print(n1+n2)
elif (opr=='-'):
    print(n1-n2)
elif (opr=='*'):
    print(n1*n2)
elif (opr=='/'):
    print(n1/n2)
elif (opr=='**'):
    print(n1**n2)
elif (opr=='%'):
    k=int(n1%n2)
    print(k)
elif (opr=='//'):
    m=int(n1//n2)
    print(m)
else:
    print("Syantax error")
