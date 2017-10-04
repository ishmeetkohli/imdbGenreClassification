from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import predict
from preprocess import preprocess

data_features = preprocess("data/trainingSet.csv")
train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

vectorizer = TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None)

train_data_features = vectorizer.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

lin_clf = svm.LinearSVC()
lin_clf.fit(train_data_features, train_data['tags'])

predict(vectorizer, lin_clf, test_data)
