units=int(input("enter the electric unit charges"))
if units<=50:
    print(units*0.50+0.20/100)
elif units<=100:
    print(units*0.75+0.20/100)
elif units>=100:
    print(units*1.20+0.20/100)
elif units<250:
    print(units*1.50+0.20/100)
    