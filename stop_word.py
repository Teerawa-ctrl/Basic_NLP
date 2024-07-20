##stop word Removal การลบคำที่ไม่สำคัญหรือว่าพบได้บ่อย เช่น is am are the in at on etc.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop words."
stop_words = set(stopwords.words("english"))

#print(stop_words) #คำตอบจะออกมาเป็น List คำของ Stopwords ทั้งหมด

words =  word_tokenize(example_sentence)

##filtered_sentense = []

##for w in words :                           #Loop เป็นการเช็คคำในตัวแปรwordsเทียบกับ Stop_words และนำคำเหล่านั้นใส่ลงไปใน filtered_sentence
    ##if w not in stop_words:
        ##filtered_sentense.append(w)
##print(filtered_sentense)                  #แสดงคำใน Stop word จากExample_sentence 

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)