class Currency:
    """A class to represent currency and manage denominations."""

    # Define available denominations in pence (for simplicity)
    # Denominations are sorted in descending order for easier change calculation
    DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]
    MAX_DENOMINATION_COUNT = 20

    def __init__(self):
        """Initialize the Currency with default denomination counts."""
        self._denomination_counts = {denom: 10 for denom in Currency.DENOMINATIONS}

    @property
    def denomination_counts(self) -> dict:
        return self._denomination_counts.copy()  # Return a copy to prevent direct modification

    def is_valid_denomination(self, denom: int) -> bool:
        """Check if the denomination is valid.

        Args:
            denom (int): The denomination to check.

        Returns:
            bool: True if the denomination is valid, False otherwise.
        """
        return denom in self._denomination_counts

    def calculate_change(self, balance: int) -> dict:
        """Calculate the change to return based on the balance.

        Args:
            balance (int): The amount for which change is to be calculated.

        Returns:
            dict: A dictionary with denominations as keys and their counts as values.

        Raises:
            ValueError: If there are insufficient funds or if exact change cannot be returned.
        """
        if self.calculate_denominations_total() < balance:  # Should ideally never occur, but just in case :)
            raise ValueError("Insufficient funds")
        change = {}
        for denom in Currency.DENOMINATIONS:
            if balance <= 0:
                break
            count = min(balance // denom, self._denomination_counts[denom])
            if count > 0:
                balance -= denom * count
                change[denom] = count
        if balance > 0:
            raise ValueError("Unable to return exact change")
        return change

    def update_denominations(self, change: dict) -> None:
        """Update the counts of denominations based on the change.

        Args:
            change (dict): A dictionary with denominations as keys and their counts as values.

        Raises:
            ValueError: If the denomination is invalid, or if the new count would be negative or exceeds the maximum allowed count.
            TypeError: If count is not an integer.
        """
        for denom, count in change.items():
            self.update_denomination(denom, count)

    def update_denomination(self, denom: int, count: int) -> None:
        """Update the count of a specific denomination.

        Args:
            denom (int): The denomination to update.
            count (int): The amount to add (or subtract if negative).

        Raises:
            ValueError: If the denomination is invalid, or if the new count would be negative or exceeds the maximum allowed count.
            TypeError: If count is not an integer.
        """
        if not isinstance(count, int):
            raise TypeError("Count must be an integer.")
        if not self.is_valid_denomination(denom):
            raise ValueError(f"{denom} is not a valid denomination")

        new_count = self.denomination_counts.get(denom) + count
        if new_count < 0:
            raise ValueError(f"Cannot update {denom}: resulting count would be negative")
        if new_count > Currency.MAX_DENOMINATION_COUNT:
            raise ValueError(f"Cannot update {denom}: exceeds maximum allowed count")

        self.denomination_counts[denom] = new_count

    def calculate_denominations_total(self):
        """Calculate the total value of the denominations.

        Returns:
            int: The total value of all denominations.
        """
        return sum(denom * count for denom, count in self.denomination_counts.items())
