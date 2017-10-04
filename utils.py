import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score

my_tags = ['comedy', 'others']

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(my_tags))
    target_names = my_tags
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def evaluate_prediction(predictions, target, title="Confusion matrix"):
    print('accuracy %s' % accuracy_score(target, predictions))
    print('precision %s' % precision_score(target, predictions,pos_label='Comedy'))
    print('recall %s' % recall_score(target, predictions,pos_label='Comedy'))
    print('f-measure %s' % f1_score(target, predictions,pos_label='Comedy'))

    cm = confusion_matrix(target, predictions)
    print('confusion matrix\n %s' % cm)
    print('(row=expected, col=predicted)')

    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure()
    plot_confusion_matrix(cm_normalized, title + ' Normalized')
    plt.show()


def predict(vectorizer, classifier, data):
    data_features = vectorizer.transform(data['plot'])
    predictions = classifier.predict(data_features)
    target = data['tags']
    evaluate_prediction(predictions, target)


def getTags(genre, train):
    tagVector = []
    for tag in train['Genre1']:
        if tag == genre:
            tagVector.append(genre)
        else:
            tagVector.append('other')

    return tagVector
