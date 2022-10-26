
num1=float(input("Enter no 1 : "))
num2=float(input("Enter No 2 : "))
opr=input("Enter Operator : ")
output=None
if opr=="+":
    output=num1+num2

if opr=="-":
    output=num1-num2

if opr=="*":
    output=num1*num2

if opr=="/":
    output=num1/num2



print("Your calculation is : ",output)

if num1 < 7:
    print ("Enter no more than 3")
elif num1 ==7:
    print ("Num1 is equal to 3")
else:
    print ("num1 is greater that 3")
