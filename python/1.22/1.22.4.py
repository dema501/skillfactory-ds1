# На банковской карте хранятся 10 000 рублей. Хозяин карты написал программу, в которую вводит свои расходы (spent), 
# после чего программа показывает баланс (balance). Баланс выводится в виде целого числа без каких-либо дополнительных сообщений. 
# Например, при остатке 3500 рублей на экран выводится число 3500. Когда сумма средств на карте становится ниже нуля, 
# программа выводит сообщение: "Слишком большие расходы".

# Напишите программу, которая выводит на экран начальный баланс карты (число 10000), баланс после каждого списания и сообщение 
# "Слишком большие расходы" при достижении отрицательного баланса.

# Для проверки используйте переменную spent = 2800 и НЕ меняйте её по ходу цикла. Переменная balance должна меняться после каждого шага цикла.


spent = 2800
balance = 10000

while balance > 0:
    print(balance)
    balance -= spent
else:
    print("Слишком большие расходы")