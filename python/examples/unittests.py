import unittest
from random_guessing_game import convert_to_int, check_numbers


class MyTestCase(unittest.TestCase):
    def test_convert_to_int_two(self):
        result = convert_to_int("1", "10")
        my_num_list = [1, 10]
        self.assertEqual(result, my_num_list)

    def test_convert_to_int_one(self):
        result = convert_to_int("10")
        my_num = 10
        self.assertEqual(result, my_num)

    def test_check_numbers(self):
        guess_num = 5
        correct_num = 5
        result = check_numbers(guess_num, correct_num)
        self.assertTrue(result)

    def test_check_numbers_wrong(self):
        guess_num = 4
        correct_num = 5
        result = check_numbers(guess_num, correct_num)
        self.assertFalse(result)

    def test_check_numbers_None(self):
        result = check_numbers(None, None)
        self.assertFalse(result)

    def test_check_numbers_empty(self):
        result = check_numbers("", "")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
