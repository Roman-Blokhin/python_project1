#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

my_family.append ('Мама')
my_family.append ('Папа')
my_family.append ('Сеня')

print (my_family)

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    [my_family [0], '162'],
    [my_family [1], '173'],
    [my_family [2], '175'],
    # ['имя', рост],
]

print (my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print ('Рост отца - ', my_family_height [1][1])

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print ('Общий рост моей семьи - ', int (my_family_height [0][1]) + int (my_family_height [1][1]) +
       int (my_family_height [2][1]), 'см')
