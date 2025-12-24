import unittest
from main import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_length_calculation(self):
        # Request 5 letters, 2 symbols, 2 numbers = 9 characters total
        pwd = generate_password(5, 2, 2)
        self.assertEqual(len(pwd), 9)

if __name__ == '__main__':
    unittest.main()