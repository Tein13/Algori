''' 1
num = float(input('Введите число:'))
def easy(num):
    if num % 1 == 0:
        num = "Число простое"
        return num
    else:
        num = "Число не простое"
        return num
print(easy(num))
'''

'''2
numbers = input('Введите числа через пробел:')
a = list(map(int, numbers.split()))
n = len(a)
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
'''

'''3
list1 = input('Введите числа через проблел:')
numbers = list(map(int, list1.split()))
def max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(max_number(numbers))
'''

'''4
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

user_num = int(input("Введите число:"))
result = (f'Число Фибоначчи:{fib(user_num)}')
print(result)
'''

# 5
# def most_common_string(arr):
#     str_count = {}
#
#     for str in arr:
#         if str in str_count:
#             str_count[str] += 1
#         else:
#             str_count[str] = 1
#
#     max_count = 0
#     most_common = None
#     for st, count in str_count.items():
#         if count > max_count:
#             max_count = count
#             most_common = str
#
#     return most_common
#
# user_str = input()
# str = user_str.split()
# res = most_common_string(str)
# print("Наиболее часто встречающаяся строка:", res)
