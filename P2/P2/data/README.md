          
# load_data - BY Diana + Bernardo

## Description

Ferramenta para carregar os dados presentes nas coleções, retiradas do LeIA e outras até próprias, e armazená-las em um só ficheiro, em um só dicionário (sentiment_dict.txt).
Como tal, a ferramenta lida com várias coleções, as quais são:
- `booster`: (retirada da LeIA) contém booster words.
- `expressions`: (gerada com ajuda do ChatGPT) contém expressões portuguesas, marcadas como POS e NEG.
- `lex`: (retirada da LeIA) contém uma série de palavras e o seu respetivo sentimento, o que corresponde às 2 primeiras colunas da coleção do LeIA, tendo optado por ignorar as restantes, que mostram, por exemplo a atribuição que pessoas deram de forma indivídual, etc.
- `negate`: (retirada da LeIA) contém negações e expressões negativas.
Podendo até, no futuro, lidar com mais, se tal for pretendido, e as quais teriamos apenas que ler e adicionar ao ficheiro output.

## How to RUN

Para se executar este programa, será necessário correr os seguintes commands:
- Instalar o spellChecker, que é utilizado para fazer a correção das palavras das coleções, visto estas estarem com erros ortográficos: `pip install spellChecker` (executar apenas uma vez)
-  `python3 load_data.py` (executar só uma vez, e ter em atenção que demora um bocado a executar)

### NOTES

Teremos nesta pasta a coleção `emoji` também mas, ter em atenção que a mesma não está a ser usada aqui, sendo apenas usada no __init__.py, para tornar os emojis presentes nos textos a sua descrição fornecida aqui.

De notar que optamos por correr o spellChecker apenas na coleção lex, alterando à mão as outras coleções, visto estas serem mais pequenas e mais fáceis de corrigir.

É também importante mencionar que, face ao spellchecker não reconhecer emoticons, nem ser capaz de corrigir expressões com mais de 1 palavra, quando o mesmo retorna None, colocamos na mesma as palavras no ficheiro gerado (sentiment_dict.txt), assumindo que estas já estão corretas, o que sabemos que nem sempre pode ser o caso.

Por sua vez, queremos só mencionar que, quando se corre o comando python3 mencionado em cima, que teremos a existência de vários prints a nos dar feedback, simplesmente para tornar este processo tedioso mais interativo.

#### Author(s):

Name               | Github 
:-----------------:|:------------------------------:
Diana PG53766      | dianamalheiro02/SPLN2024                  
Bernardo PG53699   | bernardoacosta/SPLN2324                     
                          
