password = input("Enter password: ")
l = False
n = False
s = False
for c in password:
    if c.isalpha():
        l = True
    elif c.isdigit():
        n = True
    elif c in "@#$%&":
        s = True
if len(password) < 6 or (l and not n and not s):
    print("Weak")
elif len(password) >= 8 and l and n and s:
    print("Strong")
elif len(password) >= 6 and l and n:
    print("Moderate")