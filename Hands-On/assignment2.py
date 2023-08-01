# To isolate and understand the companies from an email list of attendees at a conference.
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

    print(companies) # ['jjtech', 'amazon', 'accenture', 'microsoft', 'google']

# All of the above programming codes could have been written in a single line as below 
# for i in emails: 
#     companies.append(i.split("@")[1].split(".")[0])
#     print(companies)





