H = int(input("Введите колличество часов: "))
M = int(input("Введите колличество минут: "))
S = int(input("Введите колличество секунд: "))

c = 12*3540/354
print((H*3600 + M*59 + S)/c)
