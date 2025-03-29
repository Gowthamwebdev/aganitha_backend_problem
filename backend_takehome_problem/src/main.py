import argparse
import sys
import os
import requests
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend_takehome_problem.fetch_pubmed import fetch_papers
from backend_takehome_problem.utils import save_to_csv
from backend_takehome_problem.paper_filteration import filter_papers 

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter research papers from PubMed.")
    parser.add_argument("query", nargs="+", help="Search query (use quotes for multi-word queries)")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default="papers.csv")
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    if not query:
        print("❌ Error: Search query cannot be empty.")
        sys.exit(1)

    print(f"🔍 Searching for papers with query: '{query}'...")
    papers = fetch_papers(query)
    if not papers:
        print("⚠️ No papers found.")
        sys.exit(0)

    print("📝 Filtering non-academic papers...")
    filtered_papers = filter_papers(papers)
    if not filtered_papers:
        print("⚠️ No non-academic papers found.")
        sys.exit(0)

    save_to_csv(filtered_papers, args.file)
    print(f"✅ Filtered papers saved successfully to {args.file}.")

if __name__ == "__main__":
    main()