inProduct = False

productLIST = []

while inProduct != True:
    answer = int(input("Чтобы добавить продукт напишите циферку 1\nЧтобы удалить продукт напишите циферку 2\nЧтобы посмотреть что вы написали нажмите циферку 3\nНапиши циферку сюда:\t"))
    if answer == 1:
        product = input("Чтобы вы хотели добавить ?\t")
        productLIST.append(product)
    elif answer == 2:
        delete = int(input("Чтобы вы хотели удалить из списка?\t"))
        productLIST.pop(delete)
    elif answer == 3:
        print(productLIST)
    else:
        print("Хорошо ! Повторим цикл !")
