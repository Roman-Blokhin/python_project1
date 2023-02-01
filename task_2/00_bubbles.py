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

point_1 = sd.get_point(220,240)
def booble (point, step):
    radius_1 = 30
    for _ in range (3):
        radius_1 += step
        sd.circle(center_position=point, color=sd.COLOR_WHITE, radius=radius_1, width=3)

booble(point=point_1, step=5)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


