"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
for _ in range(3):
    line1 = str(input('Введите строку 1: ').split(' '))
    line2 = str(input('Введите строку 2: ').split(' '))
    if (type(line1)==str) and (type(line2)==str):
        print('Это строка')
    else:
        print(0)
    if len(line1)==len(line2):
        print(1)
    else:
        print(0)
    if len(line1) > len(line2):
        print(2)
    if len(line1) != len(line2) and line2 == ('learn'):
        print(3)
    else:
        print(0)
