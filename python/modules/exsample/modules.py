# package can be "shopping" with maybe a module "shopping_cart"
from package.console_clear import clear
import utility

clear()

"""
 Module: utility
"""
if __name__ == '__main__':
    number = utility.addition(1, 11)
    print(f'Das Ergebnis = {number}')
