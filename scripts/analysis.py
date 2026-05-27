#!/usr/bin/env python3
"""
Sales Analysis Module

This module performs:
- Revenue analysis
- Regional performance analysis
- Trend analysis
- Statistical analysis
"""

import pandas as pd
import numpy as np
from data_processing import DataProcessor

class SalesAnalyzer:
    def __init__(self, df):
        """Initialize the SalesAnalyzer with a DataFrame."""
        self.df = df
    
    def regional_analysis(self, region_column, revenue_column):
        """Analyze sales by region."""
        regional_stats = self.df.groupby(region_column)[revenue_column].agg([
            ('total_revenue', 'sum'),
            ('avg_revenue', 'mean'),
            ('transaction_count', 'count')
        ]).sort_values('total_revenue', ascending=False)
        
        return regional_stats
    
    def top_performers(self, region_column, revenue_column, top_n=5):
        """Get top performing regions."""
        return self.df.nlargest(top_n, revenue_column)[[region_column, revenue_column]]
    
    def revenue_trend(self, date_column, revenue_column):
        """Analyze revenue trends over time."""
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        trend = self.df.groupby(self.df[date_column].dt.to_period('M'))[revenue_column].sum()
        
        return trend


if __name__ == "__main__":
    print("Sales Analysis Module loaded successfully!")
