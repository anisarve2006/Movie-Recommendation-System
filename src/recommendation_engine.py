# src/recommendation_engine.py

import pandas as pd

def load_data(path="data/movies.csv"):
    """
    Load the movies dataset from the given path.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise Exception(f"File not found at {path}. Ensure the movies.csv file is in the data folder.")
    return df

def filter_by_genre(df, genre):
    """
    Filter movies that match the selected genre.
    Assumes the 'genre' column contains comma-separated genres.
    """
    # Use str.contains to match the genre (ignoring case)
    filtered = df[df['genre'].str.contains(genre, case=False, na=False)]
    return filtered

def recommend_movies(interest, df):
    """
    Recommend movies based on the selected interest.
    In this basic example, we assume 'interest' is a genre.
    Returns the top 10 movies matching the interest.
    """
    recommendations = filter_by_genre(df, interest)
    return recommendations.head(10)
