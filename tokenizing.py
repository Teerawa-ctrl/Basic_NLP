import nltk

#nltk.download()

#tokenizing 

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = " Hello Mr.John , how are you doing to day ? The weather is great and python is great , The sky to day is blue?"

#print(sent_tokenize(example_text)) #แยกประโยค
#print(word_tokenize(example_text)) #แยกทีละคำ

for i in word_tokenize(example_text) :
    print(i)
    
    
for i in sent_tokenize(example_text) :
    print(i)