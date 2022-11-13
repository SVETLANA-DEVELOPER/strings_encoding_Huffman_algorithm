"""
Задача:
Реалиовать кодирование строки по алгоритму Хаффмана через ООП.
Использовала модуль collections.
Алгоритм работает.
"""


# Алгоритм Хаффмана
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def get_tree(string: str):
    # Считаем, сколько раз в строке встречается каждый символ с помощью Counter
    count_string = Counter(string)
    # Преобразуем словарь в список кортежей, сортируем по значеню словаря (2-го знач. корт.) и записываем в дек
    sorted_string = deque(sorted(count_string.items(), key=lambda item: item[1]))
    # Если в деке содержится больше одного кортежа, то суммируем первые два кортежа с наименьшими значениями.
    # Получаем вес узла-родителя
    while len(sorted_string) > 1:
        weight = sorted_string[0][1] + sorted_string[1][1]
        # Удаляем узлы-потомки (первые два кортежа). И создаем правую и левую части дерева (остаточный дек)
        node = Node(left=sorted_string.popleft()[0], right=sorted_string.popleft()[0])
        # Перебираем отсортированный дек. Если вес родительского узла больше, чем значение кортежа, то пропускаем его
        for i, item in enumerate(sorted_string):
            if weight > item[1]:
                continue
            # Если же вес род. узла меньше, чем вес узла (знач. кортежа),
            # то вставляем значение узла в дек и прерываем цикл
            else:
                sorted_string.insert(i, (node, weight))
                print(f'1{sorted_string}')
                break
        # Оператор else срабатывает, если цикл не был прерван break
        else:
            sorted_string.append((node, weight))
            print(f'2{sorted_string}')
    # Возвращаем единственный оставшийся кортеж - это будет корень дерева Хаффмана
    return sorted_string[0][0]


# Создаем таблицу кодов, она будет храниться в словаре
code_table = dict()


def coding(tree, path=''):
    # Смотрим, принадлежат ли левая и правая части классу Node (то есть является ли узлом)
    # Если является узлом, то присваиваем 0 или 1
    if not isinstance(tree, Node):
        code_table[tree] = path
        print(f'1 {code_table}')
    # Присваиваем левой части 0, а правой 1
    else:
        coding(tree.left, path=f'{path}0')
        coding(tree.right, path=f'{path}1')
        print(f'2 {code_table}')


my_string = "beep boop beer!"

coding(get_tree(my_string))

for i in my_string:

    print(code_table[i], end=' ')

print()
