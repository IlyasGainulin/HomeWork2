#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
#- [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

def mult_list(list1):
    l = len(list1) // 2 + 1 if len(list1) % 2 != 0 else len(list1) // 2
    work_list = [list1[i]*list1[len(list1) - i - 1] for i in range(l)]
    print(work_list)

list1 = [2, 3, 4, 5, 6]
mult_list(list1)
list1 = list(map(int, input("Введите числа через пробел:\n").split()))
mult_list(list1)