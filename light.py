#Задачи на циклы и оператор условия_light
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.
'''
for i in range(5):
    print(i, '0000')

'''
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''
count_ = 0
a = 0
while a < 10:
    if int(input('введите число')) == 5:
        count_ += 1
    a += 1

if count_ > 4 or count_ < 2:
    print(f'вы ввели цифру 5 {count_} раз')
else:
    print(f'вы ввели цифру 5 {count_} раза')
    
'''
Задача 3
Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''
prod = 1
for i in range(1,11):
    prod *= i
print(prod)

'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5
Вывести цифры числа на каждой новой строке.
'''
for i in input('Введите число: '):
    print(i)

