# coding: utf-8

import nltk
import nlpnet

nltk.download('punkt') # download que a nlpnet necessita
nlpnet.set_data_dir('pos-pt/') # seta diretório para alguns arquivos que a nlpnet necessita
tagger = nlpnet.POSTagger() # instância o tagger


# tenta abrir o arquivo de reviews pelo primeiro parâmetro do terminal
# se não conseguir tenta abrir com o nome 'reviews_test_estag_nlp.txt'
import sys

try:
    path = sys.argv[1]
    reviews = open(path, 'r')
except Exception as e:
    try:
        reviews = open('reviews_test_estag_nlp.txt', 'r')
    except:
        print('Erro ao abrir arquivo: ', e)
        sys.exit()

# linhas anotadas do arquivo
anotado = []

# trechos que devem ser identificados
trechos = []

# para cada review anota as classes e busca pelos padrões
for review in reviews:

    # remove reviews com aspas duplas ou simples
    review = review.replace('"', '').replace("'", '')

    # anota as classes
    tags = tagger.tag(review)[0]
    anotado.append(tags)

    # percorre as tags tentando encontrar os padrões N+ADJ ou N+V+ADJ
    for i in range(len(tags)-2):

        # pega as 3 primeiras palavras (do review) e suas classes para tentar identificar um dos padrões
        w0 = tags[i]
        w1 = tags[i+1]
        w2 = tags[i+2]

        # se N+ADJ salva o trecho
        if w0[1]=='N' and w1[1]=='ADJ':
            trechos.append(w0[0] + ' ' + w1[0])

        # se N+V+ADJ salva o trecho    
        elif w0[1]=='N' and w1[1]=='V' and w2[1]=='ADJ':
            trechos.append(w0[0] + ' ' + w1[0] + ' ' + w2[0])

# grava os reviews anotados no arquivo reviews_anotados.txt
with open("reviews_anotados.txt", 'w') as out:
    for line in anotado:
        out.write(str(line).replace('[', '').replace(']', '') + '\n')
print("Arquivo reviews_anotados.txt gerado.")


# grava os trechos identificados no arquivo trechos_identificados.txt
with open("trechos_identificados.txt", 'w') as out:
    for line in trechos:
        out.write(line + '\n')
print("Arquivo trechos_identificados.txt gerado.")

