a = int(input("Введите первое число а = "))
b = int(input("Введите второе число b = "))
d = str(input("Введите действие: "))
if d == "+":
    print("Сумма чисел равна = ", a + b)
elif d == "-":
    print('Разность чисел равна = ', a - b)
elif d == "*":
    print("Произведение чисел равно = ", a * b)
elif d == "%":
    print("Остаток от деления чисел равен = ", a % b)
elif d == "/":
    print("Деление чисел равно = ", a / b)
elif d == "//":
    print("Целочисленное деление = ", a // b)
elif d == "**":
    print("Возведение в степень = ", a ** b)
    
    
