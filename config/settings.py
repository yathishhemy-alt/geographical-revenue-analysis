#!/usr/bin/env python3
"""
Configuration settings for Sales Analysis project
"""

import os
from pathlib import Path

# Project directories
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
SCRIPTS_DIR = PROJECT_ROOT / 'scripts'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
RESULTS_DIR = PROJECT_ROOT / 'results'
DASHBOARDS_DIR = PROJECT_ROOT / 'dashboards'

# Analysis settings
TOP_N_REGIONS = 5
MIN_REVENUE_THRESHOLD = 1000
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Visualization settings
FIGURE_SIZE = (12, 6)
COLOR_PALETTE = 'husl'
DPI = 300

# Data processing
DROP_DUPLICATES = True
FILL_MISSING_VALUES = False
HANDLE_OUTLIERS = True
