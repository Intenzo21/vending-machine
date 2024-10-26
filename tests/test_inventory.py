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
        """Test adding a new product to the inventory."""
        chips = Product(id_=2, name="Chips", price=150, quantity=20)
        self.inventory.add_product(chips)
        self.assertEqual(self.inventory.get_product(2), chips)

    def test_add_existing_product(self):
        """Test adding a product that already exists raises an exception."""
        with self.assertRaises(ValueError):
            self.inventory.add_product(self.product)

    def test_get_product(self):
        """Test retrieving a product by ID."""
        retrieved_product = self.inventory.get_product(1)
        self.assertEqual(retrieved_product, self.product)

    def test_get_nonexistent_product(self):
        """Test retrieving a product that does not exist raises an exception."""
        with self.assertRaises(ValueError):
            self.inventory.get_product(99)

    def test_is_product_available(self):
        """Test checking if a product is available."""
        self.assertTrue(self.inventory.is_product_available(1))

    def test_is_product_available_out_of_stock(self):
        """Test that an out-of-stock product is marked as unavailable."""
        self.product.reduce_quantity(self.product.quantity)  # Set quantity to 0
        self.assertFalse(self.inventory.is_product_available(1))

    def test_purchase_product(self):
        """Test purchasing a product reduces its quantity."""
        self.inventory.purchase_product(1)
        self.assertEqual(self.product.quantity, 9)

    def test_purchase_out_of_stock_product(self):
        """Test purchasing an out-of-stock product raises an exception."""
        self.product.reduce_quantity(self.product.quantity)  # Set quantity to 0
        with self.assertRaises(ValueError):
            self.inventory.purchase_product(1)

    def test_reload_product(self):
        """Test reloading a product increases its quantity."""
        self.inventory.reload_product(1, 5)
        self.assertEqual(self.product.quantity, 15)

    def test_reload_product_exceeds_max(self):
        """Test reloading a product above max quantity raises an exception."""
        with self.assertRaises(ValueError):
            self.inventory.reload_product(1, Product.MAX_QUANTITY + 1)

    def test_list_products(self):
        """Test listing all products in the inventory."""
        product_list = self.inventory.list_products()
        self.assertIn(str(self.product), product_list)


if __name__ == "__main__":
    unittest.main()
