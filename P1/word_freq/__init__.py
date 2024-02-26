 #!/usr/bin/env python3  

'''
NAME
   word_freq - calculates the frequency of words in a text

SYNOPSIS
   word_freq [options] input_file
   options:
        -m: ordered alphabetically (default behavior)
        -n: ordered by number of appearances
        -i: ordered by the most important words

DESCRIPTION
   This script calculates and displays the frequency of words in a given text file.
   It supports ordering the output either alphabetically or by number of appearances.
'''

from jjcli import * 
from collections import Counter
import re

__version__="0.0.1"

def tokeniza(texto):
    #palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:!?—]+', texto.lower(), re.IGNORECASE)
    palavras = re.findall(r'[a-zA-Z]+(?:\-[a-zA-Z]+)?', texto.lower())
    return palavras
             
def imprime(lista, numeric=False):
    if numeric:
        # Sort by number of occurrences (descending) then alphabetically
        lista.sort(key=lambda x: (-x[1], x[0])) 
    else:
        # Sort alphabetically
        lista.sort()
        
    for palavra, n_ocorr in lista:
        
        print(f"{palavra}   {n_ocorr}") #professor prefere ao contrário, acha mais astético
        
def important(lista,total):
    words_ratio={}
    
    # Sort alphabetically
    lista.sort()
        
    with open("data/tabelaRes.txt", 'r') as file:
        # Read each line in the file
        for line in file:
            #print(f"{line}")
            # Split the line at whitespace characters
            parts = line.strip().split('\t') 
            
            word,ocur = parts
            #print(f"{word}  {ocur}")
            words_ratio[word]=float(ocur)
    
    for palavra, n_ocorr in lista:
        ratio= n_ocorr/total 
        
        if palavra in words_ratio.keys():
            if ratio >=  words_ratio[palavra]:
                print(f"{palavra}   {ratio}")
        else:
            print(f"{palavra}   {ratio}") 
                


def main():
    # Command-line interface setup
    cl = clfilter("mni", doc=__doc__)

    for txt in cl.text():  # Process one file at a time
        lista_palavras = tokeniza(txt)
        ocorr = Counter(lista_palavras)
        lista_items = list(ocorr.items())

        if "-n" in cl.opt:
            # Order by number of appearances if -n option is present
            imprime(lista_items, numeric=True)
        if "-i" in cl.opt:
            # Order by number of appearances if -n option is present
            important(lista_items,len(lista_palavras))
        else:
            # Default to alphabetical order
            imprime(lista_items)


