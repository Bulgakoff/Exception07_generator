



try:
    number = int(input('Введите : '))
    result = 100 / number

except ZeroDivisionError as e:
    print('Деление на ноль 0')
    print('инфа о исключении в ', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('инфа о исключении в ', e)


