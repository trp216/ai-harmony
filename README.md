# Sentiment Analysis with Recurrent Neural Networks (RNN) and LSTM

## Project Overview

AI Harmony is a machine learning project aimed at classifying songs into two distinct genres: Hip-Hop and Rock. By leveraging artificial intelligence and advanced data analysis techniques, this project extracts meaningful audio features and metadata to train models for accurate genre classification.

## Dataset

The datasets used for this project were the following, all sourced from Kaggle:
- [The Echo Nest](https://www.kaggle.com/datasets/veronikafilippou/echonestmetricsjson)
- [fma-rock-vs-hiphop](https://www.kaggle.com/datasets/veronikafilippou/fmarockvshiphop) 
- [Spotify - All Time Top 2000s Mega Dataset](https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset) 
- [Dataset of songs in Spotify](https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify/data) 

All this datasets were merged, resulting in a new dataset with 10878 entries, with 6129 Hip-Hop songs and 4749 Rock songs. The dataset was filtered to contain only relevant variables to this song classification problem, resulting in the following: genre_top, duration, loudness, tempo, speechiness, acousticness, danceability, valence, energy, instrumentalness, liveness.


## Models 

The following models were analyzed as solutions for this project:
- Random Forest
- Naive Bayes
- Logistic Regression
- K-Nearest Neighbors
- Decision Tree


## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

   
## License

This project is licensed under the [MIT License](LICENSE).

