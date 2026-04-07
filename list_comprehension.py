squares=[]
for i in range(6):
    squares.append(i*i)
print(squares)
#INSTEAD OF THIS SHORT METHOD IS LIST COMPREHENSION
SQUARES=[ i*i for i in range(10) if i%2 == 0 ]
print(SQUARES)