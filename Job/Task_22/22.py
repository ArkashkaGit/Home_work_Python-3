# Задача 22:
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

number = int(input("Введите число чисел в спике:\n"))
random_list = []

# Создание рандомного списка
for i in range(0,number):
    i=random.randrange(1,9)
    random_list.append(i)
print(f"Создан рандомный список - {random_list}")

# функция находящая сумму элементов находящихся на нечётных позтциях
def summa_number(list):
    count = 0
    sum_number = 0
    for i in list[1::2]:
        sum_number += i
        count += 1
    if count < 2:
        print("в данном списке нет чисел на нечетный позизиях!")
    else:
        print(f"Сумма чисел находящихся на нечётных позициях равна - {sum_number}")

summa_number(random_list)

