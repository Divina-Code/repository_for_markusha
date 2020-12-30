
word = 'АНТАРКТИДА'
letters = []
for a in word:
    letters.append("_")

print(letters)
print(' '.join(letters))


answer = input("Букву или слово:")
for a in range(len(word)):
    if answer == word[a]:
        letters[a] = word[a]

print(''.join(letters))

