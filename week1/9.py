sentence = input("Enter a sentence: ")
words = sentence.split()
output = []
for idx, word in enumerate(words):
    if idx % 2 == 1:
        output.append(word[::-1])
    else:
        output.append(word)
print(" ".join(output))