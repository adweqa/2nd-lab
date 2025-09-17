for i in range(3):
    ed1 = input('Введите исходную единицу измерения ')
    ed2 = input('Введите целевую единицу измерения ')
    a = float(input('Введите значения исходной единицы измерения '))
    if ed1 == 'м' and ed2 == 'км':
        print(a/1000)
    elif ed1 == 'м' and ed2 == 'см':
        print(a*100)
    elif ed1 == 'м' and ed2 == 'мм':
        print(a*1000)
    elif ed1 == 'м' and ed2 == 'mi':
        print(a*0.00062136931818182)
    elif ed1 == 'м' and ed2 == 'yd':
        print(a *1.09361)
    elif ed1 == 'км' and ed2 =='м':
        print(a*1000)
    elif ed1 == 'км' and ed2 =='см':
        print(a*100000)
    elif ed1 == 'км' and ed2 =='мм':
        print(a*1000000)
    elif ed1 == 'км' and ed2 =='yd':
        print(a* 1000*1.09361)
    elif ed1 == 'км' and ed2 =='mi':
        print(a*1000*0.00062136931818182)
    elif ed1 == 'см' and ed2 == 'км':
        print(a/100000)
    elif ed1 == 'см' and ed2 == 'м':
        print(a/100)
    elif ed1 == 'см' and ed2 == 'мм':
        print(a*10)
    elif ed1 == 'см' and ed2 == 'yd':
        print(a/100 *1.09361)
    elif ed1 == 'см' and ed2 == 'mi':
        print(a/100*0.00062136931818182)
    elif ed1 == 'мм' and ed2 == 'км':
        print(a/1000000)
    elif ed1 == 'мм' and ed2 == 'м':
        print(a/1000)
    elif ed1 == 'мм' and ed2 == 'см':
        print(a/10)
    elif ed1 == 'мм' and ed2 == 'yd':
        print(a/1000*1.09361)
    elif ed1 == 'мм' and ed2 == 'mi':
        print(a/1000*0.00062136931818182)
    elif ed1 == 'yd' and ed2 == 'км':
        print(a*0.0009144)
    elif ed1 == 'yd' and ed2 == 'м':
        print(a*0.9144)
    elif ed1 == 'yd' and ed2 == 'см':
        print(a*91.44)
    elif ed1 == 'yd' and ed2 == 'мм':
        print(a*914,4)
    elif ed1 == 'yd' and ed2 == 'mi':
        print(a*0.000568182)
    elif ed1 == 'mi' and ed2 == 'км':
        print(a*1.60934451499)
    elif ed1 == 'mi' and ed2 == 'м':
        print(a*1609.34)
    elif ed1 == 'mi' and ed2 == 'см':
        print(a*160934)
    elif ed1 == 'mi' and ed2 == 'мм':
        print(a*1609340)
    elif ed1 == ed2:
        print(a)