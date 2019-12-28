# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:59:38 2019

@author: thiya
"""

import nltk
import random


#cleaning the text
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ps = PorterStemmer()
wordnet = WordNetLemmatizer()

# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

#Reading in the corpus
with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read()
 
sentences = nltk.sent_tokenize(raw)

#Preprocessing
corpus=[]
for i in range(len(sentences)):
    prereview = re.sub('[^a-zA-Z]', ' ', sentences[i])
    prereview = prereview.lower()
    prereview = prereview.split()
    prereview = [wordnet.lemmatize(word) for word in prereview if word not in set(stopwords.words("english"))]
    prereview = ' '.join(prereview)
    corpus.append(prereview)


def greeting(greet):
    """If user's input is a greeting, return a greeting response"""
    for word in greet.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)



def response(user_response):
    review = re.sub('[^a-zA-Z]', ' ', user_response)
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if word not in set(stopwords.words("english"))]
    review = ' '.join(review)
    corpus.append(review)
    
    
    #creating the TF-IDF model
    cv = TfidfVectorizer()
    X = cv.fit_transform(corpus)

    vals = cosine_similarity(X[-1], X)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat2=flat.copy()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response="I am sorry! I don't understand you"
    else:
        robo_response = sentences[idx]
   
    corpus.pop()
    return robo_response

flag=True
print("Flexi: My name is Flexi. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input("You :")
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Flexi: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Flexi: "+greeting(user_response))
            else:
                print("Flexi: ",end="")
                print(response(user_response))
#                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Flexi: Bye! take care..")    
 
 
 