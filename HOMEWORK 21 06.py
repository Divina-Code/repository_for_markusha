player1 = 0
player2 = 0
player3 = 0

inGame1 = True
inGame2 = True
inGame3 = True

while inGame1:
    print("*"*50)
    if inGame1:
        take_card = input("Игрок №1 ,Вы будете брать карту ? [ДА/НЕТ] 👕 : ")
        if take_card == "ДА":
            player1+=3
            print("Оу , не переборщи с очками , ведь у тебя их целых 👻 : ", player1)
        elif take_card == "НЕТ":
            print("На этом твой набор карт закончен , мы переходим к следующему игроку , твоих очков вот столько 😵 : ", player1)
            inGame1 = False
            player1 = False
        else:
            print("Возможно какая-то ошибочка, я уже работаю над ней 👹")
    if player1 >= 21:
        inGame1 = False
        player1 = False
while inGame2:
    print("@"*50)
    if inGame2:
        take_card = input("Игрок №2, Теперь ваша очередь, Вы будете брать карту? [ДА/НЕТ] 🤩 : ")
        if take_card == "ДА":
            player2+=3
            print("Игрок №2 , не переборщи с очками ! Их количество составляет 🧢 : ", player2)
        elif take_card == "НЕТ":
            print("К сожалению, ты закончил свой набор карт , мы переходим к следующему игроку 🙂 :", player2)
            inGame2 = False
            player2 = False
        else:
            print("Опять ошибочка , пиши пожалуйста [ДА/НЕТ] 👘 : ")
            if player2 >= 21:
                inGame2 = False
                player2 = False
while inGame3:
    print("#"*50)
    if inGame3:
        take_card = input("Здравствуй , Игрок №3, ваша очередь настала, Вы будете брать карту? [ДА/НЕТ] 😝 : ")
        if take_card == "ДА":
            player3+=3
            print("Игрок №3, иногда надо останавливаться с набором карт . Продолжим дальше? Их количество уже составляет 😊 : ", player3)
        elif take_card == "НЕТ":
            print("Игрок №3, вы окончили выбор карт. Ваш счет составляет 🤪 : ", player3)
            inGame3 = False
            player3 = False
        else:
            print("Это сырой код, хватит над ним издеватся ! Пиши только [ДА/НЕТ] 🥶 : ")
            if player3 >= 21:
                inGame3 = False
                player3 = False
