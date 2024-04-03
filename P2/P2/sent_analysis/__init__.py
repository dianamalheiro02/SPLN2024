 #!/usr/bin/env python3  

'''
NAME
    sent_analysis - A tool for sentiment analysis on Portuguese texts, using Spacy, with support for emoji description replacement and sentiment scoring.

SYNOPSIS
    sent_analysis
     
    Giving the type of file and it's directory too, when asked, where:
        1. b - book type file, where we read the whole file and analyse the sentiment of it, from top to bottom.
        2. f - tweet type file, where we read and analyse it line by line, giving the sentiment of each.
        3. directory should be in the tests file, since that folder is dedicated to holding the txt files that we want to analyse the sentiment of.
        
DESCRIPTION
    This script performs sentiment analysis on Portuguese texts. 
    It utilizes the Spacy library for language processing to tokenize texts and the LeIA sentiment analysis methodology for scoring. 
    The tool supports analyzing texts from two sources: books ('b') and tweets ('t'), allowing for the replacement of emojis with their descriptions for more accurate analysis. 
    Sentiment scores are calculated based on predefined sentiment values for Portuguese words, and the results are categorized as Positive, Negative, or Neutral based on these scores.
    The tool requires the user to specify the type of text source (book or tweet) and the path to the text file. It also utilizes predefined dictionaries for emojis and sentiment scores, which need to be present in a 'data' directory.

FILES
    data/sentiment_dict.txt - Contains the sentiment scores for Portuguese words. Each line in the file should have a word and its corresponding sentiment score, separated by a tab. 
    data/emoji.txt - Contains the mapping of emojis to their descriptions. Each line in the file should have an emoji and its description, separated by a tab.
    res.txt - Output file where the sentiment analysis tool writes the sentiment score of each analyzed word from the input text. The format for each line in the file is "ID: <word> ; <sentiment_score>".
    The script also relies on external libraries such as jjcli, Spacy, and SpellChecker. Ensure these are installed and the Portuguese language model ('pt_core_news_lg') for Spacy is downloaded before running the script.
'''

from jjcli import * 
import re
import sys
import spacy
from spellchecker import SpellChecker

__version__="0.0.1"

# Load Portuguese language model
nlp = spacy.load("pt_core_news_lg")


###
# Get a list filled with the words present in the input text
###
def tokeniza(texto):
    #palavras = re.findall(r'[a-zA-Z]+(?:\-[a-zA-Z]+)?', texto.lower())
    #return palavras

    # Process text
    doc = nlp(texto)

    # Extract words, POS, and lemma, we added the dependencies tree and the children
    data = []
    with doc.retokenize() as retokenizer:
        for entity in doc.ents:
            retokenizer.merge(entity)
        
    for sentence in doc.sents:
        for token in sentence:
            data.append(token.text) 

    #print(data)
    return data


###
# Loading up the emojis and their description into a dictionary
###
def load_emoji_dict(file_path):
    emoji_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            emoji, description = line.strip().split('\t')  # Assuming emojis and descriptions are tab-separated
            emoji_dict[emoji] = description
    return emoji_dict

###
# Replacing the emoji with their description for a better analysis
###
def replace_emojis(text, emoji_dict):
    replaced_text = ""
    for char in text:
        if char in emoji_dict:
            replaced_text += emoji_dict[char]
        else:
            replaced_text += char
    return replaced_text

###
# Loading up the booster words into a dictionary
###
def load_sentiment_dict(file_path):
    sentiment_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.strip().split('\t')
            word = columns[0]
            #print(word)
            score = float(columns[1])
            #print(score)
            sentiment_dict[word] = float(score)   # According to LeIA's analysis
    return sentiment_dict

###
# Used to analyse the polarity of a given text using the dictionaries made
###
def analysis(lista,sentiment_dict):   
    sentiment = 0
    word = 0
    with open("res.txt","w") as file:
        for palavra in lista:
            if palavra in sentiment_dict:
                sentiment += sentiment_dict[palavra]
                word+=1 
                file.write(f"ID:    {palavra}   ;   {sentiment_dict[palavra]}\n")
    
    if round(sentiment) > 0:
        print(f"This text was POSITIVE, having received a sentiment of: {round(sentiment)} \n  -> where {word}/{len(lista)} were attributed sentiment")
    elif round(sentiment) < 0:
        print(f"This text was NEGATIVE, having received a sentiment of: {round(sentiment)} \n  -> where {word}/{len(lista)} were attributed sentiment")
    else:
        print(f"This text was NEUTRAL, having received a sentiment of: {round(sentiment)} \n   -> where {word}/{len(lista)} were attributed sentiment")


###
# Main
###
def main():
    while True:
        mod = input("Type of file we are analysing:\n   > ") # b for book; t for tweet
    
        file_path = input("Input directory:\n   > ") # File that we are analysing

        print("I'm getting started now!")
        
        sentiment_dict_directory = "data/sentiment_dict.txt"    #Path to the file containing the dictionary available
        sentiment_dict=load_sentiment_dict(sentiment_dict_directory)
        
        emoji_dict_file = "data/emoji.txt"    # Path to the file containing emoji descriptions
        emoji_dict = load_emoji_dict(emoji_dict_file)
        
        print("I got the emojis replaced :)")
        
        if mod == "b":
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            
            replaced_text = replace_emojis(text, emoji_dict)
            lista_palavras = tokeniza(replaced_text)
            analysis(lista_palavras,sentiment_dict)

        elif mod == "t":
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    replaced_text = replace_emojis(line, emoji_dict)
                    lista_palavras = tokeniza(replaced_text)
                    
                    analysis(lista_palavras,sentiment_dict)    
        