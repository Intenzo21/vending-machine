import unittest

from src.vending_machine.inventory import Inventory
from src.vending_machine.product import Product


class TestInventory(unittest.TestCase):

    def setUp(self):
        """Set up an inventory and add a product for testing."""
        self.inventory = Inventory()
        self.product = Product(id_=1, name="Soda", price=120, quantity=10)
        self.inventory.add_product(self.product)

    def test_add_product(self):
        """Test adding new products to the inventory dynamically."""
        test_cases = [
            (Product(id_=2, name="Chips", price=150, quantity=20), 2),  # New product
            (Product(id_=3, name="Candy", price=100, quantity=30), 3),  # Another new product
        ]

        for product, expected_id in test_cases:
            with self.subTest(product=product.name):
                self.inventory.add_product(product)
                self.assertEqual(self.inventory.get_product(expected_id), product)

    def test_add_existing_product(self):
        """Test adding a product that already exists raises an exception."""
        with self.assertRaises(ValueError):
            self.inventory.add_product(self.product)

    def test_get_product(self):
        """Test retrieving products by ID dynamically."""
        test_cases = [
            (1, self.product),  # Valid product
            (99, None),  # Nonexistent product, expecting exception
        ]

        for product_id, expected_product in test_cases:
            with self.subTest(product_id=product_id):
                if expected_product is None:
                    with self.assertRaises(ValueError):
                        self.inventory.get_product(product_id)
                else:
                    retrieved_product = self.inventory.get_product(product_id)
                    self.assertEqual(retrieved_product, expected_product)

    def test_is_product_available(self):
        """Test checking if products are available."""
        test_cases = [
            (1, True),  # Available product
            (99, None),  # Nonexistent product, expecting exception
        ]

        for product_id, expected_availability in test_cases:
            with self.subTest(product_id=product_id):
                if expected_availability is None:
                    with self.assertRaises(ValueError):
                        self.inventory.get_product(product_id)
                else:
                    self.assertEqual(self.inventory.is_product_available(product_id), expected_availability)

    def test_purchase_product(self):
        """Test purchasing a product reduces its quantity."""
        self.inventory.reduce_stock(1)
        self.assertEqual(self.product.quantity, 9)

    def test_purchase_out_of_stock_product(self):
        """Test purchasing an out-of-stock product raises an exception."""
        self.product.reduce_quantity(self.product.quantity)  # Set quantity to 0
        with self.assertRaises(ValueError):
            self.inventory.reduce_stock(1)

    def test_reload_product(self):
        """Test reloading products with valid and invalid cases."""
        test_cases = [
            (1, 5, 15),  # Valid reload
            (1, Product.MAX_QUANTITY + 1, None),  # Exceeding max quantity
        ]

        for product_id, reload_amount, expected_quantity in test_cases:
            with self.subTest(product_id=product_id, reload_amount=reload_amount):
                if expected_quantity is None:
                    with self.assertRaises(ValueError):
                        self.inventory.reload_product(product_id, reload_amount)
                else:
                    self.inventory.reload_product(product_id, reload_amount)
                    self.assertEqual(self.product.quantity, expected_quantity)

    def test_list_products(self):
        """Test listing all products in the inventory."""
        product_list = self.inventory.list_products()
        self.assertIn(str(self.product), product_list)


if __name__ == "__main__":
    unittest.main()
