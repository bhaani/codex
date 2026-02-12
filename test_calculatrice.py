import unittest

from calculatrice import calculer, parser_expression


class TestCalculatrice(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(calculer(2, "+", 3), 5)

    def test_subtraction(self) -> None:
        self.assertEqual(calculer(5, "-", 3), 2)

    def test_multiplication(self) -> None:
        self.assertEqual(calculer(4, "*", 2.5), 10)

    def test_division(self) -> None:
        self.assertEqual(calculer(9, "/", 3), 3)

    def test_division_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            calculer(1, "/", 0)

    def test_parse_expression(self) -> None:
        self.assertEqual(parser_expression("10 * 4"), (10.0, "*", 4.0))

    def test_parse_expression_invalid_format(self) -> None:
        with self.assertRaises(ValueError):
            parser_expression("10 +")


if __name__ == "__main__":
    unittest.main()
