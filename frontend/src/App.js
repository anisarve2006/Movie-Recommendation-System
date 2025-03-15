import React, { useState } from "react";
import axios from "axios";
import MovieList from "./components/MovieList";
import SearchBar from "./components/SearchBar";

function App() {
  const [movies, setMovies] = useState([]);

  const fetchRecommendations = (interests) => {
    axios.post("http://127.0.0.1:5000/recommend", { interests })
      .then(response => setMovies(response.data.movies))
      .catch(error => console.error("Error fetching recommendations", error));
  };

  return (
    <div>
      <h1>Movie Recommendation System</h1>
      <SearchBar onSearch={fetchRecommendations} />
      <MovieList movies={movies} />
    </div>
  );
}

export default App;
