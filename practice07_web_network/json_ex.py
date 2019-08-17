import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print("##############")
a = json.dumps(j)
print(a)
print(json.loads(a))

with open('test.json', 'w') as f:
    json.dump(j, f)

with open('test.json', 'r') as f:
    print(json.load(f))
