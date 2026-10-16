"""Small, interview-friendly sales analysis package."""

from .analyzer import (
    load_sales,
    clean_sales,
    total_revenue,
    average_order_value,
    top_products,
    monthly_revenue,
)

__all__ = [
    "load_sales", "clean_sales", "total_revenue", "average_order_value",
    "top_products", "monthly_revenue",
]
