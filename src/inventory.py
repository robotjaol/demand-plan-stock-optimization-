"""
Safety stock and reorder point calculations.

Kept separate from the notebooks so the dashboard can reuse the same
formulas without copying code.
"""
from scipy.stats import norm
import numpy as np


def calculate_safety_stock(demand_std, lead_time_days, service_level=0.95):
    """Extra stock to cover demand swings during lead time."""
    z_score = norm.ppf(service_level)
    return z_score * demand_std * np.sqrt(lead_time_days)


def calculate_reorder_point(avg_daily_demand, lead_time_days, safety_stock):
    """Stock level that should trigger a new order."""
    return avg_daily_demand * lead_time_days + safety_stock


def calculate_inventory_plan(avg_daily_demand, demand_std, lead_time_days, service_level=0.95):
    """Return both safety stock and reorder point together."""
    safety_stock = calculate_safety_stock(demand_std, lead_time_days, service_level)
    reorder_point = calculate_reorder_point(avg_daily_demand, lead_time_days, safety_stock)
    return {
        "safety_stock": safety_stock,
        "reorder_point": reorder_point,
    }
