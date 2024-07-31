#การทำ POS Tagging นำข้อมูลที่ต้องติดแทคมาฝึก Model NLP จากไฟล์  "2005-GWBush.txt" และ "2005-GWBush.txt" เพื่อให้ POS Tagging เรียนรู้ประเภทของคำในข้อความนั้นๆ

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer #sort of it is an unsupervised



train_text = state_union.raw("2005-GWBush.txt")
example_text = state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(example_text) #สร้าง custom sentence tokenizer โดยใช้ข้อความจาก example_text

tokenized = custom_sent_tokenizer.tokenize(example_text) #ทำก่ารTokenize คำในประโยคแล้วเก็บค่าไว้ในตัวแปร Tokenize

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i) # แยกประโยคออกเป็นคำ
            tagged = nltk.pos_tag(words)  #แยกแต่ละคำเพื่อทำTagging
            print(tagged)
            
    except Exception as e :
        print(str(e))

process_content()