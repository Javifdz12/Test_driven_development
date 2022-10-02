import unittest
from calculator import calculator
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()

    def test_initial_value(self):
        calc = calculator()
        self.assertEqual(0, calc.value)

    def test_add_method(self):
        self.calc.add(1, 3)
        self.assertEqual(4, self.calc.value)