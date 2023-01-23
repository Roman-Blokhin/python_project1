#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict ()

moscow = sites ['Moscow']
london = sites ['London']
moscow_london = ((moscow [0] - london [0]) ** 2 + (moscow [1] - london [1]) ** 2) ** 5.
dict.append (moscow_london)
print (dict)

# TODO здесь заполнение словаря

print(distances)




