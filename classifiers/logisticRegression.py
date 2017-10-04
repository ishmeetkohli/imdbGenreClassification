from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import linear_model
from utils import predict
import matplotlib.pyplot as plt

from preprocess import preprocess

data_features = preprocess("data/trainingSet.csv")

train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

# counts = test_data.tags.value_counts()
# counts.plot(kind='bar')
# plt.show()

vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=3000)
train_data_features = vectorizer.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

logreg = linear_model.LogisticRegression(n_jobs=1, C=1e5)
logreg = logreg.fit(train_data_features, train_data['tags'])

predict(vectorizer, logreg, test_data)