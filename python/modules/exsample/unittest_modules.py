import unittest
import utility


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('Step up function before each test!')

    def test_nothing_addition(self):
        result = utility.addition()
        self.assertEqual(result, 'Please enter numbers !')

    def test_num_addition(self):
        test_param_1 = 4
        test_param_2 = 5
        result = utility.addition(test_param_1, test_param_2)
        self.assertEqual(result, 9)
        self.assertIsNot(result, 'Please enter numbers !')

    def test_string_addition(self):
        test_param_1 = 'ert'
        test_param_2 = 5
        result = utility.addition(test_param_1, test_param_2)
        self.assertEqual(result, 'Please enter numbers !')

    def test_empty_string_addition(self):
        test_param_1 = 2
        test_param_2 = ''
        result = utility.addition(test_param_1, test_param_2)
        self.assertEqual(result, 'Please enter numbers !')

    def test_none_addition(self):
        test_param_1 = None
        test_param_2 = None
        result = utility.addition(test_param_1, test_param_2)
        self.assertEqual(result, 'Please enter numbers !')

    def test_none_addition_2(self):
        test_param_1 = 3
        test_param_2 = None
        result = utility.addition(test_param_1, test_param_2)
        self.assertEqual(result, 'Please enter numbers !')

    def tearDown(self):
        print('Tear down after each test!')


if __name__ == '__main__':
    unittest.main()
