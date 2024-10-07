import pandas as pd
from sklearn.ensemble import RandomForestClassifier

tracks = pd.read_csv('../../Entrega 2/Data/fma-rock-vs-hiphop.csv')
metrics = pd.read_json('../../Entrega 2/Data/echonest-metrics.json')
track_metrics=pd.merge(tracks,metrics)
track_metrics = track_metrics.drop(['track_id', 'bit_rate', 'comments', 'composer', 'interest', 'date_created', 'date_recorded','favorites','genres', 'genres_all', 'information', 'language_code', 'license', 'lyricist', 'number', 'publisher', 'tags'], axis=1)
# change the name of the column genre_top to genre
track_metrics = track_metrics.rename(columns={'genre_top': 'genre'})

def get_model():
    output_var_name = 'genre'
    y = track_metrics[output_var_name]
    input_var_name = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'tempo', 'valence']
    X = track_metrics[input_var_name]
    
    model = RandomForestClassifier(n_estimators=25, criterion='gini', max_depth=4, min_samples_leaf=2, min_samples_split=2, bootstrap=False, random_state=42)
    model.fit(X, y)
    return model