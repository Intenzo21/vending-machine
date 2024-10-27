import unittest

from src.vending_machine.currency import Currency


class TestCurrency(unittest.TestCase):
    def setUp(self):
        """Set up a Currency instance for testing."""
        self.currency = Currency()

    def test_initial_denomination_counts(self):
        """Test initial denomination counts for each denomination."""
        expected_counts = {denom: Currency.INITIAL_DENOMINATION_COUNT for denom in Currency.DENOMINATIONS}
        self.assertEqual(self.currency.denomination_counts, expected_counts)

    def test_is_valid_denomination(self):
        """Test both valid and invalid denominations dynamically."""
        test_cases = [
            (100, True),
            (3, False),
            (50, True),
            (0, False),
        ]
        for denom, expected in test_cases:
            with self.subTest(denom=denom):
                self.assertEqual(self.currency.is_valid_denomination(denom), expected)

    def test_calculate_change_success(self):
        """Test calculating change for various amounts."""
        test_cases = [
            (200, {200: -1}),
            (50, {50: -1}),
            (70, {50: -1, 20: -1}),  # Example of multiple denominations
        ]
        for amount, expected_change in test_cases:
            with self.subTest(amount=amount):
                self.assertEqual(self.currency.calculate_change(amount), expected_change)

    def test_update_denomination_valid(self):
        """Test updating valid denominations with various values."""
        test_cases = [
            (100, 5),
            (50, -3),
            (10, 10),
        ]
        for denom, count_update in test_cases:
            expected_count = Currency.INITIAL_DENOMINATION_COUNT + count_update
            with self.subTest(denom=denom):
                self.currency.update_denomination_count(denom, count_update)
                self.assertEqual(self.currency.denomination_counts[denom], expected_count)

    def test_update_denomination_invalid(self):
        """Test invalid denomination updates, expecting errors."""
        invalid_denom_cases = [4, 3, 0]  # Nonexistent denominations
        for invalid_denom in invalid_denom_cases:
            with self.subTest(invalid_denom=invalid_denom):
                with self.assertRaises(ValueError):
                    self.currency.update_denomination_count(invalid_denom, 1)

    def test_update_denomination_negative_result(self):
        """Test updating a denomination to a negative result raises an error."""
        negative_update_cases = [
            (10, -15),
            (50, -20),  # If resulting count goes below zero
        ]
        for denom, count_update in negative_update_cases:
            with self.subTest(denom=denom, count_update=count_update):
                with self.assertRaises(ValueError):
                    self.currency.update_denomination_count(denom, count_update)

    def test_update_denomination_exceed_max_count(self):
        """Test exceeding the maximum denomination count limit raises an error."""
        diff = Currency.MAX_DENOMINATION_COUNT - Currency.INITIAL_DENOMINATION_COUNT
        denoms = [1, 20, 100]
        for denom in denoms:
            count_update = diff + 1
            with self.subTest(denom=denom, count_update=count_update):
                with self.assertRaises(ValueError):
                    self.currency.update_denomination_count(denom, count_update)

    def test_calculate_denominations_total(self):
        """Test calculating the total value for different denomination counts."""
        expected_total = sum(denom * count for denom, count in self.currency.denomination_counts.items())
        self.assertEqual(self.currency.calculate_denominations_total(), expected_total)

    def test_calculate_change_insufficient_funds(self):
        """Test calculating change when there is insufficient funds."""
        denominations_total = self.currency.calculate_denominations_total()
        with self.assertRaises(ValueError):
            self.currency.calculate_change(denominations_total + 1)

    def test_calculate_change_exact_change_unavailable(self):
        """Raises error when exact change cannot be returned."""
        self.currency.update_denomination_count(1, -Currency.INITIAL_DENOMINATION_COUNT)  # Remove all 1p coins
        with self.assertRaises(ValueError):
            self.currency.calculate_change(3)

    def test_denomination_counts_valid_updates(self):
        """Test updating multiple denominations with valid changes."""
        test_cases = [
            {100: 5, 50: -3},
            {200: -2, 10: 5},
        ]
        for count_updates in test_cases:
            with self.subTest(count_updates=count_updates):
                self.currency.update_denomination_counts(count_updates)
                for denom, count_update in count_updates.items():
                    expected_count = Currency.INITIAL_DENOMINATION_COUNT + count_update
                    self.assertEqual(self.currency.denomination_counts[denom], expected_count)

    def test_denomination_counts_invalid_updates(self):
        """Test updating with invalid denominations or values raises an error."""
        invalid_updates_cases = [
            {3: 1},  # Invalid denomination
            {10: -15},  # Negative count result
            {20: 15},  # Exceed max count
            {200: 1, 100: "five"},  # Non-integer value
        ]
        for updates in invalid_updates_cases:
            with self.subTest(updates=updates):
                self.assertRaises((TypeError, ValueError), self.currency.update_denomination_counts, updates)


if __name__ == '__main__':
    unittest.main()
