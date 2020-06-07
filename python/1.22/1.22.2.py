# Пассажирский лифт имеет ограничение на перевозку: не более 400 кг единовременно. 
# Пусть на вход программе поступает вес (weight) входящих в лифт людей, а в случае, когда возникает перевес, 
# программа выдаёт предупреждение: "Перевес N кг". 
# Например, при перевесе в 15 кг должно быть выведено сообщение: "Перевес 15 кг". 
# Обратите внимание, что в эталонной фразе не используются знаки препинания.

weight = 77
carMax = 400
currentWeight = 0

while currentWeight < carMax:
    weight = input("Введите вес...\n")
    currentWeight += int(weight)
else:
    print("Перевес", (currentWeight-carMax),"кг")