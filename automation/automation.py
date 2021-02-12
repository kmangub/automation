import re

phoneRegex = re.compile (r"/\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/")
emailRegex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

phone_numbers = []
lines = []
emails = []

with open('assets/potential-contacts.txt', 'r') as file2read:
    for currentline in file2read:
        lines.append(currentline)

    
    for line in lines:
    
        if emailRegex.search(line):
            get_email = emailRegex.search(line)
            # print(get_email)
            found = get_email.group()
            emails.append(found)
            
file2read.close()
# print(lines)

emails.sort()

print(emails)