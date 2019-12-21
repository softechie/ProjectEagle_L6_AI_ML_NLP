import re
import nltk
from nltk.tokenize import word_tokenize

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

tokenized = word_tokenize(exampleString)
##print (tokenized)

for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
##    print (tagged)

    chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print (chunked)

##    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
##        print(subtree)

##    chunked.draw()

