 #!/usr/bin/env python3  

'''
NAME
    load_data - which uses spellChecker to correct misspelled words in the files read

SYNOPSIS
    python3 load_data.py

DESCRIPTION
    This script loads up all the collection present below into a single txt file, a word to sentiment dictionary, separated by a tab.

FILES
    - booster.txt: Contains booster words for sentiment analysis
    - lex.txt: Contains sentiment scores for words
    - expressions.txt: Contains sentiment data
    - negate.txt: Contains negations in Portuguese

'''

import sys
import spacy
from spellchecker import SpellChecker

###
# Loading up the booster words into a dictionary
###
def load_sentiment_dict(file_path,sentiment_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, sentiment = line.strip().split(maxsplit=1)
            if sentiment== "DECR":
                sentiment_dict[word] = -0.293   # According to LeIA's analysis
            else:
                sentiment_dict[word] = 0.293    # According to LeIA's analysis

###
# Loading up the words and their assigned sentiment from a given file
###
def load_sentiment_scores(file_path,sentiment_dict):
    # Initialize spellchecker
    spell_checker = SpellChecker(language='pt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.strip().split('\t')
            word = columns[0]
            score = float(columns[1])
            
            # Check and correct spelling errors
            corrected_word = spell_checker.correction(word)
            
            if corrected_word != None:
                # Save the corrected word in the sentiment scores dictionary
                sentiment_dict[corrected_word] = score
                print(f"{corrected_word}: {score}")
            else:
                sentiment_dict[word] = score
                print(f"{word}: {score}")
            

###
# Load the sentiment of the expressions.txt file
###
def read_sentiment_data(file_path,sentiment_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Check if the line is not empty
                expression, sentiment = line.split(';')
                if sentiment == "POS":
                    sentiment_dict[expression] = 2
                else:
                    sentiment_dict[expression] = -2

###
# Main
###
def main():
    print("I'm getting started now!")
    sentiment_dict={}
    
    booster_dict_file = "booster.txt"    # Path to the file containing the booster words
    booster_dict = load_sentiment_dict(booster_dict_file,sentiment_dict)
    
    print("Got boosters words.")
    
    sentiment_scores_file = "lex.txt"  # Path to the file containing sentiment scores
    sentiment_scores_dict = load_sentiment_scores(sentiment_scores_file,sentiment_dict)
    
    print("Got lex words.")
    
    sentiment_file = 'expressions.txt'  # Path to your sentiment data file
    sentiment_data = read_sentiment_data(sentiment_file,sentiment_dict)
    
    print("Got the expressions.")
    
    negate_dict_file = "negate.txt"    # Path to the file containing negations in portuguese
    with open(negate_dict_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            sentiment_dict[word] = -0.74   # According to LeIA's analysis
    
    print("Negations too!!")  
    
    with open("sentiment_dict.txt","w") as file:
        for key,value in sentiment_dict.items():
            file.write(f"{key}\t{str(value)}\n")
     
    
if __name__=="__main__":
    main()