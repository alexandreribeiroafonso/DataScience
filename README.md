# DataScience

Foi escolhido o desafio "Segmentação dos principais assuntos das reviews
(feature review_scores_rating)".

Foram trabalhados os arquivos .csv, especificamente o arquivo: "reviews.csv.gz" em 'Amsterdam, North Holland, The Netherlands'.

Respondendo ao questionário solicitado no desafio e explicando a construção do modelo:

O objetivo foi criar um sistema de mineração de opiniões utilizando Python. Ele funciona em dois módulos, um para limpeza e padronização dos textos de comentários originais e outro para agrupamento e mineração dos textos opinativos.

Capturei então, uma amostra da primeira base de textos, pois se trabalhasse com muitos dados o tempo do teste seria praticamente todo consumido com o processamento, este arquivo de amostras é o '/Desafio/reviews.csv' presente aqui no repositório, que tratado pelo módulo '/Desafio/obtercsv.py' gera um novo .csv pré-processado chamado 'reviewsFiltrado.csv' que será minerado pelo módulo seguinte.

Como estratégia de Data Mining, o 'reviewsFiltrado.csv' gerado possui apenas substantivos (nouns) sendo eles os principais elementos que, do ponto de vista linguístico, identificam os assuntos tratados em um texto. Também, são excluídos os textos que não estão em inglês, pois estes devem ser tratados separadamente, já que as ferramentas NLTK e o Spacy trabalham com línguas específicas. Também, são excluídos os outros campos da planilha original. Para tal tarefa, são utilizadas as bibliotecas de NLP do Python e tratamento de listas/strings.

Em seguida, o módulo '/Desafio/desafio.py' explora a amostra gerada 'reviewsFiltrado.csv' e executa um algoritmo de agrupamento (k-means) com 20 grupos. O número de grupos a gerar pode ser alterado pela constante NUM_GROUPS do código. O número de grupos ideal é descoberto empiricamente, por tentativa e  erro. Outros algoritmos que tentam descobrir o número de grupos poderiam ser empregado futuramente, mas segundo os estudos que tenho feito, eles mais erram que acertam em tal atividade de predição.

No K-Means é utilizada a pesagem TF.IDF para pesar os termos, e as stopwords do inglês são retiradas. 

Ainda no módulo '/Desafio/desafio.py', após o agrupamento, o módulo imprime na console os grupos e os termos-substantivos mais frequentes em cada grupo, de forma ordenada, caracterizando os principais assuntos tratados em cada grupo.

Em seguida, o módulo em execução imprime na console os termos-substantivos mais frequentes em grupos (dessa vez os que mais estão em grupos). Logicamente, se esses termos estão presentes em vários grupos eles são muito citados pelos usuário, porém alguns não têm peso semântico, como, por exemplo: 'everything', não tem alto valor informativo sozinho, ao contrário de 'room' que indica que 'o quarto de dormir' é um termo muito comentado.

Finalmente, o modelo é capaz de identificar na planilha original 'reviews.csv' em que contexto os termos que mais aparecem em grupos surgem..., no caso para evitar "poluição da tela", escolhemos só o mais frequente, mais isso poderia ser estendido para os 10 mais frequentes. Assim, é possível visualizar sobre o que se fala sobre o termo-substantivo nos textos originais, ou seja identificamos agora o contexto desses substantivos. Por exmplo, 'city' é um termo frequente, mas o que se fala sobre 'city'? 

Apesar da amostra ser pequena em vista do volume de dados, o sistema proposto pode ser executado com volumes de dados maiores, mas o tempo de processamento deve crescer proporcionalmente. Muito pode ser feito ainda para minerar os dados com mais exatidão.

Os resultados são gerados na console, no meu caso utilizei o Eclipse, mas creio que em qualquer IDE deve funcionar.
