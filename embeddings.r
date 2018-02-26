library(wordVectors)
library(tsne)

setwd("/home/rique/Área de Trabalho/embeddings")

corpus <- "corpus/pt_processed.txt"
path_model <- "models/embeddings_wordVectors_r.bin"

if (!file.exists(corpus)) {
  #limpando os dados (retirando acentos e deixando apenas palavras)
  prep_word2vec("corpus/pt.txt", corpus, lowercase = T)
}

if (!file.exists(path_model)) {
  #MIN_COUNT: é a grequancia considerada da palavra
  #WINDOW: é a distância considerada para similaridade entre 2 palavras, como o k do k-means
  #VECTORS: número de dimensões
  model <- train_word2vec(corpus,
                          output = path_model, 
                          threads = 1, 
                          min_count = 1,
                          vectors = 100, 
                          window = 12)
}

model <- read.vectors(path_model)

closest_to(model, "azul", n = 10)

plot(model, model[["azul"]])
