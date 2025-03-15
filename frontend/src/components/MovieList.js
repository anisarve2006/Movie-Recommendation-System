import React from "react";
import MovieCard from "./MovieCard";
import "./MovieList.css"; // New CSS file for styling

function MovieList({ movies }) {
  return (
    <div className="movie-list-container">
      {movies.length === 0 ? (
        <p>No movies found.</p>
      ) : (
        movies.map((movie, index) => <MovieCard key={index} movie={movie} />)
      )}
    </div>
  );
}

export default MovieList;
