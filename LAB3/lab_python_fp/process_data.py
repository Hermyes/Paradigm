import json
import random
import time
from contextlib import contextmanager
from field import field
from gen_random import gen_random
from unique import Unique, start
from print_result import print_result
from cm_timer import cm_timer_2



def main():

    path = r'C:\Users\user\Desktop\Study\PARADIGM LABS 3 SEM\LAB3\data_light.json'


    with open(path, encoding='utf-8') as f:
        data = json.load(f)



    @print_result
    def f1(arg):
        return sorted(list(set(map(lambda x: x['job-name'].lower(), arg))), key=str.lower)


    @print_result
    def f2(arg):
        return list(filter(lambda x: x.startswith('программист'), arg))


    @print_result
    def f3(arg):
        return list(map(lambda x: x + ', с опытом Python', arg))


    @print_result
    def f4(arg):
        return list(zip(arg, gen_random(len(arg), 100000, 200000)))
    with cm_timer_2():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()

    import json
    import sys

    # Сделаем другие необходимые импорты

    path = None

    # Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

    with open(path) as f:
        data = json.load(f)


    # Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
    # Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
    # В реализации функции f4 может быть до 3 строк

    @print_result
    def f1(arg):
        raise NotImplemented


    @print_result
    def f2(arg):
        raise NotImplemented


    @print_result
    def f3(arg):
        raise NotImplemented


    @print_result
    def f4(arg):
        raise NotImplemented


    if __name__ == '__main__':
        with cm_timer_1():
            f4(f3(f2(f1(data))))