string  = 'Нет'
no = 0
for i in range(5):
    #answer = input("Любите ли вы Python?\n")
    if string.lower() ==  "да":
         print("Это отлично!")
    else:
        no=no+1
        if no >= 5:
            print("Это безнадёжно!")
        else:
            print("Увы, это неправильный ответ")
