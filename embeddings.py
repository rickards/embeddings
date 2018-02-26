#! /usr/bin/env python
#coding: utf-8

from gensim.models import Word2Vec
import os

if not os.path.exists('models/embeddings_gensim_python.bin'):

	arq = open('corpus/pt.txt', 'r')
	texto = arq.readlines()
	arq.close()

	sentences = []
	for linha in texto :
		linha = linha.replace(".","").replace("?","").replace("!","").replace(",","")
    		sentences.append(linha.replace("\n","").split())
	
	# treinando modelo 
	#MIN_COUNT: é a grequancia considerada da palavra
        #WINDOW: é a distância considerada para similaridade entre 2 palavras, como o k do k-means
	#SIZE: número de dimensões
	#WORKERS: número de threads
	print("traning model...")
	model = Word2Vec(sentences, min_count=1)
	# salvando modelo
	model.save('models/embeddings_gensim_python.bin')



# load model
model = Word2Vec.load('models/embeddings_gensim_python.bin')

#testes
print("\nPalavras similares a 'azul':")
print(model.wv.most_similar('azul'))

print("\nPalavra fora de contexto (noite dia jantar tarde):")
print(model.wv.doesnt_match("noite dia jantar tarde".split()))

print("\nCalculo da similaridade entre amor e odio:")
print(model.wv.similarity('amor', 'odio'))

print("\nImprimindo vetor da palavra 'teste':")
print(model.wv['teste'])

print("\nPalavras mais comuns no modelo:")
for i in range(0,5):
	print(str(i)+":"+str(model.wv.index2word[i]))

print("\nPalavras menos comuns no modelo:")
for i in range(-5,0):
	print(str(i+5)+":"+str(model.wv.index2word[i]))

phrase = raw_input("\nWrite expression with words:\n")
phrase = phrase.replace("+"," + ")
phrase = phrase.replace("-"," - ")
phrase = phrase.split()

positivos = []
negativos = []
sinal='+'
for word in phrase:
	if(word=='+'):
		sinal='+'
	elif(word=='-'):
		sinal='-'
	elif(sinal=='+'):
		positivos.append(word)
	elif(sinal=='-'):
		negativos.append(word)

result_similarity = model.wv.most_similar(positive=positivos, negative=negativos, topn=3)
print(result_similarity)
