# Найти максимальное из пяти чисел
lst = [1,6,8,10,65]
max = lst[0]
for i in range(0,5): # range(len(lst))
    if lst[i] > max:
        max = lst[i]
print(max)