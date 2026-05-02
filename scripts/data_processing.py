#!/usr/bin/env python3
"""
Data Processing Scripts for SIGMA Index

This module contains utilities for processing and cleaning data sources.
"""

import pandas as pd
import re
from pathlib import Path
from typing import Optional

def fix_csv_quotes(file_path: str, output_path: Optional[str] = None) -> pd.DataFrame:
    """
    Fix malformed CSV with nested quotes.

    Args:
        file_path: Path to the CSV file
        output_path: Optional path to save fixed CSV

    Returns:
        Cleaned DataFrame
    """
    # Read and fix line by line
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        # Fix specific quote issues
        line = line.replace('dits "gaz"', 'dits ""gaz""')
        # Add more fixes as needed for other malformed quotes
        fixed_lines.append(line)

    # Write fixed version
    fixed_path = file_path.replace('.csv', '_fixed.csv')
    with open(fixed_path, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)

    # Load with pandas
    df = pd.read_csv(fixed_path)

    # Clean up fixed file unless output_path specified
    if not output_path:
        Path(fixed_path).unlink()
    elif output_path != fixed_path:
        df.to_csv(output_path, index=False)
        Path(fixed_path).unlink()

    return df

def map_iso_to_sigma_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Map ISO metadata to SIGMA schema.

    Args:
        df: ISO DataFrame

    Returns:
        DataFrame with SIGMA schema
    """
    sigma_df = pd.DataFrame(index=df.index)

    # Basic mappings
    sigma_df['entry_type'] = 'Standard'
    sigma_df['meta_layer'] = 'L5 Technology & Infrastructure'  # Most ISO are tech
    sigma_df['issuer'] = 'ISO'
    sigma_df['issuer_type'] = 'ISO'
    sigma_df['governance_layer'] = 'International'
    sigma_df['geographic_scope'] = 'Global — 175 ISO member countries'
    sigma_df['status'] = df['currentStage'].apply(lambda x: 'Active' if pd.isna(x) or 'Published' in str(x) else 'Under Development')
    sigma_df['mandate'] = 'Voluntary'
    sigma_df['sector_applicability'] = 'Various sectors'

    # Direct field mappings
    field_mappings = {
        'reference': 'standard_id',
        'title.en': 'name_full',
        'title.fr': 'name_short',
        'publicationDate': 'year_published',
        'edition': 'key_outputs',
        'icsCode': 'domain',
        'ownerCommittee': 'issuer',
    }

    for iso_field, sigma_field in field_mappings.items():
        if iso_field in df.columns:
            sigma_df[sigma_field] = df[iso_field]

    if 'name_full' in sigma_df.columns:
        sigma_df['name_full'] = sigma_df['name_full'].fillna('')
        fallback_title = sigma_df.get('name_short', pd.Series('', index=df.index)).fillna('')
        fallback_id = sigma_df.get('standard_id', pd.Series('', index=df.index)).fillna('')
        sigma_df['name_full'] = sigma_df['name_full'].where(
            sigma_df['name_full'].astype(str).str.strip().ne(''),
            fallback_title.where(fallback_title.astype(str).str.strip().ne(''), fallback_id),
        )

    # Extract year from publication date
    years = pd.to_datetime(sigma_df['year_published'], errors='coerce').dt.year
    sigma_df['year_published'] = years.astype('Int64').astype(str).replace('<NA>', '')
    sigma_df['year_first'] = sigma_df['year_published']  # Assume same for now

    # Generate SIGMA IDs
    sigma_df['sigma_id'] = sigma_df.apply(generate_sigma_id, axis=1)

    # Map ICS codes to domains (simplified)
    ics_to_domain = {
        '01': 'Generalities',
        '03': 'Services',
        '07': 'Natural Sciences',
        '11': 'Health Technology',
        '13': 'Environment',
        '17': 'Metrology',
        '19': 'Testing',
        '21': 'Mechanical Systems',
        '23': 'Fluid Systems',
        '25': 'Manufacturing',
        '27': 'Energy',
        '29': 'Electrical Engineering',
        '31': 'Electronics',
        '33': 'Telecommunications',
        '35': 'Information Technology',
        '37': 'Image Technology',
        '39': 'Precision Mechanics',
        '43': 'Road Vehicles',
        '45': 'Railway Engineering',
        '47': 'Shipbuilding',
        '49': 'Aircraft',
        '53': 'Materials',
        '55': 'Packaging',
        '59': 'Textiles',
        '61': 'Clothing Industry',
        '65': 'Agriculture',
        '67': 'Food Technology',
        '71': 'Chemical Technology',
        '73': 'Mining',
        '75': 'Petroleum',
        '77': 'Metallurgy',
        '79': 'Wood Technology',
        '81': 'Glass',
        '83': 'Rubber',
        '85': 'Paper Technology',
        '87': 'Paint',
        '91': 'Construction',
        '93': 'Civil Engineering',
        '95': 'Military Engineering',
        '97': 'Domestic',
    }

    def map_ics_to_domain(ics_code):
        if pd.isna(ics_code):
            return 'Technology'
        code = str(ics_code).split('.')[0]
        return ics_to_domain.get(code, 'Technology')

    sigma_df['domain'] = sigma_df['domain'].apply(map_ics_to_domain)
    sigma_df['sub_domain'] = 'Various'  # Placeholder

    # Add remaining required fields
    sigma_df['why_it_matters'] = 'ISO International Standard for global harmonization'
    sigma_df['key_outputs'] = sigma_df.get('key_outputs', pd.Series('', index=df.index)).fillna('')
    sigma_df['official_url'] = 'https://www.iso.org/standard/' + df['id'].astype(str)
    sigma_df['data_source'] = 'ISO Open Data CSV'
    sigma_df['notes'] = df.get('scope.en', '')

    return sigma_df

def generate_sigma_id(row) -> str:
    """
    Generate SIGMA ID from row data.

    Format: [DOMAIN_CODE]-[ISSUER_CODE]-[STD_NUMBER]-[YEAR]
    """
    # Simplified mapping - in practice would need proper domain codes
    domain_code = 'TECH'  # Placeholder
    issuer_code = 'ISO'
    std_number = str(row.get('standard_id') or row.get('reference') or row.get('id') or '00000')
    std_number = re.sub(r'[^A-Za-z0-9]+', '-', std_number).strip('-').upper()
    if not std_number:
        std_number = '00000'
    year = str(row.get('year_published', '0000'))
    if pd.isna(year):
        year = '0000'
    year = str(int(float(year)) if year.replace('.', '').isdigit() else '0000')[:4]

    return f"{domain_code}-{issuer_code}-{std_number}-{year}"

if __name__ == "__main__":
    # Test the functions
    pass
