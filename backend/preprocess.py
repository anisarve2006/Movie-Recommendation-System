import pandas as pd

def load_data():
    movies = pd.read_csv("data/movies.csv")
    movies.fillna("", inplace=True)  # Handle missing values
    return movies
