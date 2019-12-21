import nltk
import random
from nltk.corpus import movie_reviews

i="neg/cv884_15230.txt"

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        if fileid == i:
            documents = [(list(movie_reviews.words(fileid)), category)]



random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

## Using frequency distribution, and it tells us the frequency of each vocabulary item in the text.
all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:300]

##print (word_features)

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

##print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

print (featuresets)
