salary=int(input("Enter your salary:"))
tax=0
if (salary<=30000):
    tax=(salary*5)/100
elif (salary>30000 and salary<70000):
    tax=((((salary-30000)*15)/100)+(30000*5/100))
else:
    tax=(((salary-70000)*25)/100+(((70000-30000)*15)/100)+(30000*5/100))
print("The total tax payable is :",tax)