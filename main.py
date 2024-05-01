# полный код с функцией деления
# main.py

import arithmetic as ar

# Тестирование функций из модуля arithmetic
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

print("Сложение:", ar.add(a, b))
print("Вычитание:", ar.subtract(a, b))
print("Умножение:", ar.multiply(a, b))
print("Деление:", ar.divide(a, b))


# Проверим деление на ноль
print("Проверка деления на ноль:", ar.divide(a, 0))

