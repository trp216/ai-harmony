# Sentiment Analysis with Recurrent Neural Networks (RNN) and LSTM

## Project Overview

This project aims to build a sentiment analysis model using supervised learning techniques with vanilla Recurrent Neural Networks (RNN) and Long Short-Term Memory networks (LSTM). The goal is to classify sentences as positive (labeled as 1) or negative (labeled as 0) based on their sentiment.

## Dataset

The dataset used for this project is the "Sentiment Labelled Sentences Dataset" sourced from the UC Irvine Machine Learning Repository. The dataset comprises sentences from three different websites: amazon.com, imdb.com, and yelp.com. Each website contributes 500 positive and 500 negative sentences, making a total of 3000 labeled sentences for analysis. The dataset was originally curated for the paper 'From Group to Individual Labels using Deep Features' by Kotzias et al., KDD 2015.

**Dataset Link:** [Sentiment Labelled Sentences Data Set](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences)

## Features

- Tokenization of sentences
- Lowercasing of text
- Removal of stopwords using NLTK
- Implementation of DummyClassifier as a baseline model
- Vanilla RNN and LSTM sentiment analysis models
- Hyperparameter tuning using GridSearchCV
- Enhanced sentiment analysis model using Turing neural networks 

  ## Installation

To set up the Interactive Dungeons & Dragons Story Generator on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/trp216/sentAIment-analysis.git`
2. Navigate to the project directory: `cd sentAIment-analysis`
3. Install the required dependencies:

```
pip install keras
pip install scikeras
```
If you are running the project for the first time, you will have to install nltk by [using pip](https://www.nltk.org/install.html) or uncomment the line 
```
#nltk.download('all')    # run just once
```
in the dependencies installation section of the notebook.

You will also need to install Tensorflow: [Install Tensorflow with pip](https://www.tensorflow.org/install/pip)

Note: this project was made using Python 3.11.4.

## Usage

1. Load the sentiment analysis dataset.
2. Run the Jupyter notebook and follow the instructions provided in the notebook cells. 
3. Analyze the results and compare the performance of different models.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

   
## License

This project is licensed under the [MIT License](LICENSE).

## Authors
[Duvan Ricardo Cuero Colorado](https://github.com/merolemay)

[Alejandra Diaz Parra](https://github.com/trp216)
