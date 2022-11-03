from fractions import Fraction

c = 0


def input_complex():
    global c
    a = int(input('\tВведите действительную часть числа: '))
    b = int(input('\tВведите мнимую часть числа: '))
    c = complex(a, b)
    print(f'Комплексное число: {c}\n')
    return c


def input_rac():
    global c
    c = Fraction(input('\tВведите число: '))
    return c
