import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from utils import getTags

def plotToWords(raw_plot):
    plot = BeautifulSoup(raw_plot, "lxml")
    letters_only = re.sub("[^a-zA-Z]", " ", plot.get_text())
    lower_case = letters_only.lower()
    words = lower_case.split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return (" ".join(meaningful_words))

def preprocess(filename):
    train = pd.read_csv(filename)
    # counts = train.Genre1.value_counts()
    # counts.plot(kind='bar')
    # plt.show()
    # print counts

    num_reviews = train["Plot"].size
    clean_train_reviews = []

    for i in range(0, num_reviews):
        if ((i + 1) % 100 == 0):
            print "Review %d of %d\n" % (i + 1, num_reviews)
        clean_train_reviews.append(plotToWords(train["Plot"][i]))

    tagVector = getTags('Comedy', train)
    data = {'plot': clean_train_reviews, 'tags': tagVector}
    df = pd.DataFrame(data)

    return df