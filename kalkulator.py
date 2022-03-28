


what = input( " Что делаем? (+,-): " )

a = float( input( " Введите первое число: " ) )
b = float( input( " Введите второе число: " ) )

# Условия:

if what == '+':
    c = a + b

if what == '-':
    c = a - b
-----------
# Вывод ответа:

print("Результат: " + str(c))
-----------
# Вместо второго if можно написать elif

if what == '+':
    c = a + b
    print("Результат: " + str(c))
elif what == '-':
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана неверная операция!")

