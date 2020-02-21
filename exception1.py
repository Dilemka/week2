"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
      user_answ = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'Как настроение?': 'Замахался', 'Как погода?': 'Посмотри в окно'}
      
      try:
          ask_user = input('')
      except KeyboardInterrupt:
          print('Пока')
          break
      if ask_user == 'Как дела?':
          print(user_answ['Как дела?'])
          break
      elif ask_user == 'Что делаешь?':
          print(user_answ['Что делаешь?'])
      elif ask_user == 'Как настроение?':
          print(user_answ['Как настроение?'])
      elif ask_user == 'Как погода?':
          print(user_answ['Как погода?'])
      else:
          print('Спроси что попроще')

    
if __name__ == "__main__":
    ask_user()
