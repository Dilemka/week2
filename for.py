"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
classes = [
    {'school_class': '1a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '2a', 'scores': [5, 5, 4, 4, 3]},
    {'school_class': '3a', 'scores': [3, 4, 3, 5, 5]},
    {'school_class': '4a', 'scores': [5, 4, 2, 5, 3]},
]

sum_scores_school = sum(classes[0]['scores']) + sum(classes[1]['scores']) + sum(classes[2]['scores'])
sum_len_scores_school = len(classes[0]['scores']) + len(classes[1]['scores']) + len(classes[2]['scores'])

sum_scores_class1 = sum(classes[0]['scores'])
sum_scores_class2 = sum(classes[1]['scores'])
sum_scores_class3 = sum(classes[2]['scores'])

sum_len_scores_class1 = len(classes[0]['scores'])
sum_len_scores_class2 = len(classes[1]['scores'])
sum_len_scores_class3 = len(classes[2]['scores'])

print(f'Средний балл по школе: {int(sum_scores_school/sum_len_scores_school)}')
print(f'Средний балл по 1"a" классу: {int(sum_scores_class1/sum_len_scores_class1)}')
print(f'Средний балл по 2"a" классу: {int(sum_scores_class2/sum_len_scores_class2)}')
print(f'Средний балл по 3"a" классу: {int(sum_scores_class3/sum_len_scores_class3)}')