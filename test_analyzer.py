import unittest

from sales_analyzer.analyzer import (
    average_order_value,
    clean_sales,
    monthly_revenue,
    top_products,
    total_revenue,
)


class SalesAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.rows = clean_sales([
            {"order_id": "1", "date": "2026-01-02", "product": "Pen", "quantity": "2", "unit_price": "10"},
            {"order_id": "2", "date": "2026-02-02", "product": "Book", "quantity": "1", "unit_price": "50"},
            {"order_id": "2", "date": "2026-02-02", "product": "Book", "quantity": "1", "unit_price": "50"},
            {"order_id": "3", "date": "bad-date", "product": "Bad", "quantity": "1", "unit_price": "1"},
        ])

    def test_cleaning_skips_duplicate_and_invalid_rows(self):
        self.assertEqual(len(self.rows), 2)

    def test_total_revenue(self):
        self.assertEqual(total_revenue(self.rows), 70.0)

    def test_average_order_value(self):
        self.assertEqual(average_order_value(self.rows), 35.0)

    def test_top_products(self):
        self.assertEqual(top_products(self.rows, 1), [("Book", 50.0)])

    def test_monthly_revenue(self):
        self.assertEqual(monthly_revenue(self.rows), {"2026-01": 20.0, "2026-02": 50.0})

    def test_empty_average(self):
        self.assertEqual(average_order_value([]), 0.0)

    def test_invalid_top_limit(self):
        with self.assertRaises(ValueError):
            top_products(self.rows, 0)


if __name__ == "__main__":
    unittest.main()
