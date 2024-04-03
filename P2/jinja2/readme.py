#!/usr/bin/env python3

'''
DESCRIPTION
   This script uses jinja2 and glob as a way to make a template for a README.md file.
   Jinja2 is used for the template and variable substitution, while glob is used to find all the .py files in the current directory.
   With that, we are able to make a README of the first file found, using the template below. 
 
RUN
   Run using this command: python3 readme.py > README.md
   
NOTES   
   It is also important to mention that the dependencies, as well as the author and email need changing.
   And don't forget to only use this when you have a file.py in the directory and that file has a __version__, please, or else I assume 1.0.0.
''' 

import jinja2
from glob import glob   

# Get list of Python files in the directory
python_files = glob("*.py")

# Determine project name based on the first Python file found or user input
if python_files:
    name = python_files[0].replace(".py", "")
else:
    name = input("Input Module Name: ")

pp = jinja2.Template('''
                     
# {{NAME}} - BY {{autores}}

## Description

Ferramenta para FIXME
A ferramenta é composta por várias pastas, as quais são:
- 
-

- FIXME -

## How to RUN

Para se executar este programa, será necessário correr os seguintes commands:
-
-
-

- FIXME - 

### NOTES

FIXME

#### Author(s):

Name         | Github 
:-----------:|:------------------------------:
{{autor1}}   | {{github1}}                  
{{autor2}}   | {{github2}}                     
                          
''')

#FIX ME
print(pp.render({"name":name,"autores":"Diana + Bernardo","autor1":"Diana PG53766","autor2":"Bernardo PG53699","github1":"dianamalheiro02/SPLN2024","github2":"bernardoacosta/SPLN2324"}))

