import unittest
from homeworks import multiplication_table, sum, text, filter_strings

class TestHomeworkFunctions(unittest.TestCase):

# Unit tests for task 1
    def test_multiplication_table_positive(self):
        expected_output = "5x1=5\n5x2=10\n5x3=15\n5x4=20\n5x5=25\n"
        self.assertEqual(multiplication_table(5), expected_output)

    def test_multiplication_table_zero(self):
        expected_output = "0x1=0\n0x2=0\n0x3=0\n0x4=0\n0x5=0\n"
        self.assertEqual(multiplication_table(0), expected_output)

    def test_multiplication_table_negative(self):
        expected_output = "-5x1=-5\n-5x2=-10\n-5x3=-15\n-5x4=-20\n-5x5=-25\n"
        self.assertEqual(multiplication_table(-5), expected_output)

    def test_multiplication_table_large_number(self):
        expected_output = "100x1=100\n100x2=200\n100x3=300\n100x4=400\n100x5=500\n"
        self.assertEqual(multiplication_table(100), expected_output)


# Unit tests for task 2
    def test_sum_positive(self):
        expected_output = 6
        self.assertEqual(sum(2, 4), expected_output)

    def test_sum_negative(self):
        expected_output = -7
        self.assertEqual(sum(-2, -5), expected_output)

    def test_sum_large_number(self):
        expected_output = 1001
        self.assertEqual(sum(500, 501), expected_output)

    def test_sum_large_string(self):
        expected_output = "Hello, world!"
        self.assertEqual(sum("Hello,", " world!"), expected_output)

    def test_sum_zero(self):
        expected_output = 0
        self.assertEqual(sum(0, 0), expected_output)

    def test_sum_float(self):
        expected_output = 5.3
        result = sum(2.5, 2.8)
        self.assertEqual(result, expected_output)


# Unit tests for task 3
    def test_text_positive(self):
        expected_output = "olleH"
        result = text("Hello")
        self.assertEqual(expected_output, result)

    def test_text_number(self):
        expected_output = "123"
        result = text("321")
        self.assertEqual(expected_output, result)

    def test_text_long(self):
        expected_output = "?uoy era woh ,olleH"
        result = text("Hello, how are you?")
        self.assertEqual(expected_output, result)

    def test_text_long(self):
        expected_output = "?uoy era woh ,olleH"
        result = text("Hello, how are you?")
        self.assertEqual(expected_output, result)

    def test_text_uppercase(self):
        expected_output = "HELLO"
        result = text("OLLEH")
        self.assertEqual(expected_output, result)

    def test_text_lowercase(self):
        expected_output = "hello"
        result = text("olleh")
        self.assertEqual(expected_output, result)

    def test_text_lowercase(self):
        expected_output = "hello"
        result = text("olleh")
        self.assertEqual(expected_output, result)


# Unit tests for task 4
    def test_filter_one_element(self):
        expected_output = ["Test"]
        result = filter_strings([1, "Test", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_two_element(self):
        expected_output = ["Test1", "Test2"]
        result = filter_strings([1, "Test1", "Test2", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_long_element(self):
        expected_output = ["Test, Test, Test, Test, Test, Test, Test, Test"]
        result = filter_strings(
            [1, "Test, Test, Test, Test, Test, Test, Test, Test", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26},
             [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_uppercase(self):
        expected_output = ["TEST"]
        result = filter_strings([1, "TEST", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_lowercase(self):
        expected_output = ["test"]
        result = filter_strings([1, "test", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_string_number(self):
        expected_output = ["123"]
        result = filter_strings([1, "123", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


    def test_filter_string_float(self):
        expected_output = ["1.2"]
        result = filter_strings([1, "1.2", True, 3.14, (1, 2, 3), {"name": "Valentyn", "age": 26}, [4, 5, 6]])
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main()