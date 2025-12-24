import unittest
from unittest.mock import patch
import io
import sys
import main

class TestPasswordGenerator(unittest.TestCase):

    @patch('builtins.input', side_effect=['5', '2', '3']) # Mocking user input for nr_letters, nr_symbols, nr_numbers
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_password_generation(self, mock_stdout, mock_input):
        # We need to re-run the main script to capture its output with mocked inputs
        # A better approach for testing would be to refactor main.py into a function
        # that returns the password, rather than printing it directly and taking input.
        with patch.object(main.random, 'shuffle') as mock_shuffle:
            mock_shuffle.side_effect = lambda x: x # Disable shuffling for predictable output
            # Reload main to re-execute the script's top-level code with mocks
            import importlib
            importlib.reload(main)

        output = mock_stdout.getvalue()
        self.assertIn("Your password is:", output)
        
        # Extract the generated password from the output
        password_line = [line for line in output.splitlines() if "Your password is:" in line][0]
        generated_password = password_line.split(": ")[1]

        # Basic check: password length
        # Expected length = 5 letters + 2 symbols + 3 numbers = 10
        self.assertEqual(len(generated_password), 10)

        # Basic check: ensure it contains characters from all categories (this is simplified)
        # Without mocking random.choice, this is hard to assert precisely.
        # With shuffle disabled, we can check for specific characters if we knew the choices.
        # For this simple test, we'll just check if it's not empty and has the correct length.

if __name__ == '__main__':
    unittest.main()
