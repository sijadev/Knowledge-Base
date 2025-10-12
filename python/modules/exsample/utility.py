""" 
Module which offers different useful functions
"""


def addition(num1=0, num2=0):
    if num1 and num2 is not None:
        if isinstance(num1, int) and isinstance(num2, int):
            return int(num1) + int(num2)
        else:
            return 'Please enter numbers !'
    else:
        return 'Please enter numbers !'
