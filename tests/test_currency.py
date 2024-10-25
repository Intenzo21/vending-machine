import unittest

from src.vending_machine.currency import Currency


class TestCurrency(unittest.TestCase):
    def setUp(self):
        """Set up a Currency instance for testing."""
        self.currency = Currency()

    def test_initial_denomination_counts(self):
        """Test initial denomination counts."""
        expected_counts = {denom: 10 for denom in Currency.DENOMINATIONS}
        self.assertEqual(self.currency.denomination_counts, expected_counts)

    def test_is_valid_denomination(self):
        """Test valid and invalid denominations."""
        self.assertTrue(self.currency.is_valid_denomination(100))
        self.assertFalse(self.currency.is_valid_denomination(3))

    def test_calculate_change_success(self):
        """Test calculating change successfully."""
        change = self.currency.calculate_change(200)
        expected_change = {200: 1}  # Expecting one 200 denomination
        self.assertEqual(change, expected_change)

    def test_update_denomination_valid(self):
        """Test updating a valid denomination count."""
        self.currency.update_denomination_count(100, 5)
        self.assertEqual(self.currency.denomination_counts[100], 15)

    def test_update_denomination_invalid(self):
        """Test updating an invalid denomination raises an error."""
        with self.assertRaises(ValueError):
            self.currency.update_denomination_count(3, 1)

    def test_update_denomination_negative_result(self):
        """Test updating denomination count to negative raises an error."""
        with self.assertRaises(ValueError):
            self.currency.update_denomination_count(10, -15)  # Would result in negative count

    def test_update_denomination_exceed_max_count(self):
        """Test updating denomination exceeds maximum count raises an error."""
        with self.assertRaises(ValueError):
            self.currency.update_denomination_count(20, 15)  # Would exceed the max count of 20

    def test_calculate_denominations_total(self):
        """Test calculating total value of denominations."""
        total = self.currency.calculate_denominations_total()
        expected_total = sum(denom * count for denom, count in self.currency.denomination_counts.items())
        self.assertEqual(total, expected_total)

    def test_calculate_change_insufficient_funds(self):
        """Test calculating change with insufficient funds."""
        total = self.currency.calculate_denominations_total()
        with self.assertRaises(ValueError):
            self.currency.calculate_change(total + 1)  # More than total value


if __name__ == '__main__':
    unittest.main()
