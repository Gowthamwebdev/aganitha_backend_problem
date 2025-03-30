import re
PHARMA_KEYWORDS = [
    "pharma", "biotech", "genentech", "roche", "novartis", 
    "pfizer", "merck", "bristol", "squibb", "astrazeneca"
]

def is_pharma_company(affiliation):
    """Check if affiliation is pharmaceutical/biotech company"""
    pattern = r'\b(?:' + '|'.join(PHARMA_KEYWORDS) + r')\b'
    return bool(re.search(pattern, affiliation, re.IGNORECASE))

def filter_papers(papers):
    """Filter papers with pharma/biotech affiliations"""
    filtered_papers = []
    for paper in papers:
        affiliations = paper.get("All Affiliations", "").split("; ")
        pharma_affiliations = [aff for aff in affiliations if is_pharma_company(aff)]
        
        if pharma_affiliations:
            # Get authors associated with these affiliations
            all_authors = paper.get("Authors", "").split("; ")
            non_academic_authors = []
            
            # This is simplified - would need proper author-affiliation mapping
            if pharma_affiliations:
                non_academic_authors = all_authors
            
            filtered_paper = {
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(pharma_affiliations),
                "Corresponding Author Email": paper["Corresponding Author Email"]
            }
            filtered_papers.append(filtered_paper)
    
    print(f"✅ Found {len(filtered_papers)} industry-affiliated papers.")
    return filtered_papers