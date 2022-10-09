# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
from random import randint

k = 0
list_koef = []
for i in range(k+1):
    list_koef.append(str(randint(0,100)))
    
# print(list_koef)

# list_koef = ['3' , '4' , '45', '4']
# list_koef = ['3' , '0' , '45', '4']
# list_koef = ['3' , '7' , '45']
# list_koef = ['3' , '0' , '45']
# list_koef = ['3' , '45']
# list_koef = ['0' , '45']
list_koef = ['45']
list_koef = ['0']
# print(list_koef)

# def end_equation(ist_koef):


equation = 'Y = '
if k >= 2:
    for i in range(len(list_koef)-2):
        if list_koef[i] != '0': # Проверка на нулевой множитель
            equation += list_koef[i] +'*'+'X'+'^'+ str(len(list_koef)-1-i) + ' + '
    if list_koef[-2] != '0':
        equation += list_koef[-2]+'*'+'X' + ' + ' + list_koef[-1]
    else: equation += list_koef[-1]
elif k == 1: #Можно записать elif k:
    if list_koef[-2] != '0':
        equation += list_koef[-2]+'*'+'X' + ' + ' + list_koef[-1]
    else: equation += list_koef[-1]    
else: equation += list_koef[-1]

print(equation)

with open('file_equa.txt', 'w') as my_data:
    my_data.write(equation)    
