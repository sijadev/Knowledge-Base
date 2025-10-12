from functools import reduce
from package.console_clear import clear
clear()


"""
Pure Functional bedeutet, dass die Funktion im Scope (Anweisungen) und die Daten von außerhalb getrennt werden.
Die Funktionen dürfen die Daten außerhalb nicht beeinflussen. 
"""
numbers_list = [1, 2, 3, 4]


def multiply_with2(numbers_list):
    # Es wird eine neue Liste mit den Ergebnissen erzeugt und dem Aufrufer zurückgegeben.
    my_list = []
    # Die übergebenen Daten werden zwar benutzt aber nicht geändert!!!
    for number in numbers_list:
        number *= 2
        my_list.append(number)
    return my_list


print(multiply_with2(numbers_list))
print(numbers_list)
print('\n')

# 1.0 Map
# -------
# Die Function wird von der map aufgerufen


def multiply_with_itself(item):
    return item * item

# Dem Objeckt map wird die aufzurufende Funtkion und die zubenutzende Daten übergeben.
# Map ruft selbstständig die Funktion mit jedem Wert auf
# Danach wird das map Objekt in eine Liste konventiert und kann damit ausgegeben werden.


cur_list = list(map(multiply_with_itself, numbers_list))

print(cur_list)
print(numbers_list)
print('\n')

# 2.0 Filter
# -------
# Die Funktionen werden von filter aufgerufen


def only_odd(item):
    return item % 2 != 0


def only_even(item):
    return item % 2 == 0


odd_numbers = list(filter(only_odd, numbers_list))
even_numbers = list(filter(only_even, numbers_list))

print(odd_numbers)
print(even_numbers)
print(numbers_list)
print('\n')

# 3.0 Zip
# -------
# Generiert aus den übergebenen Objekten eine neue Struktur, bei der die Reihenfolge der einzelnen Werten beachtet wird
# Die jeweiligen Werte werden in einem Tulp Objekt zusammengefasst!

name_list = ['Meier', 'Mueller', 'Schmidt']
id_list = [123, 456, 789]
registered = [True, True, False]

customer_list = list(zip(name_list, id_list, registered))

for customer in customer_list:
    cur_list = list(customer)
    print(cur_list)

print(customer_list)
print('\n')


# 4.0 Reduce
# -------
# Mit Reduce kann man z.B. aus den einzelnen Werte einer Liste aufaddieren und es so auf einen Wert reduzieren
# Needs the 'from functools import reduce' import
# acc ist Inizial 0 danach der letzte Wert aus der vorherigen Berechnung: 1, 3, 6
def accumulator(acc, item):
    return acc + item


my_value = reduce(accumulator, numbers_list, 0)
print(my_value)
print('\n')

# 5.0 Lambda
# -------
# Lambda bezeichnet man anonyme einmalige benutzbare Funktionen, die nach Ihren Aufruf "vergessen" werden.
# lambda item: aktion

# multiply_with_itself als lambda
cur_list = list(map(lambda item: item*item, numbers_list))
print(cur_list)
print('\n')

# accumulator as lambda
cur_list = reduce(lambda acc, item: acc + item, numbers_list, 0)
print(cur_list)
print('\n')

# string expression
text = 'Hallo, {0}! Nice to see you again.'
name_list = ['Bender', 'Mayer']

welcome_list = list(map(lambda name: str.format(text, name), name_list))
print(welcome_list)
print('\n')

# 6.0 Practice:
# Sort following list of tulps with lambda
tulp_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

tulp_list.sort(key=lambda item: item[1])
print(tulp_list)
print('\n')

# my_string_list = ['Hello User', 'My name is x']
# lines = map(lambda line: print(line), my_string_list)
# lines.__next__()
# lines.__next__()
