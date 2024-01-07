#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
        TestMaxInteger class
    """

    def test_negative_num(self):
        """
            Checks if function will give the highest negative
            integer
        """
        self.assertEqual(max_integer([-12, -14, -16, -25]), -12)

    def test_positive_num(self):
        """
            Checks if function will give the highest positive
            integer
        """
        self.assertEqual(max_integer([12, 14, 16, 25]), 25)

    def test_positive_float(self):
        """
            Checks if function will give the highest positive
            float
        """
        self.assertEqual(max_integer([2.75, 3.25, 4.75, 5.25]), 5.25)

    def test_negative_float(self):
        """
            Checks if function can give the highest negative
            float
        """
        self.assertEqual(max_integer([-2.75, -3.25, -4.75, -5.25]), -2.75)

    def test_char(self):
        """
            Checks if function will give the highest string
        """
        self.assertEqual(max_integer(['d', 'D', 'k', 'K']), 'k')

    def test_strings(self):
        """
            Checks if function will give the highest string
        """
        self.assertEqual(max_integer(['adam', 'Abel', 'cain', 'Eve']), 'cain')
        self.assertEqual(max_integer('Zachariah'), 'r')

    def test_empty_string(self):
        """
            Checks if function will take empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_max_integer(self):
        """
        Test for the max_integer in the max_integer module
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_if_negative_num_in_list(self):
        """
        Test for the negative number in list function
        """

        self.assertEqual(max_integer([0, -3, -5]), 0)

    def test_if_all_negative_interger(self):
        """
        Test if all arguments are negative
        """

        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    def test_if_list_empty(self):
        """
        Test for if list is empty
        """

        self.assertIsNone(max_integer([]))

    def test_if_no_args(self):
        """
        Test for if no args passed
        """

        self.assertIsNone(max_integer())

    def test_if_none_is_arg(self):
        """
        Test for if none is provided
        """

        self.assertRaises(TypeError, max_integer, None)

    def test_if_a_diff_datatype_in_list(self):
        """
        Test for if a wrong datatype is passed
        """

        self.assertRaises(TypeError, max_integer, [1, 2, "MAX"])

    def test_if_negative_float_is_in_list(self):
        """
        Test for if float is provided
        """

        self.assertEqual(max_integer([-1.4, 1.4, 1.5]), 1.5)
    def test_if_list_of_1_element(self):
        """
        Test for list of one element
        """
        self.assertEqual(max_integer([1]), 1)

if __name__ == "__main__":
    unittest.main()
