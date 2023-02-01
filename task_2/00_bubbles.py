# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей +
point = sd.get_point(120,140)
radius = 20
for _ in range (3):
    radius += 5
    sd.circle(center_position=point, color=sd.COLOR_BLACK,radius=radius, width=2)

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


