## Descrição
Programa desenvolido como parte do processo seletivo para estágio em NLP.

Este programa recebe um arquivo de reviews de produtos como entrada e gera dois arquivos de saída, o primeiro (reviews_anotados.txt) contendo a classe gramátical de cada uma das palavras dos reviews e o segundo (trechos_identificados.txt) contendo os trechos que seguem um dos padrões: \<SUBSTANTIVO\> + \<ADJETIVO\> ou \<SUBSTANTIVO\> + \<VERBO\> + \<ADJETIVO\>

## Pré-requisitos
* [python 3](https://www.python.org/download/releases/3.0/)
* [nlpnet](http://nilc.icmc.usp.br/nlpnet/)

## Execução
Para executar o programa basta passar o diretório do arquivo de reviews como parâmetro na execução, caso o diretório não seja informado o programa irá assumir que o arquivo de reviews está no diretório raiz da execução com o nome de "reviews_test_estag_nlp.txt". Exemplos de execução:
```bash
$ python3 psel_nlp.py reviews_test_estag_nlp.txt
```
ou
```bash
$ python3 psel_nlp.py
```

## Referências
O tagger utilizado para dizer a classe gramátical de cada uma das palavras faz parte da biblioteca [nlpnet](http://nilc.icmc.usp.br/nlpnet/) (Natural Language Processing with neural networks), desenvolvida pelo [NILC](http://www.nilc.icmc.usp.br/nilc/index.php) (Núcleo Interinstitucional de Linguística Computacional).
