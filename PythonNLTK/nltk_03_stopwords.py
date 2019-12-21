from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = "This is a sample sentence, showing off the stop word filtration"
stop_word_list = set(stopwords.words('english'))
print ("Stop Word List","\n","~~~~~~~~~~~~~")
print (stop_word_list)


word_tokens = word_tokenize(example_text)

##filtered_sentence=[]
##for w in word_tokens:
##    if w not in stop_word_list:
##        filtered_sentence.append(w)

## The above commented statements can be written in 1 statement to reduce the processing time

filtered_sentence = [w for w in word_tokens if w not in stop_word_list]

print ("\n")
print (word_tokens)
print (filtered_sentence)
                   
