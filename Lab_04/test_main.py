import unittest
import main

class TestMyFile(unittest.TestCase):
    
    def test_main(self):
        result = main.main("0standard0")
        self.assertEqual(result, "standard")
    
    def test_main1(self):
        result = main.main("000000000434854719300")
        self.assertEqual(result, "4348547193")

    def test_main2(self):
        result = main.main("przykladbezer")
        self.assertNotEqual(result, "przykladbezzer")

    def test_main3(self):
        result = main.main("Pominę0Parę000Wyrazów00000BezZeraNaKoncuIPoczątku")
        self.assertEqual(result, "ParęWyrazów")

    def test_indexes(self):
        string = "0standard0"
        result = main.indexesOf0(string)
        assert result == [0,9]