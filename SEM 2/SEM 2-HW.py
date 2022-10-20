# №1. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# list = {}
# n = 1
# number = int(input('Введите число больше 1: '))
# if n >= 1:
#     while n <= number:
#         key = n
#         val = 3 * n + 1
#         list[key] = val
#         n += 1
# else:
#     print ('Неверно введено число n')
# print(f'Полученный список: {list}')
from datetime import datetime


# №2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# n = int(input('Введите число n: '))
# proizv = 1
# for i in range(1, n+1):
#     proizv *= i # полностью proizv = proizv * i
#     print(proizv, end = ' ')

# №3. Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

# a = int(input("Введите число N: "))
# i = 0
# n = 0
# lst = []
# while i <= a - 1:
#     i += 1
#     b = (1 + (1 / i)) ** i
#     lst.append(b)
#     n = n + b
# print("Список из n чисел последовательности (1+ (1/n))^n: ", lst)
# print("Сумма чисел данной последовательсти = ", round(n, 2))

# №4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random
#
# n = int(input('Введите n: '))
# lst = []
# for i in range(1, n + 1):
#     lst.append(random.randint(-n,n))
# print(lst)
#
# f = open('file.txt')
# ind1 = int(f.read(1))
# ind2 = int(f.read(2))
# f.close()
# print(f'Indexes from file.txt: {ind1}, {ind2}')
#
# mult = lst[ind1] * lst[ind2]
# print(mult)

# №5. Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

# def myShuffle(some_list):
#     if len(some_list) >= 3:
#         for i in range(0, len(some_list) - 1):
#             j = datetime.now().microsecond % len(some_list) - 1 #текущее время в микросекундах
#             some_list[i], some_list[j] = some_list[j], some_list[i]
#     else:
#         print("Перемешивать нечего")
#     return some_list
# list1 = [10, -12, -13, 8]
# print(f"{myShuffle(list1)}")