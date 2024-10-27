from .currency import Currency
from .inventory import Inventory, Product


class VendingMachine:
    """Represents the vending machine."""

    def __init__(self):
        """Initialize the vending machine with inventory and currency."""
        self._balance = 0  # Stores the current balance inserted by the user
        self._currency = Currency()
        self._inventory = Inventory()

    @property
    def balance(self) -> int:
        return self._balance

    def add_product(self, product: Product) -> None:
        """
        Load a single product into the vending machine inventory.

        Args:
            product (Product): The Product object to load into the inventory.
        """
        self._inventory.add_product(product)

    def add_products(self, product_list: list[Product]) -> None:
        """
        Load a list of products into the vending machine inventory.

        Args:
            product_list (list): A list of Product objects to load into the inventory.
        """
        for product in product_list:
            self.add_product(product)

    def insert_money(self, denom: int) -> None:
        """
        Accept money from the user and add to balance.

        Args:
            denom (int): The denomination inserted by the user, in pence.
        """
        self._currency.ensure_valid_denomination(denom)
        self._balance += denom
        self._currency.insert_to_storage(denom)

    def select_product(self, product_id: int) -> Product:
        """
        Select a product by its ID.

        Args:
            product_id (int): The ID of the product to select.

        Returns:
            Product: The selected product if available.

        Raises:
            ValueError: If the product is unavailable or out of stock.
        """
        self._inventory.ensure_product_available(product_id)
        return self._inventory.get_product(product_id)

    def purchase_product(self, product_id: int) -> None:
        """
        Purchase a product if the balance is sufficient, or prompt for more money.

        Args:
            product_id (int): The ID of the product to purchase.

        Raises:
            ValueError: If the balance is insufficient for the product.
        """
        product = self.select_product(product_id)
        if self._balance < product.price:
            raise ValueError(f"Insufficient balance. Please insert {product.price - self._balance}p more.")

        # Deduct product price from balance and update inventory
        self._balance -= product.price
        self._inventory.reduce_stock(product_id)

    def dispense_change(self) -> dict:
        """
        Dispense change based on the remaining balance and update currency stock.

        Returns:
            dict: A dictionary of denominations as keys and quantities as values for the change given.

        Raises:
            ValueError: If exact change cannot be provided.
        """
        change = self._currency.calculate_change(self._balance)
        self._currency.update_denomination_counts(change)
        self._balance = 0  # Reset balance after dispensing change
        return change

    def reload_product(self, product_id: int, quantity: int) -> None:
        """
        Reload a specified product in the inventory.

        Args:
            product_id (int): The ID of the product to reload.
            quantity (int): The quantity to add.
        """
        self._inventory.reload_product(product_id, quantity)

    def reload_currency(self, denom: int, count: int) -> None:
        """
        Reload specific currency denominations.

        Args:
            denom (int): The denomination to reload.
            count (int): The quantity to add.
        """
        self._currency.update_denomination_count(denom, count)

    def get_denomination_counts(self) -> dict:
        """
        Get the current counts of all denominations in the currency storage.

        Returns:
            dict: A dictionary with denominations as keys and counts as values.
        """
        return self._currency.denomination_counts

    def get_stored_money(self) -> dict:
        """
        Get the current counts of all denominations in the currency storage.

        Returns:
            dict: A dictionary with denominations as keys and counts as values.
        """
        return self._currency.inserted_money

    @staticmethod
    def get_valid_denominations() -> list:
        """
        Get the list of valid denominations.

        Returns:
            list: A list of valid denominations.
        """
        return Currency.DENOMINATIONS

    def list_products(self) -> list:
        """
        List all products in the inventory.

        Returns:
            list: A list of string representations of all products.
        """
        return self._inventory.list_products()

    def __str__(self) -> str:
        return ("\nVending Machine state:"
                f"\n\tAccepted denominations={Currency.DENOMINATIONS}"
                f"\n\tBalance={self.balance}"
                f"\n\tCurrency=({self._currency})"
                f"\n\tInventory=({self._inventory})")
