cost=int(input("enter the quantity"))
total=cost*100
percentage=10/100*total
if total>=1000:
    print("per 10perdiscount=",percentage,"total price",total)
elif total<=1000:
    print("no discount",percentage,"actual price",total)
else:
    print("wrong")