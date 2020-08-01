#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:34:55 2020

@author: akshay_ak
"""

from spacy import displacy

import json

import neuralcoref
import numpy as np

import spacy
from spacy.matcher import Matcher
from nltk.corpus import wordnet

#import nltk
from nltk import sent_tokenize
#from nltk import word_tokenize
#from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import sys
import os

args = sys.argv[1]
args_file = os.path.splitext(args)[0]

try:
    file = open(args, "r+")
    doc = file.read()
except:
    file = open(args, "r+", encoding = "latin1")
    doc = file.read()

file.close()



sentences2 = sent_tokenize(doc)




#for i in range(len(sentences)):
#    sentences[i] = word_tokenize(sentences[i])
    
    
    
#sentences = [(lambda x: word_tokenize(x))(x) for x in sentences]
#
#lementizer = WordNetLemmatizer()
#
#for i in range(len(sentences)):
#    sentences[i] = [(lambda x: lementizer.lemmatize(x))(x) for x in sentences[i]]
#    
#
#sentences = [(lambda x: nltk.pos_tag(x))(x) for x in sentences]


#nlp = spacy.load('en_core_web_sm')
#doc_spacy = nlp(doc)
#
#Tokens = np.unique(np.array([(token.orth_).lower() for token in doc_spacy if not token.is_punct | token.is_space | token.orth_.isdigit()]))
#
##Tokens = list(set([(token.orth_).lower() for token in doc_spacy if not token.is_punct | token.is_space]))
#
#sentences = [sent.string.strip() for sent in doc_spacy.sents]
#
#for i in range(len(sentences)):
#    linespacy = nlp(sentences[i])
#    sentences[i] = [(token.lemma_, token.pos_, token.dep_) for token in linespacy]
#
#
#hypernyms = []
#
##for i in range(len(Tokens)):
##   checking = wn.synsets(Tokens[i])
##   if checking:
##       temp = [wn.synset(c.name()).hypernyms() for c in checking]
##       hypernyms.append(temp)
#       
#
#hypernyms = []
#hyponyms = []
#meronyms = []
#holonyms = []
##synsets = []
#
#for i in range(len(Tokens)):
#    temp = wn.synsets(Tokens[i])
#    if temp:
#        hypernyms.append(wn.synset(str(temp[0].name())).hypernyms())
#        hyponyms.append(wn.synset(str(temp[0].name())).hyponyms())
#        meronyms.append(wn.synset(str(temp[0].name())).part_meronyms())
#        holonyms.append(wn.synset(str(temp[0].name())).part_holonyms())
##        synsets.append(temp[0].name())
#    else:
#        hypernyms.append(temp)
#        hyponyms.append(temp)
#        meronyms.append(temp)
#        holonyms.append(temp)
##        synsets.append(temp)
#        
#        
#        
#    
#    
#        
#synsets = [wn.synsets(token) for token in Tokens]
#split_syn_sets = [syn_set.hyponyms() for syn_set in synsets]



#neuralcoref.add_to_pipe(nlp)
#
#
#file = nlp(doc)
#
#resolved_text = file._.coref_resolved
#
#
#doc1 = nlp('My sister has a dog. She loves him.')
#
#print(doc1._.coref_clusters)


#coref = neuralcoref.NeuralCoref(nlp.vocab)
#nlp.add_pipe(coref, name='neuralcoref')
#file = nlp(u'My sister has a dog. She loves him.')
#
#doc1._.has_coref
#doc1._.coref_clusters
#
#nlp = spacy.load('en')
#
#
#coref = neuralcoref.NeuralCoref(nlp.vocab, allow_outside_corefs=True)
#nlp.add_pipe(coref, name='neuralcoref')
#
#doc1 = nlp(doc)
#
#print(doc1[0].text, "=", doc1[0].coref_clusters.text)
#print(doc1[2].text, "=", doc1[2].coref_clusters.main.text)

def write_json(data, filename=args_file+'.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)
 
    


dic_temp = {
        "document":args,
        "extraction":[]
        
        }
    
with open(args_file+".json",'w') as john:
    json.dump(dic_temp, john)


#**********************************************************************************************************
#                                    PHASE 2



#text = "In 2017, Amazon acquired Whole Foods Market for US$13.4 billion, which vastly increased Amazon's presence as a brickand-mortar retailer."
print()
print("Working on BUY template")
print()
nlp = spacy.load('en')
coref = neuralcoref.NeuralCoref(nlp.vocab, allow_outside_corefs=True)
nlp.add_pipe(coref, name='neuralcoref')
text = nlp(doc)

#corefsss = []
#
#
#
#    print(" ".join(i.sent_ for i in text if i.text == 'acquired'))
#
#
#displacy.serve(doc, style='dep')



#sentences = [sent.string.strip() for sent in text.sents]
#To classify the sentence according to template buy
buy = [i for i in sentences2 if 'acquired' in i.split() or 'buy' in i.split() or 'purchase' in i.split() or 'acquiring' in i.split() or 'buying' in i.split() or 'acquires' in i.split() or 'bought' in i.split() or 'purchasing' in i.split() or 'purchased' in i.split()]

#syns = wordnet.synsets("acquired")
#for i in range(len(syns)):
#    syns[i] = syns[i].name()



#entitiese = dict()
#extras = []
#for ent in doc.ents:
#    if ent.label_ not in entitiese:
#        entitiese[ent.label_] = ent.text
#    else:
#        extras.append(ent.text)
#    print(ent.text, ent.label_)
    

    
#for tok in doc:
#    print(tok.text, "---->", tok.dep_, "---->", tok.pos_)
#    
#print(doc.ents)




##Rules for extractions

for index,senten in enumerate(buy):
    doc1 = nlp(senten)
    
    entitiese = dict()
    extras = []
    for ent in doc1.ents:
        if ent.label_ not in entitiese:
            entitiese[ent.label_] = ent.text
        else:
            extras.append(ent.text)
        #print(ent.text, ent.label_)
    
    x = ''
    y = ''
    source = ''
    z = ''
    
    
    for i,tok in enumerate(doc1):
        
#        if tok.dep_.endswith("subj") == True and tok.pos_ == 'PROPN':

        if (tok.dep_ == 'nsubj' and tok.pos_ == 'PROPN') or tok.dep_ == 'amod' and tok.pos_ == 'NOUN':
            x = tok.text
        if x == '': 
            if tok.dep_ == 'pobj' and tok.pos_ == 'PROPN' or tok.dep_ == 'nsubj' and tok.pos_ == 'NOUN':
                x = tok.text
        
        for i in entitiese.values():
                if x in i.split():
                    x = i
                else:
                    for extra in extras:
                        if x in extra.split():
                            x = extra
            
    
#        if tok.dep_.endswith("obj") == True  and tok.pos_ == 'PROPN':
        if tok.dep_ == "dobj" and tok.pos_ == 'PROPN' or tok.dep_ == "dobj" and tok.pos_ == 'ADJ'or tok.dep_ == 'nsubjpass' and tok.pos_ == 'PROPN' or tok.dep_ == 'compund' and tok.pos_ == 'NOUN':
            #y = tok.text
            
            for i in entitiese.values():
                if tok.text in i.split():
                    y = i
                else:
                    for extra in extras:
                        if tok.text in extra.split():
                            y = extra
                if y == '':
                    y = tok.text
        if y == '':
            if tok.dep_ == "dobj" and tok.pos_ == "NOUN"  or tok.dep_ == 'nsubjpass' and tok.pos_ == 'NOUN'or tok.dep_ == 'compound' and tok.pos_ == 'PROPN' :
                y = tok.text
            
            for i in entitiese.values():
                if y in i.split():
                    y = i
                else:
                    for extra in extras:
                        if y in extra.split():
                            y = extra
                        
        
        
#        if tok.dep_ == "compound" and tok.pos_ == 'PROPN':
#            z = tok.text
#        for i in entitiese.values():
#            if z in i.split():
#                z = i
#            else:
#                for extra in extras:
#                    if z in extra.split():
#                        z = extra
        
        if tok.dep_ == 'pobj' and tok.pos_ == 'PROPN':
            source = tok.text
            
        if 'DATE' in entitiese.keys():
            if source in (entitiese['DATE'].split()):
                source = ''
                del entitiese['DATE']
        for i in entitiese.values():
            if source in i.split():
                source = i
            else:
                for extra in extras:
                    if source in extra.split():
                        source = extra
                        
     
        
    if x == 'company' or x == 'The company' or x == 'He' or x == 'they' or 'it' or 'that':
        inde = sentences2.index(buy[3])    
        if (inde-5)>= 0:
            sent_coref = [sentences2[inde-5],sentences2[inde-4],sentences2[inde - 3],sentences2[inde-2], sentences2[inde-1], sentences2[inde]]
            
            text_coref = "".join(sent_coref)
            
            coref = neuralcoref.NeuralCoref(nlp.vocab)
            
            text_c = nlp(text_coref)
            for cluster in text_c._.coref_clusters:
                x = str(cluster.mentions[0])


#    print(index)
    if 'MONEY' in entitiese.keys() and y != '' and x!=y:
#        print("["+str(x)+", "+str(y)+", "+entitiese['MONEY']+", "+" "+", "+str(source)+"]")
        dic = {
                "template":"BUY",
                "sentences": [senten],
                "arguments":{
                    "1":str(x),
                    "2":str(y),
                    "3":str(entitiese['MONEY']),
                    "4":'',
                    "5":str(str(source)),
                }
            }
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
        
    elif 'MONEY' in entitiese.keys() and len(extras) > 1 and y != '' and x!=y:
#        print("["+str(x)+", "+str(y)+", "+(entitiese['MONEY']+", "+extras[1]+", "+str(source)+"]"))
        dic = {
                "template":"BUY",
                "sentences": [senten],
                "arguments":{
                    "1":str(x),
                    "2":str(y),
                    "3":str(entitiese['MONEY']),
                    "4":extras[1],
                    "5":str(source),
                }
            }
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
        
    elif len(extras) > 1 and y != '' and x!=y:
#        print("["+str(x)+", "+str(y)+", "+" "+", "+extras[1]+", "+str(source)+"]")
        dic = {
                "template":"BUY",
                "sentences": [senten],
                "arguments":{
                    "1":str(x),
                    "2":str(y),
                    "3":'',
                    "4":extras[1],
                    "5":str(source),
                }
            }
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
        
    elif y !='' and x!=y:
        
#        print("["+str(x)+", "+str(y)+", "+" "+", "+" "+", "+str(source)+"]")
        dic = {
               "template":"BUY",
               "sentences": [senten],
               "arguments":{
                   "1":str(x),
                   "2":str(y),
                   "3":'',
                   "4":'',
                   "5":str(source),
               }
           }
                
                
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
                
        
   

   
#print(x,y, entitiese['MONEY'])
        
#for tok in doc:
#    if tok.dep_ == "nsubj" and tok.pos_ == "PROPN":
#        print(tok.text)
             
        
        
        
        
#Trying to solve this instance     
#text = "﻿In 1921, the Mexican president Álvaro Obregón along with the former revolutionary general visited Downtown Dallas's Mexican Park in Little Mexico; the small park was on the corner of Akard and Caruth Street, site of the current Fairmount Hotel."   
#test = nlp(text) 
#for tok in test:
#    print(tok.text, "---->", tok.dep_, "---->", tok.pos_)
#    if tok.dep_ == 'pobj' and tok.pos_ == 'PROPN':
#            source = tok.text
#            print(source)
#    for i in entitiese.values():
#        if source in i.split():
#            source = i
#        else:
#            for extra in extras:
#                if source in extra.split():
#                    source = extra
    
#entitiese = dict()
#extras = []
#for ent in test.ents:
#    if ent.label_ not in entitiese:
#        entitiese[ent.label_] = ent.text
#    else:
#        extras.append(ent.text)
#    #print(ent.text, ent.label_)
#    
#nlp.add_pipe(coref, name='neuralcoref')
#    
#    
#index = sentences2.index(buy[3])    
#sent_coref = [sentence[index-5],sentence[index-4],sentence[index - 3],sentences2[index-2], sentences2[index-1], sentences2[index]]
#
#text_coref = "".join(sent_coref)
#
#coref = neuralcoref.NeuralCoref(nlp.vocab)
#
#text_c = nlp(text_coref)
#
#for cluster in text_c._.coref_clusters:
#    print(cluster.mentions[0])
#    
#
#
#
#kk = ['Next', 'apple']
#for i in kk:
#    print(i.split())
#
#
#    
##to find synonyms
#    
#def get_related(word):
#  filtered_words = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -15]
#  similarity = sorted(filtered_words, key=lambda w: word.similarity(w), reverse=True)
#  return similarity[:10]
#print [w.lower_ for w in get_related(nlp.vocab[u'acquired'])]

print()
print("Successfully finished ectracting information for BUY template")
print()
#*********************************************************************************************************

print()
print("Working on PART template")
print()

nlp = spacy.load('en')
text = nlp(doc)


part = []
for sentence in sentences2:
    sent_part = nlp(sentence)
    for ent in sent_part.ents:
        if ent.label_ == 'GPE':
            part.append(sentence)
        pass
        
part = list(set(part))



#text = "Industries India's telecommunication industry, the world's fastest-growing, added 227 million subscribers during the period 2010–11, and after the third quarter of 2017, India surpassed the US to become the second largest smartphone market in the world after China."
#test = nlp(text)
#
#for tok in test:
#    print(tok.text, "---->", tok.dep_, "---->", tok.pos_)
#        
#
#
#entitiese = dict()
#extras = []
#for ent in test.ents:
#    if ent.label_ not in entitiese:
#        entitiese[ent.label_] = ent.text
#    else:
#        extras.append(ent.text)
#
#
#checker = dict()        
#for ent in test.ents:
#    checker[ent.label_] = ent.text
#       


countries_x = ['India','the United States', 'America', 'Russia','China','France','Indonesia','South Korea','Pakistan','Canada']
countries_y = ['India','the United States', 'America', 'Russia','China','France','Indonesia','South Korea','Pakistan','Canada']
False_y = ['Commissioner', 'February','June', 'July', 'Laureates', 'Love','Ft','Trump', 'Stockyards', 'Cedars', 'Shield', 'HOV', 'Careers',' American Airlines', 'Soccer','Meadows','Kerry','October','Fortune','II','Muslims', 'the Warsaw Pact','Archimedes','Jayanti','°','FIFA U-17 World Cup','January','Games', 'September','Nicolls']
False_x = ['Grant', 'Lincoln', 'The U.S. Navy', 'McClellan', 'Edward','Jr.','Forbes','Fortune','Valdez','Prado','AT&T', 'Slavic Voice of America', 'Texas Eagle', 'Soviets','Kaplan']
##Rules
for index, sent in enumerate(part):
    doc1 = nlp(sent)
    
    entitiese = dict()
    extras = []
    for ent in doc1.ents:
        if ent.label_ not in entitiese:
            entitiese[ent.label_] = ent.text
        else:
            extras.append(ent.text)
    
    
    x = ''
    y = ''
    
    
    for i,tok in enumerate(doc1):
        if tok.dep_ == 'nsubj' and tok.pos_ == 'PROPN' or tok.dep_ == 'compund' and tok.pos_ == 'PROPN':
#            x = tok.text
            
            for i in entitiese.values():
                if tok.text in i.split():
                    if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
                        if entitiese['LOC'] == i or entitiese['FAC'] == i or entitiese['GPE'] == i:
                            x = i
                    elif 'LOC' in entitiese.keys():
                        if entitiese['LOC'] == i  or entitiese['GPE'] == i:
                            x = i
                    elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
                        if entitiese['ORG'] == i or entitiese['GPE'] == i :
                            x = i
                    elif 'FAC' in entitiese.keys():
                        if entitiese['FAC'] == i or entitiese['GPE'] == i:
                            x = i
                    elif 'ORG' in entitiese.keys():
                        if entitiese['GPE'] == i or entitiese['ORG'] == i :
                            x = i
                    else:
                        if entitiese['GPE'] == i:
                            x = i
                    
                        
                else:
                    for extra in extras:
                        if tok.text in extra.split():
                            if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
#                                if entitiese['LOC'] == extra or entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                x = extra
                            elif 'LOC' in entitiese.keys():
#                                if entitiese['LOC'] == extra  or entitiese['GPE'] == extra:
                                x = extra
                            elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
#                                if entitiese['ORG'] == extra or entitiese['GPE'] == extra:
                                x = extra
                                    
                            elif 'FAC' in entitiese.keys():
#                                if entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                x = extra
                            elif 'ORG' in entitiese.keys():
#                                if entitiese['GPE'] == extra or entitiese['ORG'] == extra:
                                x = extra
                            else:
#                                if entitiese['GPE'] == extra:
                                x = extra
#                            x = extra
                            
        if x == '':
            if tok.dep_ == 'nmod' and tok.pos_ == 'PROPN':
#                x = tok.text
        
                for i in entitiese.values():
                        if tok.text in i.split():
                            if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
                                if entitiese['LOC'] == i or entitiese['FAC'] == i or entitiese['GPE'] == i:
                                    x = i
                            elif 'LOC' in entitiese.keys():
                                if entitiese['LOC'] == i  or entitiese['GPE'] == i:
                                    x = i
                            elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
                                if entitiese['ORG'] == i or entitiese['GPE'] == i :
                                    x = i
                            elif 'FAC' in entitiese.keys():
                                if entitiese['FAC'] == i or entitiese['GPE'] == i:
                                    x = i
                            elif 'ORG' in entitiese.keys():
                                if entitiese['GPE'] == i or entitiese['ORG'] == i:
                                    x = i
                            
                            else:
                                if entitiese['GPE'] == i:
                                    x = i
                            
                        else:
                            for extra in extras:
                                if tok.text in extra.split():
                                    if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
#                                        if entitiese['LOC'] == extra or entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                        x = extra
                                    elif 'LOC' in entitiese.keys():
#                                        if entitiese['LOC'] == extra  or entitiese['GPE'] == extra:
                                        x = extra
                                    elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
#                                        if entitiese['ORG'] == extra or entitiese['GPE'] == extra:
                                        x = extra
                                            
                                    elif 'FAC' in entitiese.keys():
#                                        if entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                        x = extra
                                    elif 'ORG' in entitiese.keys():
#                                        if entitiese['GPE'] == extra or entitiese['ORG'] == extra:
                                        x = extra
                                    
                                    else:
#                                        if entitiese['GPE'] == extra:
                                            x = extra
#                                    x = extra
                                    
                            
        if  tok.dep_ == 'compound' and tok.pos_ == 'PROPN' or tok.dep_ == 'pobj' and tok.pos_ == 'PROPN' or tok.dep_ == 'conj' and tok.pos_ == 'PROPN':
            y = tok.text
            
            for i in entitiese.values():
                if tok.text in i.split():
                    if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
                        if entitiese['LOC'] == i or entitiese['FAC'] == i or entitiese['GPE'] == i:
                            y = i
                    elif 'LOC' in entitiese.keys():
                        if entitiese['LOC'] == i  or entitiese['GPE'] == i:
                            y = i
                    elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
                        if entitiese['ORG'] == i or entitiese['GPE'] == i:
                            y = i
                    elif 'FAC' in entitiese.keys():
                        if entitiese['FAC'] == i or entitiese['GPE'] == i:
                            y = i
                    elif 'ORG' in entitiese.keys():
                        if entitiese['GPE'] == i or entitiese['ORG'] == i:
                            y = i

                    else:
                        if entitiese['GPE'] == i:
                            y = i
                    
                else:
                    for extra in extras:
                        if tok.text in extra.split():
                            if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
#                                if entitiese['LOC'] == extra or entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                y = extra
                            elif 'LOC' in entitiese.keys():
#                                if entitiese['LOC'] == extra  or entitiese['GPE'] == extra:
                                y = extra
                            elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
#                                if entitiese['ORG'] == extra or entitiese['GPE'] == extra:
                                y = extra
                            elif 'FAC' in entitiese.keys():
#                                if entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                y = extra
                            elif 'ORG' in entitiese.keys():
#                                if entitiese['GPE'] == extra or entitiese['ORG'] == extra:
                                y = extra
                            
                            else:
#                                if entitiese['GPE'] == extra:
                                y = extra
#                            y = extra
        if y == '':
            if tok.dep_ == 'nmod' and tok.pos_ == 'PROPN':
                for i in entitiese.values():
                    if tok.text in i.split():
                        if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
                            if entitiese['LOC'] == i or entitiese['FAC'] == i or entitiese['GPE'] == i:
                                y = i
                        elif 'LOC' in entitiese.keys():
                            if entitiese['LOC'] == i  or entitiese['GPE'] == i:
                                y = i
                        elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
                            if entitiese['ORG'] == i or entitiese['GPE'] == i:
                                y = i
                        elif 'FAC' in entitiese.keys():
                            if entitiese['FAC'] == i or entitiese['GPE'] == i:
                                y = i
                        elif 'ORG' in entitiese.keys():
                            if entitiese['GPE'] == i or entitiese['ORG'] == i:
                                y = i
                        
                        else:
                            if entitiese['GPE'] == i:
                                y = i
                    
                    else:
                        for extra in extras:
                            if tok.text in extra.split():
                                if 'LOC' in entitiese.keys() and 'FAC' in entitiese.keys():
#                                    if entitiese['LOC'] == extra or entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                    y = extra
                                elif 'LOC' in entitiese.keys():
#                                    if entitiese['LOC'] == extra  or entitiese['GPE'] == extra:
                                    y = extra
                                elif 'ORG' in entitiese.keys() and 'FAC' not in entitiese.keys():
#                                    if entitiese['ORG'] == extra or entitiese['GPE'] == extra:
                                    y = extra
                                elif 'FAC' in entitiese.keys():
#                                    if entitiese['FAC'] == extra or entitiese['GPE'] == extra:
                                    y = extra
                                elif 'ORG' in entitiese.keys():
#                                    if entitiese['GPE'] == extra or entitiese['ORG'] == extra:
                                    y = extra
                                
                                else:
#                                    if entitiese['GPE'] == extra:
                                    y = extra
#                                y =extra
                            

    if x!='' and y!='' and x not in False_x and y not in False_y and x!=y and (x not in countries_x and y not in countries_y):
#        print(index)
#        print("["+str(x)+", "+str(y)+"]")  
        dic = {
                "template":"PART",
                "sentences": [sent],
                "arguments":{
                    "1":str(x),
                    "2":str(y),
                }
            }
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
    
    
    
    
    
    
#for index, i in enumerate(part):
#    doc1 = nlp(i)
#    
#    entitiese = dict()
#    extras = []
#    for ent in doc1.ents:
#        if ent.label_ not in entitiese:
#            entitiese[ent.label_] = ent.text
#        else:
#            extras.append(ent.text)
#    
#    
#    x = ''
#    y = ''
#    
#    
#    for i,tok in enumerate(doc1):
#        if tok.dep_ == 'nsubj' and tok.pos_ == 'PROPN':
#            x = tok.text
#        if x == '':
#            if tok.dep_ == 'nmod' and tok.pos_ == 'PROPN':
#                x = tok.text
#    
#        for i in entitiese.values():
#                if x in i.split():
#                    x = i
#                else:
#                    for extra in extras:
#                        if x in extra.split():
#                            x = extra
#                            
#        if tok.dep_ == 'nmod' and tok.pos_ == 'PROPN' or tok.dep_ == 'compound' and tok.pos_ == 'PROPN':
#            y = tok.text
#            
#        for i in entitiese.values():
#                if y in i.split():
#                    y = i
#                else:
#                    for extra in extras:
#                        if y in extra.split():
#                            y = extra
#    
#    
#    print(index)
#    print("["+str(x)+", "+str(y)+"]") 
#    


print()
print("Successfully complete on extracting information for PART template")
print()
#**********************************************************************************************************    
    

    

print()
print("Working on WORK template")
print()

nlp = spacy.load('en')
text = nlp(doc)


work = []
for sentence in sentences2:
    labels = set()
    sent_part = nlp(sentence)
    for ent in sent_part.ents:
        labels.add(ent.label_)
        if 'PERSON' in labels and 'ORG' in labels and 'LOC' in labels or 'PERSON' in labels and 'ORG' in labels and 'GPE' in labels or 'PERSON' in labels and 'ORG' in labels :
            work.append(sentence)
        pass
        
work = list(set(work))






#
#text = "Steve Jobs and Steve Wozniak were Beatles fans, but Apple Inc. had name and logo trademark issues with Apple Corps Ltd., a multimedia company started by the Beatles in 1967."
#test = nlp(text)
#
#
#for tok in test:
#    print(tok.text, "---->", tok.dep_, "---->", tok.pos_)
#        
#
#
#entitiese = dict()
#extras = []
#for ent in test.ents:
#    if ent.label_ not in entitiese:
#        entitiese[ent.label_] = ent.text
#    else:
#        extras.append(ent.text)

#person =[]
#org = []
#
#for ent in test.ents:
#    if ent.label_ == 'PERSON':
#        person.append(ent.text)
#    if ent.label_ == 'ORG':
#        org.append(ent.text)

#print(person)
#print(org)








design = ['CEO','CFO', 'senior vice president', 'Chief Operating Officer', 'Chief Executive Officer','executive director']


for index,sen in enumerate(work):
    doc3 = nlp(sen)
    entitiese = dict()
    extras = []
    for ent in doc3.ents:
        if ent.label_ not in entitiese:
            entitiese[ent.label_] = ent.text
        else:
            extras.append(ent.text)

    person =[]
    org = []
    
    for ent in doc3.ents:
        if ent.label_ == 'PERSON':
            person.append(ent.text)
        if ent.label_ == 'ORG':
            org.append(ent.text)
    x = ''
    y = ''
    z = []
    d = ''
    oorr = ''
    l = ''
    dd = dict()
    old = ''
    for i,tok in enumerate(doc3):
    
            
        if tok.dep_ == 'compound' and tok.pos_ == 'PROPN' or tok.dep_ == 'amod' and tok.dep_ == 'ADJ' or tok.dep_ == 'compound' and tok.pos_ == 'NOUN' or tok.dep_ == 'appos' and tok.pos_ == 'NOUN':
            for per in person:
                if tok.text in per.split():
                    if per not in dd:
                        dd[per] = ''
                        old = per
                else:
                    if old in dd:
                        if dd[old] == '':
                            for des in design:
                                if tok.text in des.split():
                                    dd[old] = des
                        else:
                            z.append(tok.text)
                    else:
                        z.append(tok.text)
                        
                        
            
    for i in range(len(z)):
        for des in design:
            if z[i] in des.split():
                z[i] = des
            else:
                z[i] = ''
                
                



#    print(index)
    for i in range(len(person)):
        x = person[i]
        if len(org)>1:
            y = org[1]
        else:
            y = org[0]
        if x in dd.keys():
            if dd[x]!='':
                d = dd[x]
            else:
                if 0<=i<len(z):
                    d = z[i]
                else:
                    if not z:
                        d = ''
                    else:
                        d = z[0]
        else:
            if 0<=i<len(z):
                d = z[i]
            else:
                if not z:
                    d = ''
                else:
                    d = z[0]
#        print("["+str(x)+", "+str(y)+", "+str(d)+", "+str(l)+"]")
        dic = {
                "template":"WORK",
                "sentences": [sen],
                "arguments":{
                    "1":str(x),
                    "2":str(y),
                    "3":str(d),
                    "4":str(l),
                }
            }
        with open(args_file+".json",'r') as json_file:
            data = json.load(json_file)
            temp = data['extraction']
            temp.append(dic)
            
        write_json(data)
        
        
#    print()
#    print()
    
    


print()
print("Successfully complete on extracting information for WORK template")
print()

print()
print("All the information is extracted for the respective templates and stored in the "+args_file+".json file which is generated in the project folder.")
    
    
    
    
    
    
    
    
#dic_temp = {
#        "document":"Amazon_com.text",
#        "extraction":[sen],
#        "arguments":{
#            "1":str(x),
#            "2":str(y),
#            "3":str(d),
#            "4":str(l)
#                
#                }
#        }
#    
#with open("sample_json.json",'w') as john:
#    json.dump(dic_temp, john)
#
#    
#    
#    
#aa = ['ak', 'asdka', 'weu']
#kk = ['uasy', 'neiu']
#
##with open("sample_json.json", "w") as data:
#for s in aa:
#    for k in kk:
#        
#        dic = {
#        			"template": "BUY",
#        			"sentences": ["In 2017, Amazon acquired Whole Foods Market for US$13.4 billion, which vastly increased Amazon's presence as a brick-and-mortar retailer."],
#        			"arguments": {
#        				"1": s,
#        				"2": k,
# 
#        			}
#        		}
#        with open("sample_json.json",'r') as json_file:
#            data = json.load(json_file)
#            temp = data['extraction']
#            temp.append(dic)
#            
#        write_json(data)


