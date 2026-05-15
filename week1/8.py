pwd = input("Enter password: ")
got_letter = False
got_num = False
got_sym = False
for ch in pwd:
    if ch.isalpha():
        got_letter = True
    elif ch.isdigit():
        got_num = True
    elif ch in "@#$%&":
        got_sym = True
if len(pwd) < 6 or (got_letter and not got_num and not got_sym):
    print("Weak")
elif len(pwd) >= 8 and got_letter and got_num and got_sym:
    print("Strong")
elif len(pwd) >= 6 and got_letter and got_num:
    print("Moderate")