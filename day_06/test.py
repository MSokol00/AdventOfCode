import unittest
from parameterized import parameterized
from .day_06 import part_01, part_02


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
    ])
    def test_part_01(self, input, expected_output):
        self.assertEqual(expected_output, part_01(input))

    @parameterized.expand([
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
    ])
    def test_part_02(self, input, expected_output):
        self.assertEqual(expected_output, part_02(input))


if __name__ == '__main__':
    unittest.main()
