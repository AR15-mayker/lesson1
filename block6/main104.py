def cut_squares(a, b):
    squares = []  # Список для хранения количества квадратов и их размеров
    while a != 0 and b != 0:
        if a > b:
            count = a // b  # Количество квадратов со стороной b
            squares.append((b, count))  # Добавляем размер и количество
            a = a % b  # Оставшийся прямоугольник
        else:
            count = b // a  # Количество квадратов со стороной a
            squares.append((a, count))  # Добавляем размер и количество
            b = b % a  # Оставшийся прямоугольник
    return squares

# Размеры исходного прямоугольника
a = 425
b = 131

# Получаем список квадратов
squares = cut_squares(a, b)

# Выводим результат
print("Исходный прямоугольник будет разрезан на следующие квадраты:")
for size, count in squares:
    print(f"{count} квадратов со стороной {size}")
