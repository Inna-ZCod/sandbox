import unittest
from AT.AT01.main import add, subtract, multiply, divide, modulus

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


# Тест для функции остатка от деления

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertNotEqual(modulus(10, 3), 2)

    def test_modulus_by_zero(self):
        self.assertRaises(ValueError, modulus, 17, 0)


if __name__ == '__main__':
    unittest.main()
