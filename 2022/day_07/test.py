import unittest
from .day_07 import part_01, part_02


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file = open('./day_07/test_input.txt')

    def tearDown(self) -> None:
        self.file.close()

    def test_part_01(self):
        self.assertEqual(95437, part_01(self.file))

    def test_part_02(self):
        self.assertEqual(24933642, part_02(self.file))


if __name__ == '__main__':
    unittest.main()
