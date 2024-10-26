import unittest

from src.vending_machine.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Set up a product instance for use in multiple tests."""
        self.product = Product(id_=1, name="Soda", price=120, quantity=10)

    def test_initialization(self):
        """Test that a product initializes correctly with given attributes."""
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Soda")
        self.assertEqual(self.product.price, 120)
        self.assertEqual(self.product.quantity, 10)

    def test_increase_quantity(self):
        """Test increasing the product quantity within allowed limits."""
        self.product.increase_quantity(5)
        self.assertEqual(self.product.quantity, 15)

    def test_increase_quantity_exceeds_max(self):
        """Test increasing quantity above maximum limit raises an exception."""
        with self.assertRaises(ValueError):
            self.product.increase_quantity(Product.MAX_QUANTITY + 1)

    def test_reduce_quantity(self):
        """Test reducing product quantity within allowed limits."""
        self.product.reduce_quantity(3)
        self.assertEqual(self.product.quantity, 7)

    def test_reduce_quantity_below_zero(self):
        """Test reducing quantity below zero raises an exception."""
        with self.assertRaises(ValueError):
            self.product.reduce_quantity(11)

    def test_str_representation(self):
        """Test the string representation of the Product class."""
        self.assertEqual(str(self.product), "Soda (ID: 1) - Price: 120p, Stock: 10")

    def test_invalid_initial_id(self):
        """Test that initializing a product with invalid ID raises an error."""
        with self.assertRaises(ValueError):
            Product(id_=0, name="Chips", price=150, quantity=5)

    def test_invalid_initial_name(self):
        """Test that initializing a product with invalid name raises an error."""
        with self.assertRaises(ValueError):
            Product(id_=2, name="", price=150, quantity=5)

    def test_invalid_initial_price(self):
        """Test that initializing a product with invalid price raises an error."""
        with self.assertRaises(ValueError):
            Product(id_=2, name="Chips", price=-150, quantity=5)

    def test_invalid_initial_quantity(self):
        """Test that initializing a product with invalid quantity raises an error."""
        with self.assertRaises(ValueError):
            Product(id_=2, name="Chips", price=150, quantity=-5)


if __name__ == "__main__":
    unittest.main()
