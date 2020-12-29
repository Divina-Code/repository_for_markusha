import random
Numbers = "1234567890"
Letters = "abcdefghijklmnopqrstuvwxyz"
BigLatters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Specialist_Symbols = "+-/*!&$#?=@<>"

Length = int(input("Какова длина пароля? \n Пиши сюда цифру: "))
passwd = " "

for a in range(Length):
   passwd += random.choice(Numbers+Letters+BigLatters+Specialist_Symbols)
print(passwd)

