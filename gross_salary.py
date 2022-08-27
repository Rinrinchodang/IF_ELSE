basic_salary=int(input("enter the salary of an employer"))
if basic_salary<=10000:
    HRA=0.20
    RA=0.80
    gross_salary=basic_salary*HRA*RA
    print("gross_salary",gross_salary)
if basic_salary<=20000:
    HRA=25
    RA=0.90
    gross_salary=basic_salary*HRA*RA
    print("gross_salary",gross_salary)
if basic_salary>20000:
    HRA=0.30
    RA=95
    gross_salary=basic_salary*HRA*RA
    print("gross_salary",gross_salary)
