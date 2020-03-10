import unittest

class SubTest(unittest.TestCase):
    def test_even(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == "__main__":
    unittest.main()