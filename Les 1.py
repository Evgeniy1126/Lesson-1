from multiprocessing.managers import Value

x = 2 # переменная int
y = 4 # переменная int
z = x*y # умножение 2-х переменных
# вывод значений z
print("z:", z)
#float
per1 = 3.2 # переменная float
per2 = 4.1 # переменная float
per3 = per2/per1
# вывод значений per3
print("per3:", per3)
# str
per4 = "Евгений" # переменная str
per5 = "Вечер" # переменная str
per6 = "Хороший" # переменная str
per7 = f"{per4} {per6} {per5}!"
# вывод значений per7
print(per7)
# "True|false - правильно или нет
def check_expression (per8, per9, per10):
    return per8 + per9 == per10
# ввод значений
try:
    per8 = int(input("Введите первое число (per8): "))
    per9 = int(input("Введите второе число (per9): "))
    per10 = int(input("Введите результат (per10): "))
    # Проверка результата if check_expression(per8, per9, per10):
    if check_expression(per8, per9, per10):
         print(f"{per8} + {per9} = {per10} - Верно!")
    else:
         print(f"{per8} + {per9} = {per10} - Неверно!")
except ValueError:
    print('Пожалуйста, введите целые числа!')
# тип данных none
per11 = None
if per11 is None:
   print("переменная не имеет значения.")
else:
   print("переменная имеет значение:", per11)