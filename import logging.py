import logging
import time
import unittest

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.ERROR)

# Decorator function to log errors
def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            print(f"An error occurred. Check the log file for details.")
    return wrapper

# Decorator function to calculate execution time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time:.5f} seconds")
        return result
    return wrapper

# Calculator class with decorated methods
class Calculator:
    @staticmethod
    @log_errors
    @calculate_time
    def add(x, y):
        return x + y

    @staticmethod
    @log_errors
    @calculate_time
    def subtract(x, y):
        return x - y

    @staticmethod
    @log_errors
    @calculate_time
    def multiply(x, y):
        return x * y

    @staticmethod
    @log_errors
    @calculate_time
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(5, 2), 7)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(8, 3), 5)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(4, 6), 24)

def test_division(self):
    self.assertEqual(Calculator.divide(10, 2), 5)
    with self.assertRaises(ValueError, msg="Expected ValueError for division by zero"):
        Calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
