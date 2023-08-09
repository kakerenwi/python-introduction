print("Mobile password simulation")

total_limit = 5

attempt_count = 0

correct_password = 1234

while attempt_count < total_limit:
    tried_password = int(input("Enter password: "))
    if correct_password == tried_password:
        print("login successful")
        break
    attempt_count = attempt_count + 1

    if attempt_count == 5:
        print("lock the phone")
        

