"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    main()
user_age = int(input('Введите свой возраст: '))
if user_age < 3:
    print("Ты ещё слишком мал для садика!")
elif 3 <= user_age < 7:
    print('Твоё место в детском сад!')
elif 7 <= user_age < 18:
    print('Ты в школе!')
elif 18 <= user_age < 24:
    print('Ты в ВУЗе!')
elif 24 <= user_age < 56:
    print('Пора работать!')
elif 56 <= user_age <= 100:
    print('Наконец-то заслуженный отдых!')
else:
    print('Ты бессметен!')