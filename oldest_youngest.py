num=int(input("enter the number"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num>num1 and num>num2:
    print("num is the oldest")
elif num1>num2 and num1>num:
    print("num1 is the oldest")
elif num2>num and num2>num1:
    print("num2 is the oldest")
if num<num1 and num<num2:
    print("num is the youngest")
elif num1<num2 and num1<num:
    print("num1 is the youngest")
else:
    print("num2 is the youngest")
