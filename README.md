# Inventory Demand Planning and Safety Stock Optimization

An end to end project that forecasts demand per SKU and calculates how
much safety stock and reorder point each one needs. Built as a portfolio
project for an MT GNT DHL Supply Chain application.

## Business Problem

Too much stock ties up cash and warehouse space. Too little stock causes
stockouts and lost sales. Good inventory planning needs an accurate demand
forecast per SKU, combined with a safety stock buffer that accounts for
how unpredictable that demand is.

## How This Project Works

The notebooks run in order and do not require any external download:

1. `01_generate_data.ipynb` creates daily sales data for 20 SKUs across
   4 categories, similar in structure to the M5 Forecasting dataset.
2. `02_eda.ipynb` explores demand patterns and variability by category.
3. `03_demand_forecast.ipynb` forecasts demand per SKU using LightGBM.
4. `04_safety_stock.ipynb` calculates safety stock and reorder point from
   the forecast results.

To use a real dataset instead, download the M5 Forecasting dataset from
Kaggle and reshape it to match the columns used here (see `data/README.md`).

## SMART Goals

| Criteria | Target |
|---|---|
| Specific | Forecast demand per SKU, then calculate safety stock and reorder point |
| Measurable | WMAPE under 20 percent on the forecast holdout, safety stock sized for a 95 percent service level |
| Achievable | Notebooks run end to end on generated data, real dataset can be swapped in later |
| Relevant | Maps directly to inventory turnover, stockout rate, and holding cost |
| Time-bound | 4 to 5 weeks part time |

## Project Structure

```
inventory-demand-planning/
  data/            sample data and instructions for the real dataset
  notebooks/       the four notebooks listed above
  src/             the safety stock formulas used by the dashboard
  dashboard/       a Streamlit app for planning
  docs/            resource list and timeline
```

## How to Run

1. `pip install -r requirements.txt`
2. Run the notebooks in order, 01 through 04.
3. Start the dashboard: `streamlit run dashboard/app.py`

## Notes for the Interview

Frame this project around the trade off between holding cost and stockout
risk: how much stock does the business need to hold to hit a target
service level, without holding more than necessary.
