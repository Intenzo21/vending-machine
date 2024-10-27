from .product import Product


class Inventory:
    """Manages a collection of products for the vending machine."""
    MAX_PRODUCTS = 10

    def __init__(self):
        """Initialize the inventory with an empty product collection."""
        self._products = {}

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the inventory.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If the product already exists in the inventory.
        """
        if not isinstance(product, Product):
            raise TypeError("Invalid product type.")
        elif self._product_exists(product.id):
            raise ValueError(f"Product with ID {product.id} already exists.")
        elif len(self._products) >= Inventory.MAX_PRODUCTS:
            raise ValueError(f"Cannot add more than {Inventory.MAX_PRODUCTS} products.")
        self._products[product.id] = product

    def get_product(self, product_id: int) -> Product:
        """
        Return the product object by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID.

        Raises:
            ValueError: If the product does not exist in the inventory.
        """
        self._ensure_product_exists(product_id)
        return self._products.get(product_id)

    def is_product_available(self, product_id: int) -> bool:
        """
        Check if a product is in stock and available.

        Args:
            product_id (int): The ID of the product to check.

        Returns:
            bool: True if the product is available, False otherwise.
        """
        product = self.get_product(product_id)
        return product.quantity > 0

    def ensure_product_available(self, product_id: int) -> None:
        """
        Ensure that a product is available for purchase.

        Args:
            product_id (int): The ID of the product to check.

        Raises:
            ValueError: If the product is out of stock.
        """
        if not self.is_product_available(product_id):
            raise ValueError(f"Product with ID {product_id} is out of stock.")

    def reduce_stock(self, product_id: int) -> None:
        """
        Reduce the stock of a specified product by 1 when a purchase is made.

        Args:
            product_id (int): ID of the product to purchase.

        Raises:
            ValueError: If the product is out of stock.
        """
        product = self.get_product(product_id)
        self.ensure_product_available(product_id)
        product.reduce_quantity()

    def reload_product(self, product_id: int, quantity: int) -> None:
        """
        Reload a specified product with more stock.

        Args:
            product_id (int): The ID of the product to reload.
            quantity (int): The amount of stock to add.
        """
        product = self.get_product(product_id)
        product.increase_quantity(quantity)

    def list_products(self) -> list:
        """
        List all products with their current stock and price.

        Returns:
            list: A list of string representations of all products.
        """
        return [str(product) for product in self._products.values()]

    def _product_exists(self, product_id: int) -> bool:
        """
        Return True if the product exists in the inventory, False otherwise.

        Args:
            product_id (int): The ID of the product to check.

        Returns:
            bool: True if the product exists, False otherwise.
        """
        return product_id in self._products

    def _ensure_product_exists(self, product_id: int) -> None:
        """
        Raise an exception if the product does not exist in inventory.

        Args:
            product_id (int): The ID of the product to check.

        Raises:
            ValueError: If the product does not exist in the inventory.
        """
        if not self._product_exists(product_id):
            raise ValueError(f"Product with ID {product_id} does not exist in inventory.")

    def __str__(self):
        return f"Products: {len(self._products)}/{Inventory.MAX_PRODUCTS}"
