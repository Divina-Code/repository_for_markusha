pali = input("Эта программа может понять палиндром это или нет. \n Введи слово сюда")
pali = pali.split()
for a in range(len(pali)):
    x1 = pali[a]
    x2 = x1[::-1].lower()
    if x1.lower() == x2:
        print(pali[a], "это палиндром")
    else:
        print(pali[a], "это не палиндром")
