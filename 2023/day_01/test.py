import unittest
from .task import part_01, part_02


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file = open('./day_01/test_input.txt')
        self.file2 = open('./day_01/test_input_2.txt')

    def tearDown(self) -> None:
        self.file.close()
        self.file2.close()

    def test_part_01(self):
        self.assertEqual(142, part_01(self.file))

    def test_part_02(self):
        self.assertEqual(281, part_02(self.file2))


if __name__ == '__main__':
    unittest.main()
