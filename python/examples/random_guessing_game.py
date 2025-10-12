from random import randrange
from sys import argv


def convert_to_int(first_string, second_string=None):
    try:
        if second_string is None:
            return int(first_string)
        else:
            my_num_list = [int(first_string), int(second_string)]
            return my_num_list
    except ValueError:
        raise ValueError('Die Eingabe ist nicht korrekt!')


def check_numbers(guess_num, correct_num):
    if isinstance(guess_num, int) and isinstance(correct_num, int):
        if guess_num == correct_num:
            print('Gratulation Sie haben die richtige Zahl erraten :)')
        return True
    else:
        print('Falsche Zahl')
        return False


def play_game(correct_num):
    if isinstance(correct_num, int) and not None:
        while True:
            guess_string = input('Geben Sie eine Zahl ein: ')
            guess_number = convert_to_int(guess_string)
            if check_numbers(guess_number, correct_num):
                break
            else:
                continue
    else:
        return ValueError('Ungültiger Wert!')


if __name__ == '__main__':
    try:
        num_list = convert_to_int(argv[1], argv[2])
        random_num = randrange(num_list[0], num_list[1])
        play_game(random_num)
    except IndexError as err:
        print(f'{err.args} Geben Sie einen Zahlenbereich ein: z.B. für 1 10')
