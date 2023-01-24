#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними

distances = dict ()
distances_1 = dict ()

moscow = sites ['Moscow']
london = sites ['London']
paris = sites ['Paris']

# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow_london = ((moscow [0] - london [0]) ** 2 + (moscow [1] - london [1]) ** 2) ** .5
moscow_paris = ((moscow [0] - paris [0]) ** 2 + (moscow [1] - paris [1]) ** 2) ** .5
london_paris = ((london [0] - paris [0]) ** 2 + (london [1] - paris [1]) ** 2) ** .5

# здесь заполнение словаря

distances ['Moscow'] = {}
distances ['Moscow'] ['London'] = moscow_london
distances ['Moscow'] ['Paris'] = moscow_paris

distances_1 ['London'] = {}
distances_1 ['London'] ['Paris'] = london_paris

print(distances)
print(distances_1)




