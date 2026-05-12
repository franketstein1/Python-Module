email = input("Enter an email address: ")
a = email.index("@")
domain = email[a + 1:]
print(f"Domain: {domain}")