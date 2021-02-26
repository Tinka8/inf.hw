import unittest
from du11 import spoj

class PrvaUloha(unittest.TestCase):
    def test_spoj(self):
        """ 
        Test that spoj() return value is a string
        """
        self.assertIsInstance(spoj(["Adam", "nemá", "domácu", "úlohu"]), str)

    def test_spoj_result(self):
        """
        Test that spoj() return expected string
        """
        self.assertEqual("Adam ma domacu ulohu", spoj(["Adam","ma","domacu","ulohu"]))

    def test_spoj_result_2(self):
        """
        Test that spoj() return expected string 
        """
        self.assertEqual("nepi Jano nepi vodu", spoj(["nepi", "Jano", "nepi","vodu"]))


if __name__ == '__main__':
    unittest.main()