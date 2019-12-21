import nltk
import random
from nltk.corpus import movie_reviews

documents=[]

##for category in movie_reviews.categories():
##    print (category)
##    for fileid in movie_reviews.fileids(category):
##        print (fileid)
##        documents.append(list(movie_reviews.words(fileid)),category)

## The above can be written in one line using the below statement
documents = [(list(movie_reviews.words(fileid)), category, fileid)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print (documents[1])


all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

## Using frequency distribution, and it tells us the frequency of each vocabulary item in the text.
all_words = nltk.FreqDist(all_words)

print(all_words.most_common(15))
print(all_words["stupid"])
