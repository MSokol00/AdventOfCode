import unittest
from .day_08 import part_01, part_02

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.input_file = open('./day_08/test_input.txt')

    def test_part_01(self):
        self.assertEqual(21, part_01(self.input_file))

    def test_part_02(self):
        self.assertEqual(8, part_02(self.input_file))

if __name__ == '__main__':
    unittest.main()
