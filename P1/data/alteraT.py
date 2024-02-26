#from jjcli import * 
#from collections import Counter
import re

word_count = {}
ratio=0
num_lines = 0
num_lines1 = 0

def tokeniza(texto):
    palavras = re.findall(r'\d+', texto.lower())
    return palavras

def tokeniza1(texto):
    palavras = re.findall(r'[a-zA-Z]+(?:\-[a-zA-Z]+)?', texto.lower())
    return palavras

# Open the file
with open("tabelaOriginal.txt", 'r') as file:
    # Read each line in the file
    for line in file:
        num_lines+=1
        # Split the line at whitespace characters
        parts = line.strip().split()
            
        # Check if there are exactly two parts
        if len(parts) == 2:
            # Unpack the parts into key and value
            key, value = parts
            
            #Get only the good ones
            if len(tokeniza(value)) == 0 and int(key) > 10 and tokeniza1(value):
                # Store the key-value pair in the dictionary
                word_count[value] = key

    
# Get the number of lines
print("Number of lines in the original file:", num_lines)
          
                  
# Open the file
with open('tabelaRes.txt', 'r+') as fileR:
    for word,count in word_count.items():
        ratio=int(count)/num_lines
        
        fileR.write(f"{word}\t{ratio}\n")
    
        num_lines1 +=1

print("Number of lines in the new file:", num_lines1)


