#!/usr/bin/env python3
"""
Fetch standards bodies data from Wikidata using SPARQL
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
import time

def query_wikidata_standards_bodies():
    """
    Query Wikidata for standards bodies (Q176799 instances)
    """
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setReturnFormat(JSON)

    # SPARQL query for standards bodies
    query = """
    SELECT ?org ?orgLabel ?acronym ?foundingYear ?country ?countryLabel ?website ?officialName
    WHERE {
      ?org wdt:P31 wd:Q176799 .  # instance of standards organization
      OPTIONAL { ?org wdt:P1813 ?acronym . }  # short name
      OPTIONAL { ?org wdt:P571 ?foundingYear . }  # inception
      OPTIONAL { ?org wdt:P17 ?country . }  # country
      OPTIONAL { ?org wdt:P856 ?website . }  # official website
      OPTIONAL { ?org wdt:P1448 ?officialName . }  # official name
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    ORDER BY ?orgLabel
    """

    print("Querying Wikidata for standards bodies...")
    sparql.setQuery(query)

    try:
        results = sparql.query().convert()
        return results["results"]["bindings"]
    except Exception as e:
        print(f"Error querying Wikidata: {e}")
        return []

def process_wikidata_results(results):
    """
    Process SPARQL results into DataFrame
    """
    data = []
    for result in results:
        row = {
            'wikidata_qid': result.get('org', {}).get('value', '').split('/')[-1],
            'org_name': result.get('orgLabel', {}).get('value', ''),
            'org_acronym': result.get('acronym', {}).get('value', ''),
            'founding_year': result.get('foundingYear', {}).get('value', ''),
            'hq_country': result.get('countryLabel', {}).get('value', ''),
            'official_url': result.get('website', {}).get('value', ''),
            'official_name': result.get('officialName', {}).get('value', ''),
        }
        data.append(row)

    df = pd.DataFrame(data)
    return df

def main():
    results = query_wikidata_standards_bodies()
    print(f"Retrieved {len(results)} standards bodies from Wikidata")

    if results:
        df = process_wikidata_results(results)
        output_path = 'data/processed/standards_bodies_wikidata.csv'
        df.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")

        # Show sample
        print("Sample:")
        print(df.head())
    else:
        print("No results retrieved")

if __name__ == "__main__":
    main()