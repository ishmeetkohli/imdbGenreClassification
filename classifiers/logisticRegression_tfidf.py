from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model
from utils import predict
from preprocess import preprocess

data_features = preprocess("data/trainingSet.csv")
train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

tf_vect = TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None)

train_data_features = tf_vect.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

logreg = linear_model.LogisticRegression(n_jobs=1, C=1e5)
logreg = logreg.fit(train_data_features, train_data['tags'])

predict(tf_vect, logreg, test_data)