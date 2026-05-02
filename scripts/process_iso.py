#!/usr/bin/env python3
"""
Process ISO Open Data for SIGMA Index
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from data_processing import fix_csv_quotes, map_iso_to_sigma_schema
from pathlib import Path

def process_iso_deliverables():
    """Process ISO deliverables metadata into SIGMA format."""
    print("Loading ISO deliverables data...")
    df = fix_csv_quotes('data/raw/iso/iso_deliverables_metadata.csv')

    print(f"Loaded {len(df)} ISO standards")

    # Filter to published standards only
    published = df[df['deliverableType'].isin(['IS', 'TS', 'TR'])]  # International Standards, Technical Specs, Technical Reports
    print(f"Filtered to {len(published)} published deliverables")

    # Map to SIGMA schema
    sigma_df = map_iso_to_sigma_schema(published)

    # Save processed data
    output_path = 'data/processed/iso_all.csv'
    sigma_df.to_csv(output_path, index=False)
    print(f"Saved {len(sigma_df)} entries to {output_path}")

    return sigma_df

if __name__ == "__main__":
    process_iso_deliverables()