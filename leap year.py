year=int(input("enter the year"))
if year%4==0:
    print("leap yaer")
else:
    print("not leap year")
century_year=int(input("enter the century_year"))
if century_year%100==0:
    if century_year%400==0:
        print("leap century_year")
    else:
        print("not leap century_year")
else:
    print("not leap century_year")

year=int(input("enter the year"))
if year%4==0:
    print("leap year")
else:
    print("not leap year")
century=int(input("enter the century year"))
if century%400==0:
     print("leap century year")
else:
     print("not leap century year")