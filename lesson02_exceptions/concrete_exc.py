


try:
    number = int(input('Введите : '))
    result = 100 / number
except ZeroDivisionError:
    print('Деление на ноль 0')
except ValueError:
    print(' invalid literal for int()')

