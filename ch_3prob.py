info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]
dict={}
unique=set()
for tup in info:
    unique.add(tup[1])
print(unique)
for name,course in info:
    if (dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
for name,course in info:
    if ( course== "English"):
        print(name)