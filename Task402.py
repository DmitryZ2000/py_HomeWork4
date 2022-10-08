# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

def check_prime(n): #функция поиска простых множителей
    multiplier = []
    for item in range(2, int(n**0.5)+1):
        if not n % item:
            multiplier.append(item)
            n = n // item
    return multiplier

# list_multiplier = check_prime(n)  - обошлись без дополнительного списка

check_prime_clear = []
print('Все найденные множества ',check_prime(n))

#Далее удаляем из полученного множества не простые числа
for item in check_prime(n):        
    if not len(check_prime(item)): # Если число простое, то множество будет пустым
        check_prime_clear.append(item)

print(f'Простые множители числа {n} составляют {check_prime_clear}')