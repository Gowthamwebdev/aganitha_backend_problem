import pandas as pd

def save_to_csv(data, filename="papers.csv"):
    """Save fetched papers to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved to {filename}")
