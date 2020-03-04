import csv
import spacy

import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_files
from operator import itemgetter
import nltk


NUM_GROUPS = 20

print ('Processing started...')
print()

random_state = 0 
data = pd.read_csv('reviewsFiltrado.csv')
vec = TfidfVectorizer(stop_words="english")
vec.fit(data.text.values)
features = vec.transform(data.text.values)

cls = MiniBatchKMeans(n_clusters=NUM_GROUPS, random_state=random_state)
cls.fit(features)

cl=pd.DataFrame(cls.labels_)
df = pd.DataFrame(columns=['text', 'group'])
for i in range(cl.__len__()):
    with open('reviewsFiltrado.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            doc = row[1]
            num = row[0]
            if (str(i) == row[0]):
                df.loc[i] = [row[1],str(cl.loc[i, 0])]


#calculando frequências em grupos

print ('** Commentary Groups created considering the similarity among NOUNS:')
print()
totalWords=[]
for i in range(NUM_GROUPS):

    print ('*Group:' + str(i))

    ls = ''
    contSentences = 0
    for index, row in df.iterrows() :
        if (row['group']== str(i)):
            #print(row['text'], row['group'])
            ls =  ls  + ' '.join(sorted(set(row['text'].lower().lstrip().rstrip().split(' ')))) + " "
            contSentences+=1
    
    
    print ('*Number of commentaries:' + str(contSentences))
    
    ls = ls.rstrip()
    
    words = ls.split(' ')
    
    #print (words)
         
    words_and_frequencies = []
    for word in words:
        words_and_frequencies.append((word, words.count(word)))
    
    sorted_list = sorted(frozenset(words_and_frequencies), key=itemgetter(1), reverse=True)
    print(sorted_list[:20])
    print ()

    i=0
    for word in words:
        if (i<=20 and i<=sorted_list.__len__()-1 ):
            totalWords.append (sorted_list[i][0])
        i+=1
        

freqWordDocs=[]
for word in totalWords:
    totalWords.count(word)
    freqWordDocs.append ((word,totalWords.count(word)))

print ("**Calculation: in how many groups each word above appeared:")
lsFreqDocGroup = sorted(frozenset(freqWordDocs), key=itemgetter(1), reverse=True)
print (lsFreqDocGroup)
print()

print ("**Identifying the context of the noun:-" + lsFreqDocGroup[0][0] + '-')
print()     
with open('reviews.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)  
    listTexts=[]
    cont=0
    for row in reader:
        if (row[5].find (lsFreqDocGroup[0][0])>-1 and cont<=25):
            listTexts.append(row[5])
            print ('* ' + row[5])
            print()
            cont+=1

print()
print ('** Finished')