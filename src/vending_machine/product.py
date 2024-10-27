from .utils import validate_id, validate_name, validate_price, validate_quantity


class Product:
    """Represents a single product in the vending machine."""
    MAX_QUANTITY = 20

    def __init__(self, id_: int, name: str, price: int, quantity: int = 0):
        """
        Initialize a new product.

        Args:
            id_ (int): The unique ID of the product.
            name (str): The name of the product.
            price (int): The price of the product in pence (e.g., 100 for £1).
            quantity (int): Initial stock quantity of the product.
        """
        self._id = validate_id(id_)
        self._name = validate_name(name)
        self._price = validate_price(price)
        self._quantity = validate_quantity(quantity)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    def increase_quantity(self, amount: int):
        """
        Increase the stock of the product by a specified amount.

        Args:
            amount (int): The amount to increase the stock by.

        Raises:
            ValueError: If the new quantity exceeds the maximum stock quantity.
        """
        validate_quantity(amount)
        new_quantity = self._quantity + amount
        if new_quantity > Product.MAX_QUANTITY:
            raise ValueError("Cannot exceed maximum stock quantity.")
        self._quantity = new_quantity

    def reduce_quantity(self, amount: int = 1):
        """
        Reduce the stock of the product by a specified amount.

        Args:
            amount (int): The amount to reduce the stock by. Defaults to 1.

        Raises:
            ValueError: If there is not enough stock to reduce by the specified amount.
        """
        validate_quantity(amount)
        if amount > self._quantity:
            raise ValueError(f"Not enough stock ({self._quantity}) to reduce by that amount ({amount}).")
        self._quantity -= amount

    def __str__(self):
        return f"{self._name} (ID: {self._id}) - Price: {self._price}p, Stock: {self._quantity}"
