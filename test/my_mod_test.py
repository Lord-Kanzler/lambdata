import unittest
from lambdata13.my_mod import enlarge

class TestMyMod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(enlarge(3), 300)


if __name__ == "__main__":
    unittest.main()
