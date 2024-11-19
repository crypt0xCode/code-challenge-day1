'''
Пишу в максимально упрощенном стиле,
дабы остальные участники сообщества могли опираться на этот код
для самостоятельного анализа и понимания его функционала.
'''
from unicodedata import digit

#region Lesson 1.
'''
1) Пользователь вводит число a и число b. Возвести а в степень b
2) Пользователь вводит число от 1 до 7. Вывести соответствующий день недели
3) Пользователь вводит 2 числа. Вывести наибольшее из них
4) Пользователь вводит свой депозит и хороший курс доллара. Вывести в консоль депо в рублях и заплакать 
'''
def start_lesson_one():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(f'a ^ b equals {a**b}')

    day = int(input('Enter day of week (1-7): '))
    if (day == 1):
        print('Today is monday.')
    elif (day == 2):
        print('Today is tuesday.')
    elif (day == 3):
        print('Today is wednesday.')
    elif (day == 4):
        print('Today is thursday.')
    elif (day == 5):
        print('Today is friday.')
    elif (day == 6):
        print('Today is saturday.')
    elif (day == 7):
        print('Today is sunday.')
    else:
        print('Unknown day! =(')

    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    if (num1 > num2):
        print(f'{num1} is greater than {num2}')
    else:
        print(f'{num2} is greater than {num1}')

    deposit = int(input('Enter your depisote in RUB: '))
    dollar_exchange = int(input('Enter dollar exchange rage in USD: '))
    print(f'Today your deposit is ${deposit / dollar_exchange}')
#endregion

#region Lesson 2.
'''
1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"
2) Пользователь вводит 3 числа. Вывести наименьшее из них
3) Из нарнийского чата Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
    но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
    Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите “Это нормально”.
    Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
    Получаемое число A всегда меньше либо равно B (то есть это проверять не надо).
'''
def start_lesson_two():
    num = int(input('Enter num: '))
    if (num % 2 == 0):
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    num3 = int(input('Enter num3: '))
    if (num1 < num2 and num1 < num3):
        print(f'{num1} is the least.')
    elif (num2 < num1 and num2 < num3):
        print(f'{num2} is the least.')
    else:
        print(f'{num3} is the least.')

    sleep_A = int(input('Enter min normal count of sleep hours: '))
    sleep_B = int(input('Enter max normal count of sleep hours: '))
    sleep_H = int(input('Enter Ann count of sleep hours: '))
    if (sleep_A <= sleep_H <= sleep_B):
        print(f'{sleep_H} is a normal count of sleep hours.')
    elif (sleep_H < sleep_A):
        print(f'{sleep_H} is a lack of sleep.')
    else:
        print(f'{sleep_H} is a oversleep.')
#endregion

#region Lesson 3.
'''
1) Написать простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введенным числам (“первое число” “операция” “второе число”) и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где:
mod - это взятие остатка от деления,
pow - возведение в степень,
div - целочисленное деление.
2) даны 2 числа a и b. Определить, делится ли a на b нацело. Делится ли b на a?
3) дано трёхзначное число. Определить, есть ли среди его цифр одинаковые
'''
def start_lesson_three():
    num1 = float(input('Enter num1: '))
    num2 = float(input('Enter num2: '))
    print('1. +\n'
          '2. -\n'
          '3. /\n'
          '4. *\n'
          '5. mod\n'
          '6. pow\n'
          '7. div\n')
    op = int(input('Enter operation:'))
    match op:   # аналог switch() { case: } в Си-подобных языках
        case 1:
            print(f'{num1} + {num2} = {num1 + num2}')
        case 2:
            print(f'{num1} - {num2} = {num1 - num2}')
        case 3:
            print(f'{num1} / {num2} = {num1 / num2}')
        case 4:
            print(f'{num1} * {num2} = {num1 * num2}')
        case 5:
            print(f'{num1} mod {num2} = {num1 % num2}')
        case 6:
            print(f'{num1} pow {num2} = {num1 ** num2}')
        case 7:
            print(f'{num1} div {num2} = {num1 // num2}')

    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    if (a // b >= 1):
        print(f'{a} div {b} = {a // b} normally.')
    elif (b // a >= 1):
        print(f'{b} div {a} {b // a} normally.')
    else:
        print(f'{a} not div {b} or {b} not div {a} normally.')

    num = int(input('Enter a number from 100 to 999: '))
    hndrd = num // 100
    dzn = (num // 10) % 10
    dgts = num % 10
    print(f'Current digits are {hndrd} {dzn} {dgts}.')
    if (hndrd == dzn and hndrd == dgts):
        print('All digits are equals!')
    elif(
        (hndrd == dzn or hndrd == dgts)
        or (dzn == hndrd or dzn == dgts)
        or (dgts == hndrd or dgts == dzn)
    ):
        print('Two digits are equals.')
    else:
        print('There is no equals digits. =(')
    pass
#endregion


def main():
    # Uncomment to starting functions.
    # start_lesson_one()
    # start_lesson_two()
    start_lesson_three()


if __name__ == '__main__':
    main()