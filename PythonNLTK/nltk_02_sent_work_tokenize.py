from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Pythonpro, how are you doing today? welcome to the python programming"

print ("word list","\n","~~~~~~~~~~")
print (word_tokenize(example_text))
print ("sentence list","\n","~~~~~~~~~~~~~")
print (sent_tokenize(example_text))

print ("\n","Let us print all the sentences","\n")
for i in sent_tokenize(example_text):
    print(i)
    
    
