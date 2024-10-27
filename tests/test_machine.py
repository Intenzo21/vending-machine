import unittest

from src.vending_machine.machine import VendingMachine
from src.vending_machine.product import Product


class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        """Set up a VendingMachine instance for testing."""
        self.vending_machine = VendingMachine()
        self.product1 = Product(id_=1, name="Coke", price=120, quantity=5)
        self.product2 = Product(id_=2, name="Pepsi", price=100, quantity=3)
        self.product3 = Product(id_=3, name="Fanta", price=100, quantity=1)
        self.product_list = [self.product1, self.product2, self.product3]

    def test_load_products_success(self):
        """Test successful loading of products."""
        self.vending_machine.add_products(self.product_list)
        for product in self.product_list:
            with self.subTest(product=product.name):
                self.assertEqual(product, self.vending_machine.select_product(product.id))

    def test_load_products_with_invalid_product(self):
        """Test loading products with an invalid product."""
        product_list = [self.product1, "product"]
        with self.assertRaises(TypeError):
            self.vending_machine.add_products(product_list)

    def test_insert_money(self):
        """Test inserting valid denominations."""
        denominations = [2, 50, 100, 200]
        expected_balance = 0
        for denom in denominations:
            expected_balance += denom
            with self.subTest(denom=denom):
                self.vending_machine.insert_money(denom)
                self.assertEqual(self.vending_machine.balance, expected_balance)

    def test_insert_invalid_money(self):
        """Test inserting an invalid denomination."""
        with self.assertRaises(ValueError):
            self.vending_machine.insert_money(9999)

    def test_select_product_success(self):
        """Test selecting an available product."""
        self.vending_machine.add_products(self.product_list)
        for product in self.product_list:
            with self.subTest(product=product.name):
                selected_product = self.vending_machine.select_product(product.id)
                self.assertEqual(selected_product.id, product.id)

    def test_select_product_out_of_stock(self):
        """Test selecting a product that is out of stock."""
        self.vending_machine.add_product(self.product3)
        self.vending_machine.insert_money(self.product3.price)
        self.vending_machine.purchase_product(3)  # Purchase the only product
        with self.assertRaises(ValueError):
            self.vending_machine.select_product(3)

    def test_purchase_product_success(self):
        """Test purchasing a product with sufficient balance."""
        self.vending_machine.add_product(self.product1)
        self.vending_machine.insert_money(200)  # Insert more than the product price
        self.vending_machine.purchase_product(1)  # Purchase product ID 1
        self.assertEqual(self.vending_machine.balance, 80)  # 200 - 120 is 80
        change = self.vending_machine.dispense_change()
        self.assertEqual(change, {50: -1, 20: -1, 10: -1})

    def test_purchase_product_insufficient_balance(self):
        """Test purchasing a product with insufficient balance."""
        self.vending_machine.add_product(self.product1)
        self.vending_machine.insert_money(100)  # Insert less than the product price
        with self.assertRaises(ValueError):
            self.vending_machine.purchase_product(1)

    def test_reload_product(self):
        """Test reloading a product in the inventory."""
        self.vending_machine.add_product(self.product1)
        self.vending_machine.reload_product(self.product1.id, 10)  # Reload 10 units
        self.assertEqual(self.product1.quantity, 15)  # 5 (initial) + 10 is 15

    def test_reload_currency(self):
        """Test reloading currency denominations."""
        self.vending_machine.reload_currency(100, 5)  # Reload 5 of 100 pence
        self.assertEqual(self.vending_machine.get_denomination_counts()[100], 15)

    def test_list_products_returns_all_products(self):
        """List all products in the inventory."""
        self.vending_machine.add_products(self.product_list)
        products = self.vending_machine.list_products()
        for product in self.product_list:
            with self.subTest(product=product.name):
                self.assertIn(str(product), products)

    def test_list_products_empty_inventory(self):
        """List products when inventory is empty."""
        products = self.vending_machine.list_products()
        self.assertEqual(products, [])


if __name__ == "__main__":
    unittest.main()
