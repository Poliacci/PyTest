import unittest #framework

def add(a, b):# function, that must be able to both additions and subtractions(like 3 + (-2) == 3 - 2 == 1)
    return a + b # a * b
# Здесь определены тестовые классы и методы тестирования

class MyTestCase(unittest.TestCase):
    def test_addition(self): # test of the addition(+)
        self.assertEqual(add(2, 2), 4)

    def test_subtraction(self): # test of the subtraction(-)
        self.assertEqual(add(5, -2), 3)

if __name__ == '__main__': #блок кода, находящийся под строкой if __name__ == '__main__':, будет выполняться только в том случае, если файл запущен непосредственно, а не импортирован как модуль
    unittest.main()