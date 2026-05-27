#!/usr/bin/env python3
"""
Data Processing Module for Sales Analysis

This module handles:
- Loading raw data
- Data cleaning
- Data transformation
- Data validation
"""

import pandas as pd
import numpy as np
from pathlib import Path

class DataProcessor:
    def __init__(self, data_path):
        """Initialize the DataProcessor."""
        self.data_path = Path(data_path)
    
    def load_data(self, filename):
        """Load data from CSV or Excel file."""
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(self.data_path / filename)
            elif filename.endswith('.xlsx'):
                df = pd.read_excel(self.data_path / filename)
            else:
                raise ValueError(f"Unsupported file format: {filename}")
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def clean_data(self, df):
        """Clean the dataset."""
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.dropna()
        
        return df
    
    def get_data_summary(self, df):
        """Get summary statistics of the data."""
        return df.describe()


if __name__ == "__main__":
    processor = DataProcessor('data/raw')
    print("Data Processing Module loaded successfully!")
