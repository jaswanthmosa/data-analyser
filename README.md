# Python Sales Data Analyzer

A small, interview-friendly Python project that reads sales from CSV, validates and cleans rows, and prints useful sales summaries. It uses only the Python standard library, so no external packages are required.

## Features

- Read sales records from a CSV file.
- Validate dates, quantities, prices, product names, and order IDs.
- Skip malformed rows and duplicate order IDs.
- Calculate total revenue and average order value.
- Show top products by revenue.
- Group revenue by month.
- Include unit tests for core functions.

## Project structure

```text
python-live-interview-demo/
├── data/
│   └── sample_sales.csv
├── sales_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements

- Python 3.10 or newer
- No third-party libraries

## Run the project

Open a terminal in the project folder and run:

```bash
python -m sales_analyzer.cli
```

To use another CSV file:

```bash
python -m sales_analyzer.cli path/to/your_sales.csv
```

To show the top five products:

```bash
python -m sales_analyzer.cli --top 5
```

The CSV must contain these columns: `order_id`, `date` (YYYY-MM-DD), `product`, `quantity`, and `unit_price`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Example output

The sample file intentionally includes duplicate and invalid rows so you can demonstrate data cleaning. The program skips those rows and summarizes the valid sales.

## Live-interview feature ideas

Practise adding one feature at a time:

1. Add `product_revenue(rows, product_name)` to report revenue for one product.
2. Add a `--month YYYY-MM` command-line option.
3. Export the cleaned rows to a new CSV file.
4. Add a minimum-revenue filter for top products.
5. Add a test for empty input or a missing CSV file.

## Design notes

- `analyzer.py` contains the business logic.
- `cli.py` handles command-line arguments and output.
- `tests/` checks the main functions.
- Revenue is calculated as `quantity * unit_price` for each valid row.
- For this demo, `order_id` is treated as unique, so duplicate IDs are skipped.

## Be ready to explain

- Why invalid rows are skipped instead of crashing the whole analysis.
- Why a `set` is used to detect duplicate order IDs.
- Why `defaultdict` is useful for grouping revenue.
- The time complexity of grouping sales: approximately O(n), plus sorting for ranked products.
- How you would add a feature and write a test for it.

## Important

This is a starter demo project generated for practice. Before presenting it as your own work, run it, understand each function, make at least one meaningful change yourself, and be truthful about how it was created. You should be able to explain and modify every part during the interview.
