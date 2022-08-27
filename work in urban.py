age=int(input("enter the age"))
sex=input("enter the sex")
marraige=input("enter the marital_status")
if sex=="female":
    print("work only in urban areas")
elif sex=="male":
    if age>=20 and age<=40:
        print("work anywhere")
    elif sex=="male":
        if age>=40 and age<=60:
            print("work in urban areas")
    else:
        print("error")

# age=int(input("enter the age"))
# sex=input("enter the sex")
# marraige=input("enter the marital_status")
# if sex=="female":
#     print("work only in urban areas")
# elif sex=="male"and age>=20 and age<=40:
#     print("work anywhere")
# elif sex=="male" and age>=40 and age<=60:
#     print("work in urban areas")
# else:
#     print("error")