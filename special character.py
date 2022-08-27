user=input("enter the characters")
if user>="a" or user<="z" or user>="A" or user<="Z":
    print("alphabet")
elif user>=0 or user<=9:
    print("digit")
else:
    print("special character")
