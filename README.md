# DataScience

Foi escolhido o desafio "Segmentação dos principais assuntos das reviews
(feature review_scores_rating)".

Foram trabalhados os arquivos .csv, especificamente o arquivo: "reviews.csv.gz" em 'Amsterdam, North Holland, The Netherlands'.

Respondendo ao questionário solicitado no desafio e explicando a construção do modelo:

O objetivo foi criar um sistema de mineração de opiniões utilizando Python. Ele funciona em dois módulos, um para limpeza e padronização dos textos de comentários original e outro para agrupamento e mineração dos textos opinativos.

Capturei então uma amostra da primeira base de textos, pois se trabalhasse com muitos dados o tempo do teste seria todo consumido com o processamento, este arquivo é o '/Desafio/reviews.csv' presente aqui no repositório, que tratado pelo módulo '/Desafio/obtercsv.py' gera um novo .csv pré-processado 'reviewsFiltrado.csv' que será minerado pelo módulo seguinte.

Como estratégia, o 'reviewsFiltrado.csv' gerado possui apenas substantivos (nouns) que são os principais elementos que, do ponto de vista linguístico, identificam os assuntos tratados em um texto. Também, são excluídos os textos que não estão em inglês, pois estes devem ser tratados separadamente, já que o NLTK e o Spacy trabalham com línguas específicas. Também, são excluídos os outros campos da planilha. Para tudo isso, são utilizadas as bibliotecas de NLP do Python e tratamento de strings.

Em seguida, o módulo '/Desafio/desafio.py' explora a amostra gerada 'reviewsFiltrado.csv' e executa um algoritmo de agrupamento (k-means) com 20 grupos. O número de grupos a gerar pode ser alterado pela constante NUM_GROUPS. O número de grupos ideal é descoberto empiricamente por tentativa e  erro. Outros algoritmos que tentam descobrir o número de grupos poderia ser empregado futuramente, mas segundo os estudos que tenho feito, eles mais erram que acertam em tal tarefa de predição. 

Ainda no módulo '/Desafio/desafio.py' após o agrupamento o módulo imprime no console os grupos e os termos-substantivos mais frequentes em cada grupo, caracterizando os principais assuntos tratados em cada grupo.

Em seguida, ele imprime no console os termos-substantivos mais frequentes em cada grupo. Logicamente, se esses termos estão presentes em vários grupos eles são muito citados pelos usuário, porém alguns não têm peso semântico, como, por exemplo: 'everything', não tem alto valor informativo sozinho, ao contrário de 'room' que indica que 'o quarto de dormir' é um termo muito opinado.

Finalmente, o modelo é capaz de identificar na planilha original 'reviews.csv' em que contexto os termos que mais aparecem em grupos surgem..., no caso para evitar "poluição da tela", escolhemos só o mais frequente, mais isso poderia ser extendido para os 10 mais frequentes, por exemplo. Assim, é possível visualizar oq ue se fala sobre o termo nos textos originais. Por exmplo 'city', o que se fala sobre 'city' ? Já que ele é um termo muito frequente nos vários grupos gerados.

Apesar da amostra ser pequena em vista do volume de dados, o sistema proposto pode ser executado com volumes de dados maiores, mas o tempo de processamento deve crescer proporcionalmente. Muito pode ser feito ainda para minerar os dados com mais exatidão.

Os resultados são gerados no console, no meu caso utilizei o Eclipse, mas creio que em qualquer IDE deve funcionar.
