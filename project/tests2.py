import unittest #framework
from functions import sum, abba

d = [1, 2, 3]
a = 10
b = 5
print (sum(d))
class TestSum(unittest.TestCase):

    def test_list_int(self): # test that it can sum a list of integers  //self.testnumber
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_abba_ab(self):
        result = a**b
        self.assertEqual(result, 100000)

if __name__ == '__main__': 
    unittest.main()