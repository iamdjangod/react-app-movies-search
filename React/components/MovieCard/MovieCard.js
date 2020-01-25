import React from 'react';

import './MovieCard.css';

const MovieCard = (props) => {
    return (
        <div className="container">
            <div className="movie-card">
                <div className="movie-header" style={{ backgroundImage: `url(${props.movie.Poster})` }}>
                </div>
                <div className="movie-content">
                    <div className="movie-content-header">
                        <h3 className="movie-title">{props.movie.Title}</h3>
                    </div>
                    <div className="movie-info">
                        <div className="info-section">
                            <label>Released</label>
                            <span>{props.movie.Released}</span>
                        </div>
                        <div className="info-section">
                            <label>IMDB Rating</label>
                            <span>{props.movie.imdbRating}</span>
                        </div>
                        <div className="info-section">
                            <label>Rated</label>
                            <span>{props.movie.Rated}</span>
                        </div>
                        <div className="info-section">
                            <label>Runtime</label>
                            <span>{props.movie.Runtime}</span>
                        </div>
                    </div>
                    <div className="plot" style={{fontSize: '12px'}}>
                        <p>{props.movie.Plot}</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MovieCard;