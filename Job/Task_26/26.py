# Задача 26:	
# Задайте число. 
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number_fibbonachi = int(input("Введите число: "))

def fibfonachi (number):

    if number < 2:
        print("Вы ввели не верное число, попробуйте ещё раз!")
    else:
        massiv = []
        massiv_plus = [0,1]
        massiv_minus = []

        count_index = 2
        while count_index < number:
            massiv_plus.append(massiv_plus[count_index-1] + massiv_plus[count_index-2])
            count_index += 1
        for i in massiv_plus[-1:-int(len(massiv_plus)):-1]:
            massiv_minus.append(-i)

        massiv = massiv_minus + massiv_plus
        print(f"Cписок чисел Фибоначчи, в том числе и отрицательные индексы:\n{massiv}")

fibfonachi(number_fibbonachi)