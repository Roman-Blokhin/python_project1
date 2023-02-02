# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# ДОПОЛНИЛ ЗАДАНИЕ СЛОВАРЯМИ, ЧТОБЫ ИНТЕРЕСНЕЙ БЫЛО + ПРАКТИКА. ПИШУ 2 ВАРИАНТА

# ВАРИАНТ №1:

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

month_year = {
    'Январь': '1',
    'Февраль': '2',
    'Март': '3',
    'Апрель': '4',
    'Май': '5',
    'Июнь': '6',
    'Июль': '7',
    'Август': '8',
    'Сентябрь': '9',
    'Октябрь': '10',
    'Ноябрь': '11',
    'Декабрь': '12',
}
month_dict = {
    '1': [
        {'Месяц': 'Январь', 'Дней': 31},
    ],
    '2': [
        {'Месяц': 'Февраль', 'Дней': 28}
    ],
    '3': [
        {'Месяц': 'Март', 'Дней': 31}
    ],
    '4': [
        {'Месяц': 'Апрель', 'Дней': 30}
    ],
    '5': [
        {'Месяц': 'Май', 'Дней': 31}
    ],
    '6': [
        {'Месяц': 'Июнь', 'Дней': 30}
    ],
    '7': [
        {'Месяц': 'Июль', 'Дней': 31}
    ],
    '8': [
        {'Месяц': 'Август', 'Дней': 31}
    ],
    '9': [
        {'Месяц': 'Сентябрь', 'Дней': 30}
    ],
    '10': [
        {'Месяц': 'Октябрь', 'Дней': 31}
    ],
    '11': [
        {'Месяц': 'Ноябрь', 'Дней': 30}
    ],
    '12': [
        {'Месяц': 'Декабрь', 'Дней': 31}
    ]
}

print('Вы ввели:', month)

if user_input == '1':
    print('Выбранный вами месяц:', month_dict[month_year['Январь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Январь']][0]['Дней']) + '.')

elif user_input == '2':
    print('Выбранный вами месяц:', month_dict[month_year['Февраль']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Февраль']][0]['Дней']) + '.')

elif user_input == '3':
    print('Выбранный вами месяц:', month_dict[month_year['Март']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Март']][0]['Дней']) + '.')

elif user_input == '4':
    print('Выбранный вами месяц:', month_dict[month_year['Апрель']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Апрель']][0]['Дней']) + '.')

elif user_input == '5':
    print('Выбранный вами месяц:', month_dict[month_year['Май']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Май']][0]['Дней']) + '.')

elif user_input == '6':
    print('Выбранный вами месяц:', month_dict[month_year['Июнь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Июнь']][0]['Дней']) + '.')

elif user_input == '7':
    print('Выбранный вами месяц:', month_dict[month_year['Июль']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Июль']][0]['Дней']) + '.')

elif user_input == '8':
    print('Выбранный вами месяц:', month_dict[month_year['Август']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Август']][0]['Дней']) + '.')

elif user_input == '9':
    print('Выбранный вами месяц:', month_dict[month_year['Сентябрь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Сентябрь']][0]['Дней']) + '.')

elif user_input == '10':
    print('Выбранный вами месяц:', month_dict[month_year['Октябрь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Октябрь']][0]['Дней']) + '.')

elif user_input == '11':
    print('Выбранный вами месяц:', month_dict[month_year['Ноябрь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Ноябрь']][0]['Дней']) + '.')

elif user_input == '12':
    print('Выбранный вами месяц:', month_dict[month_year['Декабрь']][0]['Месяц'] +
          ', в нем дней:', str(month_dict[month_year['Декабрь']][0]['Дней']) + '.')

else:
    print ('Эге-гей, нет такого месяца! Давай заново..')

print ('------------------------------------------')

# ВАРИАНТ №2:

user_input_2 = input("Введите, пожалуйста, номер месяца: ")
month_2 = int(user_input)

quantity_0 = '31'
quantity_1 = '30'
quantity_2 = '28'

if user_input_2 == '1':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

elif user_input_2 == '2':
    print ('Дней в', user_input_2, 'месяце:', quantity_2)

if user_input_2 == '3':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

elif user_input_2 == '4':
    print ('Дней в', user_input_2, 'месяце:', quantity_1)

if user_input_2 == '5':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

elif user_input_2 == '6':
    print ('Дней в', user_input_2, 'месяце:', quantity_1)

if user_input_2 == '7':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

elif user_input_2 == '8':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

if user_input_2 == '9':
    print ('Дней в', user_input_2, 'месяце:', quantity_1)

elif user_input_2 == '10':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

if user_input_2 == '11':
    print ('Дней в', user_input_2, 'месяце:', quantity_1)

elif user_input_2 == '12':
    print ('Дней в', user_input_2, 'месяце:', quantity_0)

else:
    print ('Эге-гей, нет такого месяца! Давай заново..')
