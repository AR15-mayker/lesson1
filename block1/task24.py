# TODO И как Владислав забрел в этот репо? Думаю, стоит смотреть что как и откуда копируется
# Гюнашян Владислав
# TODO оформить код + добавить округление для первого, второй не рабочий

from math import sin, sqrt

# a = int(input("Введите число a: "))

# print(f"sqrt(2 * a) + sin(abs(3 * a)) / 3.56 = {sqrt(2 * a) + sin(abs(3 * a)) / 3.56}")


x = int(input("Введите число x: "))

print(f"sin(3.2 + (1 - x)**0.5 / abs(5 * x)) \
      = {sin((3.2 + (1 - x)**0.5) / abs(5 * x))}")
