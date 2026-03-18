num=[1,3,4,6,7,2,7,5,20,25,50,42]
x=20
index=0
for val in num:
    if(val == 20):
        print(f"{x} found at Index {index}")
        break
    index+=1