import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


##PunktSentenceTokenizer is a unsupervised machine learing sentece tokenizer
##It is trained, we can retrain it if required


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")


##Retraining with sample data
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)



tokenized = custom_sent_tokenizer.tokenize(sample_text)

print (tokenized)

def process_content():
    try:
        for i in tokenized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print (str(e))


process_content()
