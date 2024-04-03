                     
# sent_analysis - BY Diana + Bernardo

## Description

Ferramenta para análise de sentimentos feito para analisar textos em português, com suporte para emojis.
A ferramenta é composta por várias pastas, as quais são:
- `data`: contém as bibliotecas/coleções usadas
- `dist`: contém o software final
- `sent_analysis`: contém o código da aplicação em si
- `tests`: contém os ficheiros de teste para este projeto, de entre os quais temos o livro do Harry Potter fornecido nas aulas. 

## How to RUN

Para se executar este programa, será necessário correr os seguintes commands:
- Para fornecer um dicionário (palavra, sentiment) a ser usado para este projeto (executar apenas uma vez): 
Na pasta data, correr `python3 load_data.py` do qual resulta um ficheiro chamado sentiment_dict.txt.
Este processo encontra-se mais detalhado no README lá presente.

- Após a criação do dicionário, corer na pasta tests (executar apenas uma vez):
`python3 get_tweet.py`  que irá retirar os tweets de um ficheiro csv, retirado da internet e guarda o seu conteúdo. - Mais INFO no seu README.

- `flit build` (executar uma vez)

- `pip install .` 

- `sent_analysis`:
Que tem a peculariedade de perguntar, após executado, qual o tipo do ficheiro que estámos a analisar (`b` para livros (book) ou `t` para tweets), juntamente com o ficheiro txt a ser analisado.

### NOTES

Esta peculariedade do nosso programa mencionada anteriormente deve-se ao facto de os nossos portáteis já terem alguma idade e terem dificuldade em executar várias vezes o mesmo programa, e como se pretendia mais à frente se analisar por capítulos o livro do Harry Potter, teremos optado por resolver este problema desta forma. Mas seria completamente possível executá-lo com, por exemplo, `sent_analysis b HP.txt`, tendo apenas que se modificar a def main() do ficheiro __init__.py.

#### Author(s):

Name               | Github 
:---------------:  |:------------------------------:
Diana PG53766      | dianamalheiro02/SPLN2024                  
Bernardo PG53699   | bernardoacosta/SPLN2324                     
                          
