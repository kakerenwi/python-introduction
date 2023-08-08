# Using if and else in assignment2. If company name is JJTech/Microsoft, 70% partner gift coupon will be sent
# to the company.Coupon> email. If not 10% Regular Gift coupon to the email addresses.  
emails = [
    "vamsi@jjtech.com",
    "ironman@amazon.in",
    "hulk@accenture.org",
    "spiderman@microsoft.com",
    "captain.america@google.us"
]

companies = []

for i in emails: # for iteration (loop)
    print(i)
    data = i.split("@")
    company_details = data[1].split(".")
    print(company_details[0])
    companies.append(company_details[0])

    if company_details[0] == "jjtech" or company_details[0] == "microsoft":
        print("Sending COUPON70 to email ", i)
    else:
        print("Sending COUPON10 to email ",i)
        
    print(companies)