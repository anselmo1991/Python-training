import unittest
from time import sleep
from io import StringIO
from unittest.mock import patch
from task_timeit import timeit


class TestTimeitDecorator(unittest.TestCase):
    def test_execution_time_above_threshold(self):
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            @timeit(threshold=0.1)
            def test_function():
                sleep(0.2)
            test_function()
            expected_output = "Function 'test_function' took"
            self.assertIn(expected_output, captured_output.getvalue())

    def test_execution_time_below_threshold(self):
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            @timeit(threshold=0.5)
            def test_function():
                sleep(0.2)
            test_function()
            self.assertEqual("", captured_output.getvalue().strip())

    def test_no_threshold(self):
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            @timeit()
            def test_function():
                sleep(0.2)
            test_function()
            expected_output = "Function 'test_function' took"
            self.assertIn(expected_output, captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
