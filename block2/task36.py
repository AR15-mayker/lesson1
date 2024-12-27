# Ввод цифр трехзначного числа a3a2a1 и двузначного числа b2b1
a3 = int(input("Введите цифру сотен (a3): "))
a2 = int(input("Введите цифру десятков (a2): "))
a1 = int(input("Введите цифру единиц (a1): "))
b2 = int(input("Введите цифру десятков (b2): "))
b1 = int(input("Введите цифру единиц (b1): "))

# Вычисляем результат
result = (a3 * 100 + a2 * 10 + a1) + (b2 * 10 + b1)

# Получаем цифры из результата
c3 = result // 100  # Сотни
c2 = (result // 10) % 10  # Десятки
c1 = result % 10  # Единицы

# Выводим цифры результата
print("Цифры суммы:")
print("Цифра сотен (c3):", c3)
print("Цифра десятков (c2):", c2)
print("Цифра единиц (c1):", c1)