email = input("Enter an email address: ")
pos = email.index("@")
domain = email[pos + 1:]
print("Domain:", domain)