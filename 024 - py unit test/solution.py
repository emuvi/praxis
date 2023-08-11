import unittest


def sum(a, b):
    return a + b


class Tester(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(2, sum(1, 1))


if __name__ == '__main__':
    unittest.main()
