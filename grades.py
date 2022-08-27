physics=int(input("enter the physics marks"))
chemistry=int(input("enter the  chemistry marks"))
biology=int(input("enter the biology marks"))
mathematics=int(input("enter the mathematics marks"))
computer=int(input("enter the computer marks"))
total=physics+chemistry+biology+mathematics+computer
ave=total/5
percentage=(total/500)*100
print("per",percentage)
if physics>=90:
    print("grade A")
elif chemistry>=80:
    print("grade B")
elif biology>=70:
    print("grade C")
elif mathematics>=60:
    print("grade D")
elif computer>=40:
    print("grade E")
else:
    print("no grade")
