from package.console_clear import clear

clear()

"""
Child class ist von der ParentClass abgeleitet, deswegen kann die
display Methode von dieser aufgerufen werden.
"""


class ParentClass:

    @staticmethod
    def display():
        print('Message from Superclass')


class ChildClass(ParentClass):
    pass


child_class = ChildClass()
child_class.display()

print('\n')

"""
Bei diesem Beispiel ruft die Child class engine, die Methode von der Parent class
auf und übergibt die Eigenschaften des Autos.
"""


class PKW:

    def engine(self, brand, ps):
        print(f'The {brand} has {ps} PS')


class BMW(PKW):
    brand = 'BMW'
    ps = 243

    def engine(self, **kwargs):
        super(BMW, self).engine(BMW.brand, BMW.ps)


my_car = BMW()
my_car.engine()
