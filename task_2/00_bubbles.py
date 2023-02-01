# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей +
point = sd.get_point(120,140)
radius = 20
for _ in range (3):
    radius += 5
    sd.circle(center_position=point, color=sd.COLOR_BLACK,radius=radius, width=2)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

point_1 = sd.get_point(220,240)
def booble (point, step):
    radius_1 = 30
    for _ in range (3):
        radius_1 += step
        sd.circle(center_position=point, color=sd.COLOR_WHITE, radius=radius_1, width=3)

booble(point=point_1, step=5)

# Нарисовать 10 пузырьков в ряд

def booble (point, step):
    radius_2 = 15
    for _ in range (1):
        radius_2 += step
        sd.circle(center_position=point, color=sd.COLOR_GREEN, radius=radius_2, width=5)

for x in range (250, 701, 50):
    point_2 = sd.get_point(x, 140)
    booble(point=point_2, step=5)

# Нарисовать три ряда по 10 пузырьков

def booble (point, step):
    radius_3 = 25
    for _ in range (2):
        radius_3 += step
        sd.circle(center_position=point, color=sd.random_color(), radius=radius_3, width=3)

for y in range (200, 300, 45):
    for x in range (650, 931, 30):
        point_3 = sd.get_point(x, y)
        booble(point=point_3, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

def booble (point, step):
    radius_4 = 10
    for _ in range (1):
        radius_4 += step
        sd.circle(center_position=point, color=sd.random_color(), radius=radius_4, width=1)

for _ in range (100):
    point_4 = sd.random_point()
    step = random.randint (1, 40)
    booble(point=point_4, step=step)

sd.pause()


