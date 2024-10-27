import unittest

from src.vending_machine.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Set up a product instance for use in multiple tests."""
        self.product = Product(id_=1, name="Soda", price=120, quantity=10)

    def test_initialization(self):
        """Test that a product initializes correctly with various attributes."""
        test_cases = [
            {"id_": 1, "name": "Soda", "price": 120, "quantity": 10},
            {"id_": 2, "name": "Chips", "price": 150, "quantity": 5},
            {"id_": 3, "name": "Water", "price": 100, "quantity": 20},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                product = Product(**case)
                self.assertEqual(product.id, case["id_"])
                self.assertEqual(product.name, case["name"])
                self.assertEqual(product.price, case["price"])
                self.assertEqual(product.quantity, case["quantity"])

    def test_increase_quantity(self):
        """Test increasing the product quantity with multiple values."""
        test_cases = [
            (5, 15),  # Increase by 5, expect total 15
            (0, 10),  # Increase by 0, expect no change
            (10, 20),  # Increase to max quantity
        ]

        for increase_amount, expected_quantity in test_cases:
            with self.subTest(increase_amount=increase_amount):
                self.product.increase_quantity(increase_amount)
                self.assertEqual(self.product.quantity, expected_quantity)
                self.product.reduce_quantity(increase_amount)  # Reset quantity to initial value

    def test_increase_quantity_exceeds_max(self):
        """Test increasing quantity beyond the max limit raises an exception."""
        test_cases = [
            Product.MAX_QUANTITY + 1,
            Product.MAX_QUANTITY + 5,
        ]

        for increase_amount in test_cases:
            with self.subTest(increase_amount=increase_amount):
                with self.assertRaises(ValueError):
                    self.product.increase_quantity(increase_amount)

    def test_reduce_quantity(self):
        """Test reducing product quantity with multiple values."""
        test_cases = [
            (3, 7),  # Reduce by 3, expect 7
            (10, 0),  # Reduce to zero
        ]

        for reduce_amount, expected_quantity in test_cases:
            with self.subTest(reduce_amount=reduce_amount):
                self.product.reduce_quantity(reduce_amount)
                self.assertEqual(self.product.quantity, expected_quantity)
                self.product.increase_quantity(reduce_amount)  # Reset quantity to initial value

    def test_reduce_quantity_below_zero(self):
        """Test reducing quantity below zero raises an exception."""
        test_cases = [11, 15]

        for reduce_amount in test_cases:
            with self.subTest(reduce_amount=reduce_amount):
                with self.assertRaises(ValueError):
                    self.product.reduce_quantity(reduce_amount)

    def test_str_representation(self):
        """Test the string representation of the Product class."""
        expected_string = "Soda (ID: 1) - Price: 120p, Stock: 10"
        self.assertEqual(str(self.product), expected_string)

    def test_invalid_initialization(self):
        """Test invalid initialization values for Product attributes."""
        test_cases = [
            {"id_": 0, "name": "Chips", "price": 150, "quantity": 5},  # Invalid id
            {"id_": 2, "name": "", "price": 150, "quantity": 5},  # Invalid name
            {"id_": 3, "name": "Water", "price": -100, "quantity": 5},  # Invalid price
            {"id_": 4, "name": "Candy", "price": 100, "quantity": -5},  # Invalid quantity
        ]

        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    Product(**case)


if __name__ == "__main__":
    unittest.main()
