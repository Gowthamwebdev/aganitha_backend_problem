import argparse
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend_takehome_problem.fetch_pubmed import fetch_papers, fetch_paper_details
from backend_takehome_problem.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default="papers.csv")
    args = parser.parse_args()

    print("Fetching papers...")
    paper_ids = fetch_papers(args.query)
    
    if not paper_ids:
        print("No papers found.")
        exit(0)

    print("Fetching paper details...")
    paper_details = fetch_paper_details(paper_ids)

    save_to_csv(paper_details, args.file)
    print("Done.")

if __name__ == "__main__":
    main()