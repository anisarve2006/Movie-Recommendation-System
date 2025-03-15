import pandas as pd
import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_df = preprocess.load_data()

def recommend_movies(user_input):
    tfidf = TfidfVectorizer(stop_words='english')
    movie_matrix = tfidf.fit_transform(movies_df['genres'] + " " + movies_df['keywords'])

    input_vec = tfidf.transform([user_input])
    similarity = cosine_similarity(input_vec, movie_matrix)

    movies_df['similarity'] = similarity[0]
    recommended = movies_df.sort_values(by="similarity", ascending=False).head(10)
    
    return recommended[['title', 'overview', 'genres']].to_dict(orient='records')
