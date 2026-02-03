import re
from pathlib import Path
import bibtexparser

BIB_FILE = "_publications/publications.bib"
OUT_DIR = Path("_publications")
OUT_DIR.mkdir(exist_ok=True)

MONTH_MAP = {
    "jan": "01", "january": "01",
    "feb": "02", "february": "02",
    "mar": "03", "march": "03",
    "apr": "04", "april": "04",
    "may": "05",
    "jun": "06", "june": "06",
    "jul": "07", "july": "07",
    "aug": "08", "august": "08",
    "sep": "09", "september": "09",
    "oct": "10", "october": "10",
    "nov": "11", "november": "11",
    "dec": "12", "december": "12",
}

def clean_braces(s: str) -> str:
    return s.replace("{", "").replace("}", "").strip()

def slugify(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^A-Za-z0-9\-]", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.lower().strip("-")

def format_authors(bib_author: str) -> str:
    """
    BibTeX authors: 'Last, First and Last2, First2 ...' or 'First Last and ...'
    Return a simple 'First Last, First2 Last2, ...'
    """
    if not bib_author:
        return ""
    parts = [a.strip() for a in bib_author.split(" and ") if a.strip()]
    names = []
    for a in parts:
        if "," in a:
            last, first = [x.strip() for x in a.split(",", 1)]
            names.append(f"{first} {last}".strip())
        else:
            names.append(a)
    return ", ".join(names)

def pick_venue(e: dict) -> str:
    return clean_braces(e.get("journal") or e.get("booktitle") or e.get("publisher") or "")

def pick_date(year: str, month: str) -> str:
    if not year:
        return "0000-01-01"
    mm = "01"
    if month:
        m = clean_braces(month).lower()
        mm = MONTH_MAP.get(m, mm)
    return f"{year}-{mm}-01"

def pick_paper_url(e: dict) -> str:
    url = e.get("url", "").strip()
    if url:
        return url
    doi = e.get("doi", "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    return ""

def short_citation(e: dict, authors_str: str, year: str, title: str, venue: str) -> str:
    # Simple: "Authors. Title. Venue, Year."
    a = authors_str if authors_str else "Unknown authors"
    v = venue if venue else ""
    y = year if year else ""
    pieces = [a + ".", title + "."]
    if v:
        pieces.append(v + ",")
    if y:
        pieces.append(y + ".")
    return " ".join(pieces).replace(" ,", ",")

with open(BIB_FILE, encoding="utf-8") as f:
    db = bibtexparser.load(f)

for e in db.entries:
    key = e.get("ID", "paper")
    year = clean_braces(e.get("year", "0000"))
    month = e.get("month", "")
    date = pick_date(year, month)

    title = clean_braces(e.get("title", "Untitled"))
    authors = clean_braces(format_authors(e.get("author", "")))
    venue = pick_venue(e)
    paperurl = pick_paper_url(e)

    citation = clean_braces(short_citation(e, authors, year, title, venue))

    # academicpages often uses filename YYYY-MM-DD-something.md
    filename = f"{date}-{slugify(key)}.md"
    path = OUT_DIR / filename

    md = f"""---
title: "{title}"
collection: publications
permalink: /publication/{date}-{slugify(key)}/
date: {date}
year: {year}
venue: "{venue}"
authors: "{authors}"
paperurl: "{paperurl}"
citation: "{citation}"
---

"""
    path.write_text(md, encoding="utf-8")
    print(f"Generated {path}")