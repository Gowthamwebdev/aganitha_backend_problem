import requests
import xml.etree.ElementTree as ET
import re

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def fetch_papers(query):
    """Fetch research papers from PubMed and extract relevant details."""
    try:
        search_url = f"{BASE_URL}esearch.fcgi?db=pubmed&term={query}&retmode=json&retmax=50"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        paper_ids = data.get("esearchresult", {}).get("idlist", [])

        if not paper_ids:
            print(f"⚠️ No papers found: {query}")
            return []

        fetch_url = f"{BASE_URL}efetch.fcgi?db=pubmed&id={','.join(paper_ids)}&retmode=xml"
        response = requests.get(fetch_url)
        response.raise_for_status()
        root = ET.fromstring(response.text)

        papers = []
        for article in root.findall(".//PubmedArticle"):
            paper_id = article.findtext(".//PMID", "N/A")
            title = article.findtext(".//ArticleTitle", "N/A")
            
            pub_date_node = article.find(".//PubDate")
            if pub_date_node is not None:
                year = pub_date_node.findtext("Year", "N/A")
                month = pub_date_node.findtext("Month", "")
                day = pub_date_node.findtext("Day", "")
                publication_date = f"{year}-{month}-{day}".strip("-")
            else:
                publication_date = "N/A"
            
            affiliations = []
            emails = []
            non_academic_authors = []
            company_affiliations = []
            for aff in article.findall(".//AffiliationInfo/Affiliation"):
                text = aff.text or ""
                affiliations.append(text)
                match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
                if match:
                    emails.append(match.group())

                if any(keyword in text.lower() for keyword in ["inc", "ltd", "gmbh", "llc", "corp", "biotech", "pharma", "company", "corporation"]):
                    company_affiliations.append(text)
                else:
                    non_academic_authors.append(text)
            
            authors = []
            for author in article.findall(".//AuthorList/Author"):
                last_name = author.findtext("LastName", "").strip()
                fore_name = author.findtext("ForeName", "").strip()
                initials = author.findtext("Initials", "").strip()
                
                if last_name and fore_name:
                    full_name = f"{fore_name} {last_name}"
                elif last_name and initials:
                    full_name = f"{initials} {last_name}"
                else:
                    full_name = last_name or "N/A"
                
                authors.append(full_name)

            authors_str = "; ".join(authors) if authors else "N/A"


            # Modify the papers.append() section to include:
            papers.append({
                "PubmedID": paper_id,
                "Title": title,
                "Publication Date": publication_date,
                "Authors": authors_str,
                "All Affiliations": "; ".join(affiliations) if affiliations else "N/A",
                "Company Affiliations": "; ".join(company_affiliations) if company_affiliations else "N/A",
                "Non-academic Authors": "; ".join(non_academic_authors) if non_academic_authors else "N/A",
                "Corresponding Author Email": "; ".join(emails) if emails else "N/A"
            })


        print(f"✅ Successfully fetched {len(papers)} papers.")
        return papers

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching papers: {e}")
        return []