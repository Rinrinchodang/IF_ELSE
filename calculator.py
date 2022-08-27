from tkinter import*
print("select any operation to perform:")
print("1.ADD")
print("2.SUBSTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
operation=int(input("select any operation to perform:"))
num=int(input("enter the number"))
num1=int(input("enter the number"))
if operation=="1":
    print("the sum is"+ (num)+(num1))
elif operation=="2":
    print("the difference is"+(num)-(num1))
elif operation=="3":
    print("the product is"+(num)*(num1))
elif operation=="4":
    print("the result is"+(num)/(num1))
else:
    print("invalid entry")
 




