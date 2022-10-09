# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [2, 4, 5, 2, 5, 5, 33, 5, 2, 2, 2, 2,3,5,5,5,5]
# my_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# my_list = [2,2,2,2,2,2,3,3,3,3,3]

print('Исходный список: ',my_list)


#**************Альтернативное решение***************
# def sort_list(my_list):
#     for i in range(0, len(my_list)-1):
#         for j in range(i + 1, len(my_list)):
#             if my_list[j] <  my_list[i]: # Если значение справа больше, то переставляем
#                 temp = my_list[i]
#                 my_list[i] = my_list[j] 
#                 my_list[j] = temp
#     return my_list
#
# new_sorted_list =sort_list(my_list)
#**************Альтернативное решение***************

new_sorted_list = sorted(my_list) #Сортировка списка встроенной функцией sorted
print('Получили сортированный список',new_sorted_list)

res_list = []
res_list.append(new_sorted_list[0])
#Далее оставляем только уникальные значения
for i in range(1,len(new_sorted_list)):
    if new_sorted_list[i-1] != new_sorted_list[i]:
        res_list.append(new_sorted_list[i])

print('Неповторяющихся элементы исходного списка: ', res_list)