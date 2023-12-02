import unittest
from .task import part_01, part_02


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file = open('./day_02/test_input.txt')

    def tearDown(self) -> None:
        self.file.close()
        # self.file2.close()

    def test_part_01(self):
        self.assertEqual(8, part_01(self.file, 12, 13, 14))

    def test_part_02(self):
        self.assertEqual(2286, part_02(self.file))


if __name__ == '__main__':
    unittest.main()
