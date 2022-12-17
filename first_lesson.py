import random
import datetime

def run():

    '''Выполняем первое задание'''
    my_list_1 = [2, 5, 8, 2, 12, 12, 4]
    my_list_2 = [2, 7, 12, 3]

    for i in my_list_2:
        while i in my_list_1:
            my_list_1.remove(i)

    print(my_list_1)

    '''Выполняем второе задание'''
    date = datetime.date(random.randint(datetime.MINYEAR,datetime.MAXYEAR),random.randint(1,12),1)
    date += datetime.timedelta(random.randint(1,31))
    monthes = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августв", "сентбря", "октября", "нобря", "декабря"]
    days = ['один','два','три','четыре','пять','шесть','семь','восемь','девять','десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать'
            'шестнадцать','семнадцать','восемнадцать','девятнадцать','двадцать','двадцать один','двадцать два','двадцать три','двадцать четыре'
            'двадцать пять','двадцать шесть','двадцать семь','двадцать восемь','двадцать девять','тридцать','тридцать один']
    date_reform = f'{days[date.day-1]} {monthes[date.month-1]} {date.year} года'
    print(date_reform)

    '''Выполняем третье задание'''
    first_list = []
    for i in range(1, random.randint(2,40)):
        first_list.append(random.randint(1,15))
    result = list(set(first_list))
    """for i in first_list:
        if i not in result:
            result.append(i)"""

    print(f'Оригинальный список\n{first_list}\n\nПосле удаления дубликатов\n{result}')