import unittest
import subprocess
import os

# Define the full path to the exercise script
exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_2.py")


class TestExample1(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_example_1(self):
        """Test the provided example 1."""
        output = self.run_exercise("7\n")
        self.assertEqual(output, "8\n")

    def test_example_2(self):
        """Test the provided example 2."""
        output = self.run_exercise("10\n")
        self.assertEqual(output, "12\n")

    def test_example_3(self):
        """Test the provided example 3."""
        output = self.run_exercise("11\n")
        self.assertEqual(output, "12\n")


if __name__ == '__main__':
    unittest.main()