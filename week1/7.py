numbers = input("Enter numbers: ")
list = numbers.split()
for n in list:
    num = int(n)
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)