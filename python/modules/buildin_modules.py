from random import random, shuffle

# print out the documentation of the module random
# help(random)

# print all available methods of the random object
print(dir(random))

my_list = list(range(1, 11))
print(my_list)

# 1.0 random.random() picks a number between 0 and 1
# auf zwei Nachstellen formatiert
num = format(random(), '.2f')
print(num)

# 2.0 random.shuffle() werden die Werte zufällig angeordnet
shuffle(my_list)
print(my_list)
