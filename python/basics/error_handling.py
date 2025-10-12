from package.console_clear import clear
clear()

"""
 Error Handling in Python: try -- expect
"""

text_math = 'Das Ergebnis lautet {0}'
text_age = 'Sie sind {0} Jahre'

def error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            print('Es sind nur Zahlen erlaubt!')
            print('\n')
        except ZeroDivisionError:
            print('Null ist eine ungültige Eingabe!')
        except ValueError:
            print('Der Wert ist nicht korrekt!')
    return wrapper


@error_handling
def divison(a, b):
    c = a / b
    return c

@error_handling
def convert_to_int(age):
    int_age = int(age)
    return int_age

def output(value, text):
    if(value != None):
        print(text.format(value))

c = divison(2, 0)
output(c, text_math)
d = divison(4, 2)
output(d, text_math)
f = divison('a', 4)


#age = input('Geben Sie bitte Ihr Alter in Jahren an: ')
#int_age = convert_to_int(age)
#output(int_age, text_age)


def summ(a, b):
    try:
        return a + b
    except TypeError as err:
        print(f'Ein Fehler ist aufgetretten: {err}')
        print('\n')

summ('a', 2)

def error_appeared(message):
    raise Exception(message)

error_appeared('Die Eingabe ist nicht korrekt!')