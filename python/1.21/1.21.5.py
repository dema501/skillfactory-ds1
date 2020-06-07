string = 'прелестная строка'

for i, l in enumerate(string):
    if i%2==0 and l in "ауоыиэяюёе":
        print('Строка мне не нравится!')
        break
else:
    print('Какая хорошая строка!')