student1 = {"name": "Joe", "age": 20, "gender": "male", "course": "bachelor of arts"}

student2 = { "gender": "male", "name": "mark", "age": 16, "course": "higher secondary"}

student3 = {"name": "christina","course": "higher secondary", "age": 16, "gender": "female"}

print(student1)

print(type(student1))

print(student2["course"])
print(student2["gender"])
print(student3["gender"])

student1["age"] = 21
print(student1)

student3["name"] = "Emma"
print(student3)

student2["results"] = True
print(student2)

print(student3.keys())

print(student3.values())

student3 = {"name": "christina","course": "higher secondary", "age": 16, "gender": "female"}

print(student3.items())

for key, val in student3.items():
    print(key, val)

student3.clear()
print(student3)






