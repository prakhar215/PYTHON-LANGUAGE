usename=input("Enter Username:")
password=input("Enter Password:")
if(usename == "prak" and password == "123"):
    print("Successfully Logged In")
else:
    if(usename != "prak"):
        print("Wrong Usename")
    else:
        print("Wrong passsword")