"""Functions for loading, cleaning, and analyzing a small sales CSV."""

from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

REQUIRED_COLUMNS = {"order_id", "date", "product", "quantity", "unit_price"}


def load_sales(file_path: str | Path) -> list[dict[str, str]]:
    """Load rows from a CSV file. Raises a helpful error for missing columns."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Sales file not found: {path}")

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            raise ValueError("CSV is missing required columns: " + ", ".join(sorted(missing)))
        return list(reader)


def clean_sales(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Validate rows, convert numeric fields, and skip invalid or duplicate orders.

    The first valid row for an order_id is kept. Invalid dates, blank products,
    non-positive quantities, and negative prices are skipped.
    """
    cleaned: list[dict[str, Any]] = []
    seen_order_ids: set[str] = set()

    for row in rows:
        order_id = str(row.get("order_id", "")).strip()
        product = str(row.get("product", "")).strip()
        try:
            order_date = datetime.strptime(str(row.get("date", "")).strip(), "%Y-%m-%d").date()
            quantity = int(row.get("quantity", 0))
            unit_price = float(row.get("unit_price", 0))
        except (TypeError, ValueError):
            continue

        if not order_id or not product or order_id in seen_order_ids:
            continue
        if quantity <= 0 or unit_price < 0:
            continue

        cleaned.append({
            "order_id": order_id,
            "date": order_date.isoformat(),
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "revenue": round(quantity * unit_price, 2),
        })
        seen_order_ids.add(order_id)

    return cleaned


def total_revenue(rows: list[dict[str, Any]]) -> float:
    """Return total revenue across cleaned sales rows."""
    return round(sum(float(row["revenue"]) for row in rows), 2)


def average_order_value(rows: list[dict[str, Any]]) -> float:
    """Return average revenue per row/order, or zero for empty input."""
    if not rows:
        return 0.0
    return round(total_revenue(rows) / len(rows), 2)


def top_products(rows: list[dict[str, Any]], limit: int = 3) -> list[tuple[str, float]]:
    """Return products sorted by revenue, highest first."""
    if limit < 1:
        raise ValueError("limit must be at least 1")
    revenue_by_product: dict[str, float] = defaultdict(float)
    for row in rows:
        revenue_by_product[str(row["product"])] += float(row["revenue"])
    ranked = sorted(revenue_by_product.items(), key=lambda item: (-item[1], item[0]))
    return [(name, round(revenue, 2)) for name, revenue in ranked[:limit]]


def monthly_revenue(rows: list[dict[str, Any]]) -> dict[str, float]:
    """Return revenue grouped by YYYY-MM, sorted chronologically."""
    totals: dict[str, float] = defaultdict(float)
    for row in rows:
        month = str(row["date"])[:7]
        totals[month] += float(row["revenue"])
    return {month: round(totals[month], 2) for month in sorted(totals)}
