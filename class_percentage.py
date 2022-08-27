classes=int(input("enter the number of class held="))
attendence=int(input("enter the number of class attended="))
medical=input("enter yes or no=")
percentage=attendence/classes*100
print("per",percentage)
if medical=="yes":
    print("allow to sit")
elif percentage<75:
    print("not allow to sit")
elif percentage>=75:
    print("allow to sit")
else:
    print("not allow")
