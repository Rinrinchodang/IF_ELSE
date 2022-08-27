side_1=int(input("enter the length of side_1"))
side_2=int(input("enter the length of side_2"))
side_3=int(input("enter the length of side_3"))
if side_1==side_2==side_3:
    print("equilateral")
elif side_1==side_2!=side_3 or side_1==side_3!=side_2 or side_2==side_3!=side1:
    print("isosceles")
else:
    print("scalene")


x=int(input("enter the sides of triangle:"))
y=int(input("enter the sides of triangle:"))
z=int(input("enter the sides of triangle:"))
if x==y==z:
    print("equi")
elif x==y or y==z or z==x:
    print("iso")
else:
    print("sca")
