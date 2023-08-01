name = "vamsi"

name1 = "IRONMAN"

username = "        vamsi        " # we can use strip to remove the space before and after the word

print(name.upper())

print(name1.lower())

print(name1.replace("IRON", "GOLD"))

print(username)

print(len(username))

corrected_name = username.strip()
print(len(corrected_name))

message = "hello everyone how are you"
print(message.split())

message = "hello everyone, how are you"
print(message.split(","))

email = "vamsi@gmail.com"
print(email.split("@"))

