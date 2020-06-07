
import numpy as np


def game_core_v3(number):
    '''Применим бинарный поиск для поиска загаданное числа.
        Обозначим правую границу поиска переменной right,
        левую границу – left. Функция принимает загаданное
        число и возвращает число попыток'''

    count = 0

    left = 0
    right = 100  # Левая и правая граница поиска
    while (right - left) > 1:  # Пока правая граница правее левой
        middle = int((left + right) / 2)
        if (middle >= number):
            right = middle  # Передвигаем правую границу
        else:
            left = middle  # Иначе передвигаем левую границу

        count += 1

    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать,
        как быстро игра угадывает число'''

    count_ls = []

    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)

    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__ == "__main__":
    score_game(game_core_v3)
