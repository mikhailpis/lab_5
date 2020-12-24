#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу, выдающую индексы заданного элемента или сообщающую, что такого элемента в списке нет.

import sys

if __name__ == '__main__':
    A = list(map(int, input("Введите список ").split()))
    numb = int(input("Введите число, котрое нужно найти в списке "))

    if not numb in A:
        print("В списке нет искомого элемента", file=sys.stderr)
        exit(1)

    for i, item in enumerate(A):
        if item == numb:
            print("Индекс искомого элемента: ", i)
