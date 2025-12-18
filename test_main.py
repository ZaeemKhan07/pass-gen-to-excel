
import unittest
from unittest.mock import patch, MagicMock
import runpy
import sys
from io import StringIO

class TestMain(unittest.TestCase):

    def setUp(self):
        # This helps to run the script in isolation for each test
        if 'main' in sys.modules:
            del sys.modules['main']
        
        # It's also good practice to unload the module under test's dependencies
        if 'saving_password' in sys.modules:
            del sys.modules['saving_password']

    @patch('builtins.input', side_effect=['8', '2', '2'])
    @patch('saving_password.save_to_excel')
    def test_password_generation_length_and_save_call(self, mock_save, mock_input):
        """
        Test that the generated password has the correct total length based on user inputs
        and that the save function is called with the correct arguments.
        """
        # Capture standard output to prevent clutter and for potential assertions
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Execute the main.py script
            runpy.run_path('main.py', run_name='__main__')
        finally:
            # Restore standard output
            sys.stdout = original_stdout

        # Assert that save_to_excel was called exactly once
        mock_save.assert_called_once()

        # Retrieve the arguments from the mocked call
        args, _ = mock_save.call_args
        num_letters, num_symbols, num_numbers, password = args

        # Check if the inputs match what was provided
        self.assertEqual(num_letters, 8)
        self.assertEqual(num_symbols, 2)
        self.assertEqual(num_numbers, 2)

        # Check if the generated password has the correct length
        self.assertEqual(len(password), 8 + 2 + 2)

    @patch('builtins.input', side_effect=['3', '1', '2'])
    @patch('random.choice', side_effect=['x', 'y', 'z', '@', '8', '9'])
    @patch('random.shuffle', side_effect=lambda l: l.reverse()) # Predictable "shuffle"
    @patch('saving_password.save_to_excel')
    def test_password_content_is_correct(self, mock_save, mock_shuffle, mock_choice, mock_input):
        """
        Test that the generated password contains the exact characters chosen
        by the mocked random.choice function.
        """
        runpy.run_path('main.py', run_name='__main__')

        mock_save.assert_called_once()
        
        # The arguments are positional, not keyword
        args, _ = mock_save.call_args
        password = args[3]

        # The expected characters are ['x', 'y', 'z', '@', '8', '9']
        # The shuffle mock reverses the list, so the password will be '98@zyx'
        self.assertEqual(password, '98@zyx')
        
    @patch('builtins.input', side_effect=['4', '1', '1'])
    @patch('saving_password.save_to_excel')
    def test_output_format(self, mock_save, mock_input):
        """
        Test that the script prints the welcome message and the final password
        in the expected format.
        """
        original_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        try:
            runpy.run_path('main.py', run_name='__main__')
        finally:
            sys.stdout = original_stdout
            
        output = captured_output.getvalue()
        
        # Check for the welcome message
        self.assertIn("Welcome to the PyPassword Generator!", output)
        
        # Check for the password output line
        # The strip is needed to remove trailing newlines
        self.assertIn(f"Your password is: {mock_save.call_args[0][3]}", output.strip())

if __name__ == '__main__':
    unittest.main()
