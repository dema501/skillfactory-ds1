number  = 173
for i in range(2, number):
    if number%i == 0:
        print("Не является простым")
        break

print("Простое")