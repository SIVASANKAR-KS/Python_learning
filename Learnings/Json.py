import json

#JSON to Python
x='{"name":"Siva", "age":30, "city":"chennai"}'
y=json.loads(x)
print(y)


x={"name":"Siva", "age":30, "city":"chennai"}
y=json.dumps(x)
print(y)


x = {
    "name": "Nivash",
    "age":27,
    "married":True,
    "divorced":False,
    "children":("Ann", "Billy"),
    "pets":None,
    "cars": [
        {"model":"BMW 230", "mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]

}
print(json.dumps(x, indent=4, sort_keys=True))