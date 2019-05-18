# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, The Journey Starts Here... Be Patient ---moving to Agave Library ---Phoenix."

# To take input from the user
#my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print("Welcome to Python Programming")
print("This program will exclude the punctuations from given input and outputs only String values")
print("Input Given:",my_str)
print("Output:",no_punct)