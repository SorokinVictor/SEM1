import logger as log


def calculator(a, b):
    point = input('\tВведите знак: ')
    if point == '+':
        result = a + b
        print(result)
        log.logger(f'{a}+{b}={result}')
    elif point == '-':
        result = a - b
        print(result)
        log.logger(f'{a}-{b}={result}')
    elif point == '*':
        result = a * b
        print(result)
        log.logger(f'{a}*{b}={result}')
    elif point == '/':
        if b == 0:
            print("Деление на 0 не допускается")
        else:
            result = a / b
            print(result)
            log.logger(f'{a}/{b}={result}')
