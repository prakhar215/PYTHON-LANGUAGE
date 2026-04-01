fi=open("sample.txt","x")
fi.write("some random text")
print(fi.read())
fi.close()