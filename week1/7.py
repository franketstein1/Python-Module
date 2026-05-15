line = input("Enter numbers: ")
nums = line.split()
for item in nums:
    num = int(item)
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)