#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# В списке, состоящем из целых элементов, вычислить:
# 1) Индекс максимального элемента списка;
# 2) произведение элементов списка, расположенных между первым и вторым нулевыми элементами.
# Преобразовать список таким образом, чтобы в первой его половине располагались элементы,
# стоявшие в четных позициях, а во второй половине - элементы, стоявшие в нечетных позициях.

import sys

if __name__ == '__main__':
    A = list(map(int, input('Введите список ').split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

# Задание 1
    A_max = A[0]
    i_max = 0
    for i, item in enumerate(A):
        if item >= A_max:
            i_max, A_max = i, item
    print('Индекс максимального элемента: ', i_max)

# Задание 2
    arrays = []
    for i, item in enumerate(A):
        if item == 0:
            arrays.append(i)

    x = arrays[0] + 1
    y = arrays[1]
    m = 1

    for item in A[x:y]:
        m *= item
    print("Произведение элементов списка, расположенных между первым и вторым нулевыми элементами равно: ", m)

    # Количество вставленных элементов
    k = 0
    for key, value in enumerate(A):
        if key % 2 != 0:
            A.insert(k, A.pop(key))
            k += 1
            print(A)
