import pandas as pd

def is_academic(affiliation):
    academic_keywords = [
        "university", "college", "iit", "iiit", "nit", "institute", "aiims", "bits"
    ]
    return any(word in affiliation.lower() for word in academic_keywords)

def is_academic_only(row):
    affils = [a.strip() for a in row["affiliations"].split(",")]
    return all(is_academic(a) for a in affils)

df = pd.read_csv("input_papers.csv")
filtered_df = df[~df.apply(is_academic_only, axis=1)]
filtered_df.to_csv("filtered_papers.csv", index=False)
