import re
import nltk
from nltk.tokenize import word_tokenize

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
I work for AtosSyntel Inc, located at Phoenix US
My birthday is in June, 06-01-1900
I spent Canadian Dollars 20 today
I go to gym weekly twice
I maintained 100% attendance
'''

tokenized = word_tokenize(exampleString)


for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)

    namedEnt = nltk.ne_chunk(tagged)

    print (namedEnt)
    namedEnt.draw()


    
##NE Type and Examples
##ORGANIZATION - Georgia-Pacific Corp., WHO
##PERSON - Eddy Bonte, President Obama
##LOCATION - Murray River, Mount Everest
##DATE - June, 2008-06-29
##TIME - two fifty a m, 1:30 p.m.
##MONEY - 175 million Canadian Dollars, GBP 10.40
##PERCENT - twenty pct, 18.75 %
##FACILITY - Washington Monument, Stonehenge
##GPE - South East Asia, Midlothian
