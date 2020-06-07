# Вы играете в компьютерную игру, дошли до схватки с финальным боссом, но вот беда: ваш компьютер "заглючил", 
# и вы не можете управлять персонажем в игре. Босс атакует и каждую секунду наносит один удар, 
# который отнимает у вас 80 единиц здоровья. На схватку с боссом вы вышли с 500 единицами здоровья. 
# Создайте цикл, позволяющий понять, через сколько секунд босс вас убьет.

# В результате работы программа должна вывести на экран число секунд, в течение которых будет длиться схватка. 
# Ответ должен быть выведен на экран в виде целого числа без какого-либо дополнительного поясняющего текста.

# Для проверки используйте переменную current_health для сохранения текущего уровня здоровья и изменяйте её по ходу цикла, 
# и — переменную attack = 80 для хранения значения атаки Босса.


current_health = 500
attack = 80
life_time = 0

while current_health > 0:
    life_time +=1
    current_health -= attack
else:
    print(life_time)
