x1 = float(input("Введите значение угла для минутной стрелки: "))
x2 = float(input("Введите значение полных часов и полных минут: "))
hours = int(x1 // 30)
minutes = int((x2 % 12) * 2)
print(f"Часы: {hours}. Минуты: {minutes}")
