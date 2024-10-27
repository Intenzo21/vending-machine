class Currency:
    """A class to represent currency and manage denominations."""

    # Define available denominations in pence (for simplicity)
    # Denominations are sorted in descending order for easier change calculation
    DENOMINATIONS = (200, 100, 50, 20, 10, 5, 2, 1)
    INITIAL_DENOMINATION_COUNT = 10
    MAX_DENOMINATION_COUNT = 20

    def __init__(self):
        """Initialize the Currency with default denomination counts."""
        self._denomination_counts = {denom: Currency.INITIAL_DENOMINATION_COUNT for denom in Currency.DENOMINATIONS}
        self._inserted_money = {}  # Stores the money inserted by the user

    @property
    def denomination_counts(self) -> dict:
        return self._denomination_counts.copy()  # Return a copy to prevent direct modification

    @property
    def inserted_money(self) -> dict:
        return self._inserted_money.copy()  # Return a copy to prevent direct modification

    def insert_to_storage(self, denom: int) -> None:
        """
        Insert a denomination to the storage.

        Args:
            denom (int): The denomination to insert.

        Raises:
            ValueError: If the denomination is invalid.
        """
        self.ensure_valid_denomination(denom)
        self._inserted_money[denom] = self._inserted_money.get(denom, 0) + 1

    def is_valid_denomination(self, denom: int) -> bool:
        """
        Check if the denomination is valid.

        Args:
            denom (int): The denomination to check.

        Returns:
            bool: True if the denomination is valid, False otherwise.
        """
        return denom in self._denomination_counts

    def ensure_valid_denomination(self, denom: int) -> None:
        """
        Ensure the denomination is valid.

        Args:
            denom (int): The denomination to check.

        Raises:
            ValueError: If the denomination is invalid.
        """
        if not self.is_valid_denomination(denom):
            raise ValueError(f"{denom} is not a valid denomination.")

    def calculate_change(self, balance: int) -> dict[int, int]:
        """
        Calculate the change to return based on the balance.

        Args:
            balance (int): The amount for which change is to be calculated.

        Returns:
            dict: A dictionary with denominations as keys and their counts as values.

        Raises:
            ValueError: If there are insufficient funds or if exact change cannot be returned.
        """
        if self.calculate_denominations_total() < balance:  # Should never occur if denom counts are updated when money is inserted (not implemented yet)
            raise ValueError("Insufficient change funds. Please reload currency denominations.")
        change = {}
        for denom in Currency.DENOMINATIONS:
            if balance <= 0:
                break
            count = min(balance // denom, self._denomination_counts[denom])
            if count > 0:
                balance -= denom * count
                change[denom] = -count
        if balance > 0:
            raise ValueError("Unable to return exact change. Please reload currency denominations.")
        return change

    def update_denomination_counts(self, updates: dict[int, int]) -> None:
        """
        Update the counts of denominations based on the updates.

        Args:
            updates (dict): A dictionary with denominations as keys and their change in counts as values.
                            Positive values increase the count, while negative values decrease it.

        Raises:
            ValueError: If the denomination is invalid, or if the new count would be negative or exceeds the maximum allowed count.
            TypeError: If count is not an integer.
        """
        for denom, count_update in updates.items():
            self._validate_denomination_count_update(denom, count_update)

        for denom, count_update in updates.items():
            self._denomination_counts[denom] += count_update

    def update_denomination_count(self, denom: int, count_update: int) -> None:
        """
        Update the count of a specific denomination.

        Args:
            denom (int): The denomination to update.
            count_update (int): The amount to add (or subtract if negative).

        Raises:
            ValueError: If the denomination is invalid, or if the new count would be negative or exceeds the maximum allowed count.
            TypeError: If count is not an integer.
        """
        self._validate_denomination_count_update(denom, count_update)
        self._denomination_counts[denom] += count_update

    def _validate_denomination_count_update(self, denom: int, count_update: int) -> None:
        """
        Validate the update of a specific denomination count.

        Args:
            denom (int): The denomination to update.
            count_update (int): The amount to add (or subtract if negative).

        Raises:
            ValueError: If the denomination is invalid, or if the new count would be negative or exceeds the maximum allowed count.
            TypeError: If count is not an integer.
        """
        if not isinstance(count_update, int):
            raise TypeError("Count must be an integer.")
        self.ensure_valid_denomination(denom)

        new_count = self._denomination_counts.get(denom) + count_update
        if new_count < 0:
            raise ValueError(f"Cannot update {denom}: resulting count would be negative.")
        if new_count > Currency.MAX_DENOMINATION_COUNT:
            raise ValueError(f"Cannot update {denom}: exceeds maximum allowed count.")

    def calculate_denominations_total(self) -> int:
        """
        Calculate the total value of the denominations.

        Returns:
            int: The total value of all denominations.
        """
        return sum(denom * count for denom, count in self._denomination_counts.items())

    def __str__(self):
        return (f"Denomination counts: {self._denomination_counts}, "
                f"Max denomination count: {Currency.MAX_DENOMINATION_COUNT}, "
                f"Stored money: {self._inserted_money}")
