# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:59:38 2019

@author: thiya
"""

from flask import Flask, render_template, request, redirect
from vsearch import search4letters
import requests

app = Flask(__name__)

import nltk
import random


#cleaning the text
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

wordnet = WordNetLemmatizer()

log = []
previous_response = []

login_id = []
password = []

login_url = 'http://pfm-api-prod.herokuapp.com/login'



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


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


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
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response="I am sorry! I don't understand you"
    else:
        robo_response = sentences[idx]
   
    corpus.pop()
    return robo_response

@app.route('/chat')
def chat_response() -> str:
    user_response = request.args.get('msg')

    user_response = user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return str("Flexi: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                return str(greeting(user_response))
            else:        
                chat_response = response(user_response)
                return str(chat_response)
    else:
        return str("Flexi: Bye! take care.." + str(log))    

    return str(response(user_msg))
 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry2.html',the_title='Chatbot')

if __name__ == '__main__':
    app.run()