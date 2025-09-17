for i in range(3):
    a = float(input("Введите длину первой стороны: "))
    b = float(input('Введите длину второй стороны: '))
    c = float(input('Введите длину третьей стороны: '))
    p = (a + b + c)/2
    print(f'Площадь: {round((p*(p-a)*(p-b)*(p-c))**0.5,2)}')


