"""
Streamlit dashboard for inventory planning.

Run with: streamlit run dashboard/app.py

Reads the inventory plan created by notebooks/04_safety_stock.ipynb.
Run notebooks 01 through 04 first.
"""
import streamlit as st
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from inventory import calculate_inventory_plan

st.set_page_config(page_title="Inventory Demand Planning", layout="wide")
st.title("Inventory Demand Planning Dashboard")

PLAN_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "inventory_plan.csv")

if not os.path.exists(PLAN_PATH):
    st.warning("No inventory plan found. Run notebooks 01 through 04 first.")
else:
    plan = pd.read_csv(PLAN_PATH)

    st.subheader("Adjust Planning Assumptions")
    lead_time_days = st.slider("Lead Time (days)", 1, 30, 7)
    service_level = st.slider("Target Service Level", 0.80, 0.99, 0.95)

    results = plan.apply(
        lambda row: calculate_inventory_plan(
            row["avg_daily_demand"], row["demand_std"], lead_time_days, service_level
        ),
        axis=1,
        result_type="expand",
    )
    plan_updated = pd.concat([plan[["sku_id", "avg_daily_demand", "demand_std"]], results], axis=1)

    col1, col2 = st.columns(2)
    col1.metric("Total Safety Stock, All SKUs", f"{plan_updated['safety_stock'].sum():.0f} units")
    col2.metric("Average Reorder Point", f"{plan_updated['reorder_point'].mean():.0f} units")

    st.subheader("Safety Stock by SKU")
    st.bar_chart(plan_updated.set_index("sku_id")["safety_stock"])

    st.subheader("Full Inventory Plan")
    st.dataframe(plan_updated.round(1))
