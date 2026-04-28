try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except:
    print("File not found!")
finally:
    file.close()
    print("File closed.")
