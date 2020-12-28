isGuessed = True

while isGuessed:
    puzzle = "(270*2):2-35 = ?  "

    answer = input(puzzle)

    if answer == "100":
        print("Ну ты красавчик , так держать !")
        isGuessed == False
    elif answer == "135":
        print("Не , не угадал! ")
    else:
        print("Пересчитывай , либо покупай курс в МФТИ")

print("А ты хорош")
