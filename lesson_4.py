import os, random

""" 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую 
    директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки. 
    Проверьте работу функций в этом же модуле."""

def mkdir():
    for i in range(1,10):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'dir{i}')
        os.mkdir(path)


def rmvder():
    for i in range(1,10):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'dir{i}')
        os.rmdir(path)

""" Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. 
    Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
"""
def get_random(list):
    if type(list).__name__ == 'list' and list !=[]:
        return random.choice(list)
    else:
        return None


def run():
    mkdir()
    print(os.listdir())
    rmvder()
    print(os.listdir())
    list = [random.randint(1,100) for _ in range(random.randint(0,20))]
    print(list)
    print(get_random(list))
    print(get_random('1234'))