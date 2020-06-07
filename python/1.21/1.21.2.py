#string = input()
string = 'абстракция'
for i in string:
    if i.lower() in "абв":
        continue
    print(i, end="")