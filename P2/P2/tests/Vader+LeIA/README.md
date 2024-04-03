
                     
# Vader+LeIA - BY Diana + Bernardo

## Description

Usado para executar a análise e comparar a análise  de texto realizada pelo VADER no livro do Harry Potter em eng, e da LeIA, no livro em pt.
Para tal, é utilizada a pasta lexicons, para o LeIa, e as bibliotecas são depois importadas nos .py respetivos (`leiaHP.py` e `vaderHP.py`), sendo depois gerando um histograma de comparação, tal como o pedido no enunciado, através do ficheiro `histograma.py`.

## How to RUN

Para se executar este passo, será necessário correr os seguintes commands:
- `python3 leiaHP.py`: (executar só uma vez) que usa o `leia.py`, que temos aqui presente também, e que analisa os capítulos em português, presentes como `HPXX.txt`.
- `python3 vaderHP.py`: (executar só uma vez) que importa a biblioteca do vader e analisa os capítulos `HPXXeng.txt` presentes. 
- `python3 histograma.py`: (executar só uma vez) que tal como mencionado anteriormente, gera um histograma de comparação  entre os dois histogramas anteriores.


### NOTES

De mencionar que o livro Harry Potter and the Philosopher's Stone analisado, veio do seguinte link, o qual encontramos https://github.com/arshg285/Harry-Potter-Text-Analysis/blob/main/harry_potter_corpus/sorcerers_stone.txt.

#### Author(s):

Name               | Github 
:-----------------:|:------------------------------:
Diana PG53766      | dianamalheiro02/SPLN2024                  
Bernardo PG53699   | bernardoacosta/SPLN2324                     
                          
