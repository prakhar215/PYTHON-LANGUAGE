word=str(input("Enter the word:"))
vovel='aeiou'
count=0
for ch in word:
    if(ch=='a' or ch=='e'or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("The value of total vovels in the vord is",count)