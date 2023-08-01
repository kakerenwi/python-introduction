email = "vamsi.chunduru@jjtech.com"  # jjtech (to take out jjtech out of the email)

data = email.split("@")  # ['vamsi.chunduru', 'jjtech.com']

print(data)

company = data[1].split(".") # ['jjtech', 'com']

print(company)

print(company[0]) # jjtech


