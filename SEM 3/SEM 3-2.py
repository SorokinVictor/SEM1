# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# stroka1 = 'qwe'
# count = 0
# for i in range(len(list1)):
#     if list1[i] == stroka1:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# if count != 2:
#     print(-1)

# list1 = ["123", "234", 123, "567"]
# stroka1 = '123'
# count = 0
# for i in range(len(list1)):
#     if list1[i] == stroka1:
#         count += 1
#     if count == 2:
#         print(i)
#         break
# if count != 2:
#     print(-1)