"""Command-line interface for the sales analyzer."""

import argparse
from pathlib import Path

from .analyzer import (
    average_order_value,
    clean_sales,
    load_sales,
    monthly_revenue,
    top_products,
    total_revenue,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze sales from a CSV file.")
    parser.add_argument("csv_file", nargs="?", default="data/sample_sales.csv", help="Path to sales CSV")
    parser.add_argument("--top", type=int, default=3, help="Number of top products to show")
    args = parser.parse_args()

    rows = clean_sales(load_sales(Path(args.csv_file)))
    print("\nSALES SUMMARY")
    print("-------------")
    print(f"Valid orders:        {len(rows)}")
    print(f"Total revenue:       ₹{total_revenue(rows):,.2f}")
    print(f"Average order value: ₹{average_order_value(rows):,.2f}")

    print(f"\nTop {args.top} products by revenue:")
    products = top_products(rows, args.top)
    if not products:
        print("  No valid sales found.")
    for product, revenue in products:
        print(f"  {product}: ₹{revenue:,.2f}")

    print("\nRevenue by month:")
    months = monthly_revenue(rows)
    if not months:
        print("  No valid sales found.")
    for month, revenue in months.items():
        print(f"  {month}: ₹{revenue:,.2f}")


if __name__ == "__main__":
    main()
