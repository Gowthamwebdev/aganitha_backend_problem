import re

NON_ACADEMIC_KEYWORDS = [
    "inc", "ltd", "corp", "biotech", "pharma", "technologies", 
    "llc", "gmbh", "solutions", "systems", "research lab", "company"
]
def is_non_academic(affiliation):
    """Check if the affiliation is non-academic based on keywords."""
    if not affiliation or affiliation == "N/A":
        return False
    pattern = r'\b(?:' + '|'.join(NON_ACADEMIC_KEYWORDS) + r')\b'
    return bool(re.search(pattern, affiliation, re.IGNORECASE))

def filter_papers(papers):
    """Filter papers based on non-academic affiliations."""
    filtered_papers = []
    for paper in papers:
        affiliations = paper.get("Affiliations", "N/A").split("; ")
        non_academic_affiliations = [aff for aff in affiliations if is_non_academic(aff)]
        
        if non_academic_affiliations:
            paper["Non-Academic Affiliations"] = "; ".join(non_academic_affiliations)
            filtered_papers.append(paper)
    
    print(f"✅ Found {len(filtered_papers)} non-academic papers.")
    return filtered_papers