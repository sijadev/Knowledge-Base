from package.console_clear import clear
clear()

""" 
Verständnis (commprehension) for list, set and dictionary
"""

# 1.0 Schnelles Erstellen und befüllen mit einem Ausdruck (expression) und möglicher Bedingung

# Gleich zu stellen, als würde über man über die range mit "for" iterieren
# Syntax: expression(was soll mit jedem wert passieren)  "for"  variable "in" Wertbereich (Iterierbar)  Bedingung


# List
my_num_list = [num for num in range(1, 11)]
print(my_num_list)
print('\n')

my_str_list = [char for char in 'hello']
print(my_str_list)
print('\n')

# Jeder Wert in der Range soll mit der Potenz hoch 2 berechnet werden.
my_num_ext_list = [num**2 for num in range(1, 11)]
print(my_num_ext_list)
print('\n')

# Mit einer Bedingung, dass nur gerade Zahlen übernommen werden!
my_num_even_list = [num**2 for num in range(1, 11) if num % 2 == 0]
print(my_num_even_list)
print('\n')

# -----------------------------------------------------------------

# Set
my_num_set = {num for num in range(0, 10)}
print(my_num_set)
print('\n')

# Analog wie bei einer Liste nur ist zu beachten das die Reihenfolge nicht sortiert ist!
my_num_ext_set = {num**2 for num in range(1, 11)}
print(my_num_ext_set)
print('\n')

# -----------------------------------------------------------------

# Dictionary
# Syntax: expression(was soll mit jedem wert passieren)
# "for"  key, value "in" Dictionary (Iterierbar) + mögliche Bedingung

my_base_dic = {
    'a': 1,
    'b': 2
}

# k:v legt den Key und Value und dessen Wert fest
# k, v was soll verwendet werden
# if die Bedingung, was soll verwendet werden
my_dic = {k: v**2 for k, v in my_base_dic.items()}
print(my_dic)
print('\n')

my_even_dic = {k: v**2 for k, v in my_base_dic.items() if v % 2 == 0}
print(my_even_dic)
print('\n')

# num:num**2 "for" num "in" Range + mögliche Bedingung

my_from_range_dic = {num: num**2 for num in range(0, 11) if num % 2 != 0}
print(my_from_range_dic)
print('\n')


# Practice:
# Erstelle eine neue Liste nur mit den doppelten Buchstaben aus der Liste
base_list = ['a', 'b', 'c', 'd', 'b', 'n', 'n']

# Die urprüngliche Liste wird zu einem Set konvertiert, weil jeder Wert nur einmal eingefügt wird. 
# Das Ergebnis wäre sonst jeweils mit 2 Einträgen
# Set --> List
duplicates_list = list(
    set([char for char in base_list if base_list.count(char) > 1]))
duplicates_list.sort()
print(duplicates_list)
