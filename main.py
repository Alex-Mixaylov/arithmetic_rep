# main.py
def add(x, y):
    """Сложение x и y"""
    return x + y
def subtract(x, y):
    """Вычитание y из x"""
    return x - y
def multiply(x, y):
    """Умножение x на y"""
    return x * y
def divide(x, y):
    """Деление x на y. Ошибка, если y равно 0."""
    if y == 0:
        return "Деление на ноль!"
    return x / y
