from package.console_clear import clear

clear()

"""
Generators: range() ist zum Beispiel eine Generator Funktion. 
Die das Keyword yield benutzt. Yield unterbricht die for Schleife 
innerhalb der Funktion und wartet auf einen erneuten Aufruf der Funktion.
Somit werden die Werte der Range schrittweise abgearbeitet.
"""

""" 
range übergibt innerhalb des Schleifenkopfes einen Wert an
und wartet auf den erneuten Aufruf
for i in range(0, 10) bis ein StopIteration auftritt. 
Generator besitzen bessere Performance und benötigen weniger Speicherplatz. 
--> loop durch eine range viel schneller als durch eine liste !!!!
"""

# range liefert von 0 bis 9, damit wird eine Liste generiert.
my_list = list(range(10))
print(my_list)
my_list.clear()


# die Range Funktion von oben als eigene implementiert


def generator_func(num):
    for i in range(num):
        yield i


# Diese kann wie range verwendet werden
for i in generator_func(10):
    my_list.append(i)

print(my_list)

my_list.clear()

# Range als Objekt
gen = generator_func(10)

# Schrittweise Aufruf mit next()
print(next(gen))
print(next(gen))
print(next(gen))

# Der Generator merkt seinen Zustand 3 Aufrufe --> 0, 1, 2
# Die Liste wird nun von 3 bis 9 befüllt.
for i in gen.__iter__():
    my_list.append(i)

print(my_list)


# Unterschied loop und generator:
# how does loop work:


def special_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_loop(my_list)


# how does a generator work:


class MyGenerator():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.last:
            cur_num = MyGenerator.current
            MyGenerator.current += 1
            return cur_num
        else:
            MyGenerator.current = 0
            raise StopIteration


# Using the Generator
my_gen = MyGenerator(0, 10)
for i in my_gen:
    print(i)

# New Generator
new_gen = MyGenerator(0, 3)
num = new_gen.__next__()
print(num)

# Practice: Fibonacci numbers
clear()


def fibo(numbers):
    a = 0
    b = 1
    for i in range(numbers):
        yield a
        temp = a
        a = b
        b = temp + b


for i in fibo(21):
    print(i)

c = 'hello'[0]
print(c)
