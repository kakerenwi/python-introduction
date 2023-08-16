import requests

BASE_URL ="https://reqres.in"

# list users
def list_users():
    print("Request: List users......")
    response = requests.get("{}/api/users".format(BASE_URL))
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

users = list_users()
print(users)


# single user with a variable or argument
def list_user(user_id):
    print("Request: List user......", user_id)
    response = requests.get("{}/api/users/{}".format(BASE_URL, user_id))
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

print() # print an empty line before the response
list_user(4)
list_user(5)
list_user(1)

# create user
def create_user(user_information):
    print("Request: create user......", user_information)
    response = requests.post("{}/api/users".format(BASE_URL), user_information)
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

print()
create_user({
    "name": "Black Panther",
    "job": "Save Wakanda"
})

# Update user (Both put and patch)
def update_user(user_id, user_data):
    print("Request: update user......", user_data)
    response = requests.put("{}/api/users/{}".format(BASE_URL, user_id), user_data)
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

print()
update_user(5, {
    "name": "morpheus",
    "job": "zion resident"
})

# delete user
def delete_user(user_id):
    print("Request: delete user......", user_id)
    response = requests.delete("{}/api/users/{}".format(BASE_URL, user_id))
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

print()
delete_user(1)

