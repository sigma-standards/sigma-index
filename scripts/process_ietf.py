#!/usr/bin/env python3
"""
Fetch IETF RFC metadata and process into SIGMA format
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import requests
import xml.etree.ElementTree as ET
from data_processing import map_iso_to_sigma_schema

def fetch_rfc_index():
    """
    Fetch RFC index from IETF
    """
    url = "https://www.rfc-editor.org/rfc/rfc-index.xml"
    print(f"Fetching RFC index from {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching RFC index: {e}")
        return None

def process_rfc_data(xml_data):
    """
    Process RFC XML data into DataFrame
    """
    root = ET.fromstring(xml_data)
    rfcs = []

    # Find all RFC entries
    for rfc_entry in root.findall('.//{https://www.rfc-editor.org/rfc-index}rfc-entry'):
        rfc = {}

        # Extract basic fields
        doc_id = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}doc-id')
        if doc_id is not None:
            rfc['number'] = doc_id.text.replace('RFC', '')

        title = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}title')
        if title is not None:
            rfc['title'] = title.text

        # Extract authors
        authors = []
        for author in rfc_entry.findall('.//{https://www.rfc-editor.org/rfc-index}author'):
            name_elem = author.find('.//{https://www.rfc-editor.org/rfc-index}name')
            if name_elem is not None:
                authors.append(name_elem.text)
        rfc['authors'] = authors

        # Extract date
        date_elem = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}date')
        if date_elem is not None:
            month = date_elem.find('.//{https://www.rfc-editor.org/rfc-index}month')
            year = date_elem.find('.//{https://www.rfc-editor.org/rfc-index}year')
            if month is not None and year is not None:
                rfc['date'] = f"{month.text} {year.text}"

        # Extract status (current-status)
        status = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}current-status')
        if status is not None:
            rfc['status'] = status.text
        else:
            rfc['status'] = 'RFC'  # Default to RFC if not specified

        # Extract DOI if available
        doi = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}doi')
        if doi is not None:
            rfc['doi'] = doi.text

        # Extract stream
        stream = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}stream')
        if stream is not None:
            rfc['stream'] = stream.text

        # Extract working group
        wg = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}wg')
        if wg is not None:
            rfc['wg'] = wg.text

        # Extract pages
        pages = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}page-count')
        if pages is not None:
            rfc['pages'] = pages.text

        # Extract abstract
        abstract = rfc_entry.find('.//{https://www.rfc-editor.org/rfc-index}abstract')
        if abstract is not None:
            rfc['abstract'] = abstract.text

        rfcs.append(rfc)

    df = pd.DataFrame(rfcs)
    return df

def map_rfc_to_sigma(df):
    """
    Map RFC data to SIGMA schema
    """
    sigma_df = pd.DataFrame(index=df.index)

    # Basic mappings
    sigma_df['entry_type'] = 'Standard'
    sigma_df['meta_layer'] = 'L5 Technology & Infrastructure'
    sigma_df['issuer'] = 'IETF'
    sigma_df['issuer_type'] = 'Industry SDO'
    sigma_df['governance_layer'] = 'International'
    sigma_df['geographic_scope'] = 'Global'
    sigma_df['status'] = df['status'].apply(lambda x: 'Active' if x == 'RFC' else 'Superseded')
    sigma_df['mandate'] = 'Voluntary'
    sigma_df['sector_applicability'] = 'Internet and networking technologies'

    # Direct mappings
    sigma_df['standard_id'] = 'RFC ' + df['number'].astype(str)
    sigma_df['name_full'] = df['title']
    sigma_df['name_short'] = sigma_df['standard_id']
    sigma_df['year_published'] = pd.to_datetime(df['date'], errors='coerce').dt.year
    sigma_df['year_first'] = sigma_df['year_published']
    sigma_df['domain'] = 'Information Technology'
    sigma_df['sub_domain'] = 'Internet Standards'

    # Generate SIGMA IDs
    sigma_df['sigma_id'] = 'DG-IETF-RFC' + df['number'].astype(str) + '-' + sigma_df['year_published'].astype(str)

    # Additional fields
    sigma_df['why_it_matters'] = 'Core internet protocol standard'
    sigma_df['key_outputs'] = sigma_df['standard_id']
    sigma_df['official_url'] = 'https://www.rfc-editor.org/rfc/rfc' + df['number'].astype(str) + '.html'
    sigma_df['data_source'] = 'IETF RFC Editor'
    sigma_df['notes'] = df['abstract'].fillna('').str[:200].apply(lambda x: x + '...' if len(x) > 200 else x)

    return sigma_df

def main():
    rfc_data = fetch_rfc_index()
    if not rfc_data:
        return

    df = process_rfc_data(rfc_data)
    print(f"Processed {len(df)} RFCs")

    sigma_df = map_rfc_to_sigma(df)
    output_path = 'data/processed/ietf_rfcs.csv'
    sigma_df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")

    # Show sample
    print("Sample:")
    print(sigma_df[['sigma_id', 'name_full', 'year_published']].head())

if __name__ == "__main__":
    main()
