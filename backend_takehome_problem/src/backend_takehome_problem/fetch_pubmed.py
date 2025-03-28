import requests
import pandas as pd
import argparse

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

import requests
import urllib.parse  # Needed for encoding complex queries

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query: str):
    """Fetch papers from PubMed API based on a complex query."""
    encoded_query = urllib.parse.quote_plus(query)  # Encode query properly

    params = {
        "db": "pubmed",
        "term": encoded_query,  # Pass encoded query
        "retmode": "json",
        "retmax": 50
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids):
    """Fetch detailed metadata for given paper IDs."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(DETAILS_URL, params=params)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch details")
    
    data = response.json()
    result = []
    
    for paper_id in paper_ids:
        paper_data = data["result"].get(paper_id, {})
        result.append({
            "PubmedID": paper_id,
            "Title": paper_data.get("title", "N/A"),
            "Publication Date": paper_data.get("pubdate", "N/A"),
        })
    
    return result

