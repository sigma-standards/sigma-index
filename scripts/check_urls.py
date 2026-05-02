#!/usr/bin/env python3
"""
URL Health Check Script for SIGMA Index

Checks the validity of URLs in the SIGMA dataset.
"""

import pandas as pd
import requests
import time
import sys
from pathlib import Path

def check_url(url, timeout=10):
    """Check if a URL is accessible."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    # Find data files
    data_dir = Path(__file__).parent.parent / "data" / "processed"
    if not data_dir.exists():
        print("No processed data directory found.")
        return

    # Look for CSV files
    csv_files = list(data_dir.glob("*.csv"))
    if not csv_files:
        print("No CSV files found in processed data.")
        return

    for csv_file in csv_files:
        print(f"Checking URLs in {csv_file.name}")
        try:
            df = pd.read_csv(csv_file)
            if 'official_url' not in df.columns:
                continue

            broken_urls = []
            for idx, row in df.iterrows():
                url = row['official_url']
                if pd.isna(url) or not url.startswith('http'):
                    continue

                if not check_url(url):
                    broken_urls.append((row.get('sigma_id', f'row {idx}'), url))

                # Rate limiting
                time.sleep(0.1)

            if broken_urls:
                print(f"Broken URLs in {csv_file.name}:")
                for sid, url in broken_urls:
                    print(f"  {sid}: {url}")
            else:
                print(f"All URLs in {csv_file.name} are accessible.")

        except Exception as e:
            print(f"Error processing {csv_file.name}: {e}")

if __name__ == "__main__":
    main()