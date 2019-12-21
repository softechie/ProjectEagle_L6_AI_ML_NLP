from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example_text = "It is important to be very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

example_words = ["Python","Pythoner","Pythoning","Pythoned","Pythonly"]

ps = PorterStemmer()

for w in example_words:
    print (ps.stem(w))

word_list = word_tokenize(example_text)

for w in word_list:
    print(ps.stem(w))
