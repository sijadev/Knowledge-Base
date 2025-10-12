from package.console_clear import clear
clear()

""" 
Lernziel: Funktionen (Ihr Pointer) können in Variablen übergeben werden
Diese können somit als Funktion aufgerufen werden.

Funktionen können als Parameter bei einer anderen Funktion verwendet werden.
Diese können innerhalb der Funktion aufgerufen werden.
"""
# Methode gibt nur ein Hello in der Konsole aus


def hello():
    print('hello')


# Die Funktion hello wird in einer neuen Variable gespeichert
# --> Der Pointer auf die hello Funktion wird kopiert !
greet = hello

# Die Funktion hello wird gelöscht
# --> Der Pointer auf die hello Funktion wird gelöscht
# Ein Aufruf der hello Funktion ist nicht mehr möglich
del hello

try:
    hello()
except NameError:
    print('Errror: hello method is not callable!')

# Aufruf der Greet Funktion
# Da der ursprüngliche Pointer, jetzt bei greet, existiert
# kann diese auch Aufgerufen werden.
finally:
    # Die Funktion wird aufgerufen und besitzt aber keinen
    # Rückgabewert --> None
    print(greet())
    print('\n')

# -------------------------------------------------------------

# Die erste Funktion bekommt die zweite als Parameter übergeben
# und ruft diese auf
# Diese Art wird als HOF (Higher Order Function) bezeichnet


def function_one(function):
    function()

# Die zweite Funktion sorgt nur für die Ausgabe in der Konsole


def function_two():
    print('Hey, hey')


# Bei der Zuweisung wird die Funktion aufgerufen und besitzt keinen
# Rückgabewert None
var_output = function_one(function_two)
# None
print(var_output)

"""
Anderes Beispiel für HOF:

def greet():
    def func():
        return 5
    return func()

Die Methode gibt eine andere Methode zurück, hier den Return von func
"""
