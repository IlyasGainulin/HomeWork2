#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

s = ""
n = int(input("Введите число:\n"))
while n != 0:
    s = str(n % 2) + s
    n //=2
print(f'Преобразованное число в двоичной системе = {s}')