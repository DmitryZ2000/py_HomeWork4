# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

data1 = '50*X^5 + 40*X^4 + 30*X^3 + 20*X^2 + 10*X + 1000'
# data1 = '50*X^5 + 40*X^4 + 30*X^3 + 20*X^2 + 1000'
# data1 = '50*X^5 + 40*X^4 + 30*X^3 + 10*X + 1000'
data2 ='500*X^5 + 400*X^4 + 300*X^3 + 200*X^2 + 200*X + 2000'
# data2 ='500*X^5 + 400*X^4 + 300*X^3 + 200*X + 2000'

def end_equation(list_koef, equation):
        if list_koef[-2] != '0':
            equation += list_koef[-2]+'*'+'X' + ' + ' + list_koef[-1]
        else: equation += list_koef[-1]
        return equation

print('Чтение из файла')
# path1 = 'file_equa1.txt'
# path2 = 'file_equa2.txt'
# f = open(path1, 'r')
# data1 = f.read()
# f.close()

# f = open(path2, 'r')
# data2 = f.read()
# f.close()
# print('Данные из файла', data1)
# print('Данные из файла', data2)
print('Чтение из файла закончено')

data_list1 = data1.split(' + ')
data_list2 = data2.split(' + ')
print('Fist eqation: ', data_list1)
print('Second eqation:', data_list2)

def split_data(data_list):
    data_dic = {}
    # data_dic1['1'] = []
    for i in range(len(data_list)):
        if '^' in data_list[i]:
            stepen = data_list[i].split('^')[1] #Степень во втором элементе строки
            data_dic[stepen] = data_list[i].split('*')[0]
        elif (not '^' in data_list[i]) and 'X' in data_list[i] :
            data_dic['1'] = data_list[i].split('*')[0]
        else: data_dic['0'] = data_list[i]
    return data_dic   

data_dic1 = split_data(data_list1)

print('First Dictionary', data_dic1)
data_dic2 = split_data(data_list2)
print('Second Dictionary', data_dic2)

#Далее создание словоря
dic_res = {}
for key1 in data_dic1.keys(): #Вывод ключей    
    for key2 in data_dic2.keys():
        # print(key2*4)        
        if key1 == key2:
            dic_res[key1] = str(int(data_dic1[key1]) + int(data_dic2[key2]))
        elif key1 in data_dic1.keys() and (not key1 in data_dic2.keys()):            
            dic_res[key1] = str(int(data_dic1[key1]))
        elif key2 in data_dic2.keys() and (not key2 in data_dic1.keys()):
            # print(key2)
            dic_res[key2] = str(int(data_dic2[key2]))
print('Final Dictionary', dic_res)

k = int(list(dic_res.keys())[0])
# print(k)
list_koef = list(dic_res.values())
# print(list_koef)

equation = 'Y = '

if k >= 2:
    for i in range(len(list_koef)-2):
        if list_koef[i] != '0': # Проверка на нулевой множитель
            equation += list_koef[i] +'*'+'X'+'^'+ str(len(list_koef)-1-i) + ' + '
    equation = end_equation(list_koef, equation) #Вызов функции окончания выражения
elif k == 1: #Можно записать elif k:
    equation = end_equation(list_koef, equation) #Вызов функции окончания выражения
else: equation += list_koef[-1]

print(equation)

with open('file_equa_task405.txt', 'w') as my_data:
    my_data.write(equation)   