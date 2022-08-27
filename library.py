expected_date=int(input("enter the expected_date"))
expected_month=int(input("enter the expected_month[1-12]"))
expected_year=int(input("enter the expected_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if expected_date==return_date:
    if expected_month==return_month:
        if expected_year==return_year:
            print("no fine")
        else:
            print("fine",(return_year-expected_year)*10000)  
    else:
        print("fine",(return_month-expected_month)*500) 
else:
    print("fine",(return_date-expected_date)*15)        
    

