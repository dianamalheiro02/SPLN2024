              
# get_tweet - BY Diana + Bernardo

## Description

Ferramenta para extrair tweets (texto/contúdo) de um determinado ficheiro, neste caso CSV, o qual encontramos na internet, no kagle (https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis ).
A ferramenta é simples, servindo apenas para abrir o ficheiro e retirar do mesmo a segunda coluna, onde está presente o tweet na sua totalidade, não apenas o ID.


## How to RUN

Para se executar este programa, será necessário correr os seguintes commands:
-`python3 get_tweet.py Test.csv` (executar apenas uma vez)

### NOTES

É de notar que se pretendemos utilizar a API do Twitter para obter tweets, teriamos apenas que, por cada ID presente no ficheiro (1º coluna), procurar o https://twitter.com/anyuser/status/ID do mesmo, mas visto já possuirmos o seu conteúdo neste dataset do kagle, não vimos a necessidade de tal.

#### Author(s):

Name               | Github 
:-----------------:|:------------------------------:
Diana PG53766      | dianamalheiro02/SPLN2024                  
Bernardo PG53699   | bernardoacosta/SPLN2324                     
                          
