# Research Paper Fetcher and Filter

## Overview

This project is a command-line tool that fetches research papers from PubMed based on a given query, filters out non-academic papers, and saves the results to a CSV file. It ensures that only academic papers are retained based on author affiliations.

## Project Structure

```
src/
│-- backend_takehome_problem/
│   │-- __init__.py           # Package initialization
│   │-- fetch_pubmed.py       # Fetch papers from PubMed API
│   │-- paper_filteration.py  # Filters papers based on affiliations
│   │-- utils.py              # Utility functions (saving CSV, etc.)
│-- main.py               # Main script to run the CLI program
│
tests/                        # Unit tests for the project
.env                           # Environment file for storing API keys
output.csv                     # Example output file
pyproject.toml                 # Dependency management using Poetry
poetry.lock                     # Poetry lock file
README.md                      # Project documentation
```

## Installation

### Prerequisites

Ensure you have Python 3.10 or higher installed.

### Steps to Install

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd backend_takehome_problem
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage

To run the program and fetch papers:

```sh
poetry run get-papers-list "machine learning"
```

### Arguments

* `query`: The search term for fetching papers (use quotes for multi-word queries).
* `-d` or `--debug`: Enable debug mode for additional logs.
* `-f <filename>` or `--file <filename>`: Specify the output CSV file name.

### Example

```sh
poetry run get-papers-list "deep learning" -f results.csv
```

## Functionality

* **Fetch Papers** : Queries PubMed and retrieves research papers.
* **Filter Papers** : Filters out non-academic papers based on author affiliations.
* **Save Data** : Saves the results to a CSV file.

## Tools and Libraries Used**Requests** ([Documentation](https://docs.python-requests.org/en/latest/)): For making API calls.

* **Pandas** ([Documentation](https://pandas.pydata.org/)): For handling and storing fetched data.
* **Poetry** ([Documentation](https://python-poetry.org/)): Dependency management.

## Error Handling

* Handles empty queries with a validation check.
* Manages API request failures using exception handling.
* Handles missing data (e.g., missing affiliations or titles) by assigning default values.
