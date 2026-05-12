sentence = input("Enter a sentence: ")
w = sentence.split()
nw = []
c = 0
for i in w:
    if c % 2 == 1:
        nw.append(i[::-1])
    else:
        nw.append(i)
    c += 1
result = " ".join(nw)
print(result)