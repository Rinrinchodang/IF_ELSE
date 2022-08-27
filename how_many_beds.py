girls=int(input("enter the number of girls"))
beds=int(input("enter the number of beds"))
total=girls-beds
total2=beds-girls
if girls>beds:
    print(total,"girl is more")
elif beds>girls:
    print(total,"bed is left")
else:
    print("nothing")

