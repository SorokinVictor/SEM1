# №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input("Введите существующий номер дня недели: "))
# if day == 6 or day == 7:
#     print ('Это выходной день')
# elif day >= 1 and day <= 5:
#     print ('Это рабочий день')

# №2. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# ⋁ - ИЛИ. ⋀ - И.
#
# for x in range (2):
#     for y in range(2):
#         for z in range(2):
#             print ((x,y,z), not (x or y or z) == (not x and not y and not z))

# №3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#
# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# if ( x > 0 and y > 0):
#     print ('Точка находится в 1 четверти')
# elif ( x < 0 and y > 0):
#     print ('Точка находится во 2 четверти')
# elif ( x < 0 and y < 0):
#     print ('Точка находится в 3 четверти')
# elif (x > 0 and y < 0):
#     print('Точка находится в 4 четверти')
# else:
#     print('Введите значения x и y неравное 0')

# №4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input('Введите номер четверти: '))
# if number == 1:
#     print ('x > 0, y > 0')
# if number == 2:
#     print ('x < 0, y > 0')
# if number == 3:
#     print('x < 0, y < 0')
# if number == 4:
#     print ('x > 0, y < 0')
# else:
#     print ('Такой четверти не существует')

# Альтернативное решение задания №4 :

# q = int(input('Input number of Quoter :'))
#
# match q:
#     case 1:
#         print(' X > 0 and Y > 0')
#     case 2:
#         print(' X < 0 and Y > 0')
#     case 3:
#         print(' X < 0 and Y < 0')
#     case 4:
#         print(' X > 0 and Y < 0')
#     case _:
#         print('Uncorrect number')

#
# №5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# x1 = int(input('Введите кординату x точки A: '))
# y1 = int(input('Введите кординату y точки A: '))
# x2 = int(input('Введите кординату x точки B: '))
# y2 = int(input('Введите кординату y точки B: '))
# distance = (((x2 - x1) * (x2-x1) + (y2 - y1) * (y2 - y1)) ** 0.5)
# print (round(distance,2))

# Алетернативное решение задания №5:

# import math
#
# x1 = int(input('Введите кординату x точки A: '))
# y1 = int(input('Введите кординату y точки A: '))
# x2 = int(input('Введите кординату x точки B: '))
# y2 = int(input('Введите кординату y точки B: '))
#
# distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print (round(distance,2))