from time import time
from package.console_clear import clear

clear()

""" 
Decorator: Sind eine Art von Wrap Methoden, welche die übergebene Funktion einschließen
und diese ebenfalls erweitern können. Somit ist eine Erweiterung vor und nach dem 
Funktionsaufruf möglich
"""


def decorator_hello(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')

    return wrap_func


@decorator_hello
def hello():
    print('hello')


hello()


# Funktonessaufbau des Decorator --> my_decorator(hello)()
# --------------------------------------------------------


# Decorator Pattern
def decorator_bye(func):
    def wrap_func(*args, **kwargs):
        print('\n*********')
        func(*args, **kwargs)
        print('*********')

    return wrap_func


@decorator_bye
def bye(say_bye, emoji=':('):
    print(say_bye, emoji)


bye('bye')
print('\n')


# --------------------------------------------------------

# Practice: Function Time Performance

def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args)
        finished_time = time()
        sec = (finished_time - start_time)
        print(f'The function took {sec} s.')

    return wrapper


@performance
def performance_test_function(range_end):
    for number in range(0, range_end):
        number ** 2


performance_test_function(9999990)
