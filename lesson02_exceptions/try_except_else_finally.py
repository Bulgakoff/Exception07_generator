


try:#--> код которвый может вызвать  ИС
    number = int(input('Введите : '))
    result = 100 / number
except:#--->что делать еслми возникла ИС
    print('except ---> Деление на ноль 0')
else:
    print('else что делать если ошибок не было')
finally:
    print('finally выполняется всегда')

