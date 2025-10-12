from package.console_clear import clear

clear()

"""
 File I/O: Input/Output
"""
file_r_path = './files/example.txt'
file_w_path = './files/output.txt'

output_string = 'Hello, my name is dojo !'

# Vorgehensweise:

# my_file = open(file_path)
# print(my_file.readlines())
# my_file.close()

# Standard in Python: there is no close needed !
# mode: r readonly mode, r+ also writes but at the beginning of the file
with open(file_r_path, mode='r') as my_r_file:
    print(my_r_file.readlines())

# mode: w --> creates or overwrites the existing file
with open(file_w_path, mode='w') as my_w_file:
    my_w_file.write(output_string)

# mode: a --> append at the end of the file
with open(file_w_path, mode='a') as my_w_file:
    my_w_file.writelines('\n')
    my_w_file.write('How are you ?')

# Error Handling:
# try:
#     with open('foo.tx', mode='r') as my_file:
#         print(my_file.readlines())
# except FileNotFoundError as err:
#     print('File does not exists!')
#     raise err
# except IOError as err:
#     print('IO Error!')
#     raise err


# Practice: Translator

# with open(file_r_path, mode='r') as my_r_file:
#     print(my_r_file.readlines())
    #
