
"""#Задание 2.
#Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование стро
"""

time = int(input('Введите время в секундах: '))
hours = time//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time % 3600)//60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours_res}:{minutes_res}:{seconds_res}')