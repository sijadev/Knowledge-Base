import re
from package.console_clear import clear

clear()

"""
Regular Expressions:
"""
pattern_o = re.compile('o')
string = 'Hello everybody, my name is sija. I am 49 years old.'

name = re.search('sija', string)
letter_o = pattern_o.findall(string)

print(letter_o)

# Practice: Email Validation
email_pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
password_pattern = re.compile(r'[a-zA-Z0-9$%@#]{8,}\d')

password1 = 'qwe223%@9'
password2 = '3§ztgfd12'

check_password = password_pattern.fullmatch(password1)
print(check_password)

check_password = password_pattern.fullmatch(password2)
if check_password is None:
    print('Passwort ist nicht Regel konform!')
