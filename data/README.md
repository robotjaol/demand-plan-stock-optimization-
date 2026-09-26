# Data

## Sample Data (used by default)

Notebook `01_generate_data.ipynb` creates `data/raw/sku_sales.csv` on its
own. No download needed to run this project.

## Real Dataset (optional upgrade)

**M5 Forecasting - Accuracy**
- Source: Kaggle Competition (Walmart)
- Link: https://www.kaggle.com/competitions/m5-forecasting-accuracy/data
- Daily sales history for about 30,000 SKUs across 10 stores, plus price
  and calendar event data.

The real M5 files come in a wide format, one column per day. Reshape them
to the long format used here: one row per date, sku_id, category, and
units_sold. Save the result as `data/raw/sku_sales.csv`, then run
notebooks 02 through 04 as usual.
