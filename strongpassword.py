password=input("enter your password")
if len(password)>=7:
    if "@" in password or "#" in password or "$" in password or "%" in password or "&" in password or "*" in password or "-" in password:
        if "A" or "Z" in password:
            if "0" or "9" in password:
                if "a" or "z" in password:
                # if "0" or "9" in password:
                    print("strong password")
                else:
                    ("weak password")
            else:
                print("weak password")
        else:
            print("weak password")
    else:
        print("weak password")
else:
    print("invalid")

