#!/usr/
# pip install -U spacy
# python -m spacy download en_core_web_sm

'''
NAME
   resTPC - writes down the words present in a file along with their pos_ and lemma_

SYNOPSIS
   python3 restTPC.py [input_file]
   python3 -i resTPC.py [input_file] -> for spacy

DESCRIPTION
   This script gives out a table like output after processing the input_file. 
   The columns are: word, POS and Lemma. It uses SpaCy for NLP tasks.
   Added some new columns:
            1) Dependency Tree
            2) Children
            3) Morph
   Could also add the ancestors and make present the tree using displacy.
'''

import spacy
#from spacy import displacy #Para ver em página web a árvore
import pandas as pd
import sys

# Load Portuguese language model
nlp = spacy.load("pt_core_news_lg")

# Get the filename and directory from command-line arguments
file_path = sys.argv[1]

# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Process text
doc = nlp(text)
#displacy.serve(doc,style='dep')

# Extract words, POS, and lemma, we added the dependencies tree and the children
data = []
with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)
    
#Remove SPACE and other confusing entities    
for sentence in doc.sents:
    for token in sentence:
        if token.is_space:
            continue
        if token.pos_ == 'PROPN':
            data.append([token.text, token.pos_ , token.ent_type_, token.dep_, list(token.children)]) 
                        ##, token.morph])
        else:
            data.append([token.text, token.pos_, token.lemma_, token.dep_, list(token.children)])
            ##, token.morph])


# Create DataFrame
df = pd.DataFrame(data, columns=["Word", "POS","Lemma", "Dep", "Children"])
##, "Morph"])

# Display DataFrame
print(df)

# Optionally, you can also save to other formats
# df.to_json("dataframe_output.json", orient="records") #for a json file output
df.to_csv("dataframe_output.csv", index=False) #for a table like output
# df.to_excel("dataframe_output.xlsx", index=False)
# df.to_json("dataframe_output.json", orient="records")
# df.to_pickle("dataframe_output.pkl")
