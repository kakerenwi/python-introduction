import requests

# list users
response = requests.get("https://reqres.in/api/users")
print(response)
print(response.json())

print()

# list single user
response = requests.get("https://reqres.in/api/users/3")
print(response)
print(response.json())

print()
# create user
result = requests.post("https://reqres.in/api/users", {
    "name": "ironman",
    "job": "save the world"
})
print(result)
print(result.json())


