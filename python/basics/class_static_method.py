from package.console_clear import clear
clear()

"""
a, method: (self)
-----------------

- can modify objects instance state
  Kann die Instanz des Objekts ändern --> self

- can modify class state
  Kann ebenfalls die erzeugte Klasse ändern.

b, classmethod: (cls)
---------------------

- can't modify object instance state
  Kann nicht die Instanz des Objekts selbst ändern --> nur cls

- can modify object class state
  Kann aber mit cls die Klasse des Objekts ändern.

c, staticmethod: 
----------------

- can't modify object instance state
- can't modify object class state
  Kann weder die Instanz noch die Klasse des Objekts ändern.
"""

# region Customer


class Customer:

    def __init__(self, name, customer_id, age, gender, registered):
        self.name = name
        self.customer_id = customer_id
        self.age = age
        self.gender = gender
        self.registered = registered

    @classmethod
    def from_string(cls, customer_values_str):
        name, id, age, gender, registered = customer_values_str.split(',')
        is_registered = bool(registered)
        return cls(name, int(id), int(age), gender, is_registered)

    def is_registered(self):
        return self.registered

    def get_gender(self, id):
        if id == self.customer_id:
            return self.gender
        else:
            return None

    @staticmethod
    def create_greetings(gender, name):
        greeting_template = 'Hallo {0} {1}, Welcome back!'
        if gender == 'm':
            greeting_message = str.format(greeting_template, 'Mister', name)
        else:
            greeting_message = str.format(greeting_template, 'Miss', name)

        return greeting_message

    @staticmethod
    def print_warning(name):
        warning_template = 'ist leider nicht registiert !' + '\n'
        print(name + ' ' + warning_template)


# endregion
# region Customers


class Customers:
    customers_list = []

    def __init__(self, customer_list):
        self.customers_list = customer_list

    @classmethod
    def create_customers(cls):
        return cls(cls.customers_list)

    def add_costumer(self, costumer):
        # Call a private method
        if(costumer.is_registered()):
            self.customers_list.append(costumer)
        else:
            Customer.print_warning(costumer.name)

    def greeting_all(self):
        for customer in self.customers_list:
            id = customer.customer_id
            text = Customer.create_greetings(
                customer.get_gender(id), customer.name)
            print(text + '\n')


# endregion


my_customers = Customers.create_customers()
my_customers.add_costumer(Customer.from_string(
    'Hans Meier,12002,25,m,true'))
my_customers.add_costumer(Customer.from_string(
    'Beate Jansen,12001,45,f,'))
my_customers.greeting_all()
