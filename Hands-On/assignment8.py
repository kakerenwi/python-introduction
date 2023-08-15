def greeting():
    print("hello everyone")

result = greeting()
print(result)

response = len("ironman")
print(response)

def validate_account(account_number):
    print("validating account: ", account_number)
    print("connecting to the database...")
    print("verifying in the database, for account: ", account_number)
    #print("account is valid")
    return False


print("Money to Withdraw 1000")
is_valid = validate_account(13443144)
if is_valid == True:
    print("withdrawing amount: 1000")

# return is used when you want to use the result later on in the code
# It is the result at the end of a function.

