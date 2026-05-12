a = input("Enter a word: ")
if len(a) > 1:
    new = a[-1] + a[1:-1] + a[0]
else:
    new = a

print(new)