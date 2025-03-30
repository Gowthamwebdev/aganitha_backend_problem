import pandas as pd

def save_to_csv(papers, filename):
    """Save filtered papers to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"📁 Data saved to {filename}")
