__author__ = 'Guru'

import unittest
from Hello import HelloWorld

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Hello()
        self.assertEqual(greeter.message, 'Hello word!')

if __name__ == '__main__':
    unittest.main()
