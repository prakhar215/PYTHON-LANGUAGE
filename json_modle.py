import json
py_obj= {
    "name":"prakhar",
    "is student": None
}
json_str = json.dumps(py_obj)
print(type(json_str))
with open("data.json","r") as f:
    py_obj=json.load(f)
    print(py_obj)
    print("prakhar koshta")