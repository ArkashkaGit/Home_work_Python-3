# Задача 25:	
# Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input("Введите число:\n"))
binary_number = bin(decimal_number)

print(f"десятичное число: {decimal_number}\nпреобразовыванно в двоичное: {binary_number}")


def calculator_binary(number):
    remains = str()
    while (number >= 1):
            remains = str(number % 2) + remains
            number = number // 2 
    return remains

print(f"десятичное число: {decimal_number}\nпреобразовыванно в двоичное: {calculator_binary(decimal_number)}")