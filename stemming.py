#Stemming เป็นการลดรูปคำจากคำว่า run ran running ให้อยู่ในรูปแบบเดียวกันตือ  run จากดิกชันน่ารรี่ บางคำอาจจะลดรููปจาก pyythonly -> pythonli

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 

ps = PorterStemmer()

example_word = ("python", "pythoner" , "pythoning", "pythoned", "pythoned","pythonely")

##for w in example_word :
##   print(ps.stem(w))

new_text = " It is very important to be pytthonly while you are pythoning with Python. All pythoner have pythonly to be gratefull"
words = word_tokenize(new_text)

for w in words :
    print(ps.stem(w))