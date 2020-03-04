import csv
import spacy
import pandas as pd
import goslate
from googletrans import Translator
from langdetect import detect
from oauthlib.oauth2.rfc6749.endpoints.base import catch_errors_and_unavailability



translator = Translator()
gs = goslate.Goslate()

nlp = spacy.load("en_core_web_sm")
print ('Processing started...')
with open('reviews.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    LTextosF = []
    
    listTexts=[]
    for row in reader:
        listTexts.append(row[5])
    
    #it = list(gs.translate(listTexts, target_language='en'))
    
    it = listTexts

    strT=''
    for row in it:
        try:
            if (row.rstrip().lstrip() !='' and detect(row)=='en'):
                doc = nlp(row)
                for token in doc:
                    if (token.pos_=='NOUN'):
                        strT =  strT + token.orth_ + ' '
    
            if (strT!=''):
                LTextosF.append(strT)
        except:
            print ('Load error unexpected, continuing...')
        strT=''
    #print (LTextosF)    
    pd.DataFrame(LTextosF).to_csv('reviewsFiltrado.csv',index=True, header=['text'])
    print ('File reviewsFiltrado.csv created.')
