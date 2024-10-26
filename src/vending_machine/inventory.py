from .product import Product


class Inventory:
    """Manages a collection of products for the vending machine."""
    MAX_PRODUCTS = 10

    def __init__(self):
        """Initialize the inventory with an empty product collection."""
        self.__products = {}

    def add_product(self, product: Product):
        """
        Add a new product to the inventory.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If the product already exists in the inventory.
        """
        if self.__product_exists(product.id):
            raise ValueError(f"Product {product.name} (ID: {product.id}) already exists.")
        self.__products[product.id] = product

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
        self.__ensure_product_exists(product_id)
        return self.__products.get(product_id)

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

    def purchase_product(self, product_id: int) -> None:
        """
        Reduce the stock of a specified product by 1 when a purchase is made.

        Args:
            product_id (int): ID of the product to purchase.

        Raises:
            ValueError: If the product is out of stock.
        """
        product = self.get_product(product_id)
        if not self.is_product_available(product_id):
            raise ValueError(f"{product.name} (ID: {product_id}) is out of stock.")
        product.reduce_quantity()

    def reload_product(self, product_id: int, quantity: int):
        """
        Reload a specified product with more stock.

        Args:
            product_id (int): The ID of the product to reload.
            quantity (int): The amount of stock to add.
        """
        product = self.get_product(product_id)
        product.increase_quantity(quantity)

    def list_products(self):
        """
        List all products with their current stock and price.

        Returns:
            list: A list of string representations of all products.
        """
        return [str(product) for product in self.__products.values()]

    def __product_exists(self, product_id: int) -> bool:
        """
        Return True if the product exists in the inventory, False otherwise.

        Args:
            product_id (int): The ID of the product to check.

        Returns:
            bool: True if the product exists, False otherwise.
        """
        return product_id in self.__products

    def __ensure_product_exists(self, product_id: int) -> None:
        """
        Raise an exception if the product does not exist in inventory.

        Args:
            product_id (int): The ID of the product to check.

        Raises:
            ValueError: If the product does not exist in the inventory.
        """
        if not self.__product_exists(product_id):
            raise ValueError(f"Product with ID {product_id} does not exist in inventory")
