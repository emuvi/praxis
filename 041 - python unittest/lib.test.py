import unittest

import lib

class TestLis(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(lib.sum(1, 1), 2)
        
        
if __name__ == '__main__':
    unittest.main()