import React from "react";
import "./MovieCard.css"; // New CSS file for styling

function MovieCard({ movie }) {
  return (
    <div className="movie-card">
      <div className="movie-details">
        <h2>{movie.title}</h2>
        <p className="movie-genre">{movie.genres}</p>
        <p className="movie-overview">{movie.overview.substring(0, 100)}...</p>
      </div>
    </div>
  );
}

export default MovieCard;
