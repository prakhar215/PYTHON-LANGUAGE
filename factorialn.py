def fac_cal(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
n=int(input("Enter the number :"))
print("The factorial is :",fac_cal(n))