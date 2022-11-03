import controller as c

print('Выберите калькулятор:\n\t 1. рациональный\n\t 2. комплексный\n')

calc = input('Тип калькулятора № ')
if calc == '1':
    c.button_click_rac()

if calc == '2':
    c.button_click_complex()
