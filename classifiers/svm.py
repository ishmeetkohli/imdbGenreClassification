from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from utils import predict
from preprocess import preprocess

data_features = preprocess("data/trainingSet.csv")
train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

print len(test_data)

vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=3000)
train_data_features = vectorizer.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

lin_clf = svm.LinearSVC()
lin_clf.fit(train_data_features, train_data['tags'])

predict(vectorizer, lin_clf, test_data)
