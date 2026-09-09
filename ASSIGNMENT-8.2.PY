"""
LAB 8: Test-Driven Development with AI
---------------------------------------
Using Python and unittest

Tasks:
1. Even/Odd Number Validator
2. String Case Converter
3. List Sum Calculator
4. Student Result Class
5. Username Validator
"""

import unittest


# ============================================================
# TASK 1: EVEN / ODD NUMBER VALIDATOR
# ============================================================

def is_even(n):
    """
    Returns True if n is an even integer.
    Returns False if n is an odd integer.
    Raises TypeError if the input is not an integer.
    """

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    return n % 2 == 0


class TestEvenOdd(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(2))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_zero(self):
        self.assertTrue(is_even(0))

    def test_negative_even_number(self):
        self.assertTrue(is_even(-4))

    def test_negative_odd_number(self):
        self.assertFalse(is_even(-5))

    def test_large_even_number(self):
        self.assertTrue(is_even(1000000000))

    def test_large_odd_number(self):
        self.assertFalse(is_even(999999999))

    def test_invalid_string(self):
        with self.assertRaises(TypeError):
            is_even("2")

    def test_invalid_float(self):
        with self.assertRaises(TypeError):
            is_even(2.5)


# ============================================================
# TASK 2: STRING CASE CONVERTER
# ============================================================

def to_uppercase(text):
    """
    Converts a string to uppercase.
    Raises TypeError for invalid input.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text.upper()


def to_lowercase(text):
    """
    Converts a string to lowercase.
    Raises TypeError for invalid input.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return text.lower()


class TestStringCaseConverter(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual(to_uppercase("ai coding"), "AI CODING")

    def test_lowercase(self):
        self.assertEqual(to_lowercase("TEST"), "test")

    def test_uppercase_mixed_case(self):
        self.assertEqual(to_uppercase("PyThOn"), "PYTHON")

    def test_lowercase_mixed_case(self):
        self.assertEqual(to_lowercase("PyThOn"), "python")

    def test_uppercase_empty_string(self):
        self.assertEqual(to_uppercase(""), "")

    def test_lowercase_empty_string(self):
        self.assertEqual(to_lowercase(""), "")

    def test_uppercase_numbers(self):
        with self.assertRaises(TypeError):
            to_uppercase(123)

    def test_lowercase_numbers(self):
        with self.assertRaises(TypeError):
            to_lowercase(123)

    def test_uppercase_none(self):
        with self.assertRaises(TypeError):
            to_uppercase(None)

    def test_lowercase_none(self):
        with self.assertRaises(TypeError):
            to_lowercase(None)


# ============================================================
# TASK 3: LIST SUM CALCULATOR
# ============================================================

def sum_list(numbers):
    """
    Calculates the sum of numeric values in a list.

    Non-numeric values are ignored safely.
    Raises TypeError if the input itself is not a list.
    """

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    total = 0

    for value in numbers:

        # Ignore non-numeric values
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            total += value

    return total


class TestListSum(unittest.TestCase):

    def test_normal_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, 5, -4]), 0)

    def test_mixed_numeric_and_string(self):
        self.assertEqual(sum_list([2, "a", 3]), 5)

    def test_all_negative_numbers(self):
        self.assertEqual(sum_list([-2, -3, -5]), -10)

    def test_decimal_numbers(self):
        self.assertEqual(sum_list([1.5, 2.5, 3]), 7)

    def test_strings_only(self):
        self.assertEqual(sum_list(["a", "b", "c"]), 0)

    def test_none_values(self):
        self.assertEqual(sum_list([1, None, 2]), 3)

    def test_boolean_values_are_ignored(self):
        self.assertEqual(sum_list([1, True, 2]), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_list("123")


# ============================================================
# TASK 4: STUDENT RESULT CLASS
# ============================================================

class StudentResult:
    """
    Stores student marks and calculates average and result.

    Rules:
    - Marks must be between 0 and 100.
    - Average >= 40 means Pass.
    - Average < 40 means Fail.
    """

    def __init__(self):
        self.marks = []

    def add_marks(self, mark):
        """
        Adds a valid mark to the list.
        """

        if not isinstance(mark, (int, float)):
            raise TypeError("Marks must be numeric")

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.marks.append(mark)

    def calculate_average(self):
        """
        Calculates the average of all marks.
        """

        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)

    def get_result(self):
        """
        Returns Pass if average is 40 or more.
        Otherwise returns Fail.
        """

        if self.calculate_average() >= 40:
            return "Pass"

        return "Fail"


class TestStudentResult(unittest.TestCase):

    def test_pass_result(self):
        student = StudentResult()

        student.add_marks(60)
        student.add_marks(70)
        student.add_marks(80)

        self.assertEqual(student.calculate_average(), 70)
        self.assertEqual(student.get_result(), "Pass")

    def test_fail_result(self):
        student = StudentResult()

        student.add_marks(30)
        student.add_marks(35)
        student.add_marks(40)

        self.assertEqual(student.calculate_average(), 35)
        self.assertEqual(student.get_result(), "Fail")

    def test_zero_mark(self):
        student = StudentResult()

        student.add_marks(0)

        self.assertEqual(student.calculate_average(), 0)
        self.assertEqual(student.get_result(), "Fail")

    def test_hundred_mark(self):
        student = StudentResult()

        student.add_marks(100)

        self.assertEqual(student.calculate_average(), 100)
        self.assertEqual(student.get_result(), "Pass")

    def test_boundary_pass(self):
        student = StudentResult()

        student.add_marks(40)

        self.assertEqual(student.get_result(), "Pass")

    def test_negative_mark(self):
        student = StudentResult()

        with self.assertRaises(ValueError):
            student.add_marks(-10)

    def test_mark_above_100(self):
        student = StudentResult()

        with self.assertRaises(ValueError):
            student.add_marks(101)

    def test_invalid_mark_string(self):
        student = StudentResult()

        with self.assertRaises(TypeError):
            student.add_marks("80")

    def test_no_marks(self):
        student = StudentResult()

        self.assertEqual(student.calculate_average(), 0)
        self.assertEqual(student.get_result(), "Fail")


# ============================================================
# TASK 5: USERNAME VALIDATOR
# ============================================================

def is_valid_username(username):
    """
    Validates a username.

    Requirements:
    - Minimum length: 5 characters
    - No spaces
    - Only alphanumeric characters
    """

    if not isinstance(username, str):
        return False

    if len(username) < 5:
        return False

    if " " in username:
        return False

    if not username.isalnum():
        return False

    return True


class TestUsernameValidator(unittest.TestCase):

    def test_valid_username(self):
        self.assertTrue(is_valid_username("user01"))

    def test_short_username(self):
        self.assertFalse(is_valid_username("ai"))

    def test_username_with_space(self):
        self.assertFalse(is_valid_username("user name"))

    def test_username_with_special_character(self):
        self.assertFalse(is_valid_username("user@123"))

    def test_exactly_five_characters(self):
        self.assertTrue(is_valid_username("user1"))

    def test_four_characters(self):
        self.assertFalse(is_valid_username("user"))

    def test_empty_username(self):
        self.assertFalse(is_valid_username(""))

    def test_username_with_underscore(self):
        self.assertFalse(is_valid_username("user_1"))

    def test_username_with_hyphen(self):
        self.assertFalse(is_valid_username("user-1"))

    def test_numeric_username(self):
        self.assertTrue(is_valid_username("12345"))

    def test_none_username(self):
        self.assertFalse(is_valid_username(None))

    def test_number_as_username(self):
        self.assertFalse(is_valid_username(12345))


# ============================================================
# DEMONSTRATION OF EXPECTED OUTPUT
# ============================================================

def demonstrate_tasks():

    print("\n" + "=" * 60)
    print("LAB 8: TEST-DRIVEN DEVELOPMENT WITH AI")
    print("=" * 60)

    print("\nTASK 1: EVEN / ODD NUMBER VALIDATOR")
    print("--------------------------------------------")
    print("is_even(2)  ->", is_even(2))
    print("is_even(7)  ->", is_even(7))
    print("is_even(0)  ->", is_even(0))
    print("is_even(-4) ->", is_even(-4))
    print("is_even(-5) ->", is_even(-5))

    print("\nTASK 2: STRING CASE CONVERTER")
    print("--------------------------------------------")
    print('to_uppercase("ai coding") ->', to_uppercase("ai coding"))
    print('to_lowercase("TEST") ->', to_lowercase("TEST"))
    print('to_uppercase("") ->', to_uppercase(""))
    print('to_lowercase("PyThOn") ->', to_lowercase("PyThOn"))

    print("\nTASK 3: LIST SUM CALCULATOR")
    print("--------------------------------------------")
    print("sum_list([1, 2, 3]) ->", sum_list([1, 2, 3]))
    print("sum_list([]) ->", sum_list([]))
    print("sum_list([-1, 5, -4]) ->", sum_list([-1, 5, -4]))
    print('sum_list([2, "a", 3]) ->', sum_list([2, "a", 3]))

    print("\nTASK 4: STUDENT RESULT")
    print("--------------------------------------------")

    student1 = StudentResult()

    for mark in [60, 70, 80]:
        student1.add_marks(mark)

    print("Marks: [60, 70, 80]")
    print("Average ->", student1.calculate_average())
    print("Result  ->", student1.get_result())

    student2 = StudentResult()

    for mark in [30, 35, 40]:
        student2.add_marks(mark)

    print("\nMarks: [30, 35, 40]")
    print("Average ->", student2.calculate_average())
    print("Result  ->", student2.get_result())

    print("\nTASK 5: USERNAME VALIDATOR")
    print("--------------------------------------------")
    print('is_valid_username("user01") ->',
          is_valid_username("user01"))

    print('is_valid_username("ai") ->',
          is_valid_username("ai"))

    print('is_valid_username("user name") ->',
          is_valid_username("user name"))

    print('is_valid_username("user@123") ->',
          is_valid_username("user@123"))

    print('is_valid_username("user1") ->',
          is_valid_username("user1"))


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # First display examples
    demonstrate_tasks()

    # Run all unit tests
    print("\n" + "=" * 60)
    print("RUNNING ALL TEST CASES")
    print("=" * 60)

    unittest.main(verbosity=2)