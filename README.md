### Análise de Termos Frequentes em Descrições de Vagas

 Este projeto foi criado com o objetivo de analisar descrições de vagas de emprego (por exemplo, coletadas do LinkedIn) e identificar as palavras e expressões mais recorrentes nos anúncios. Essa análise ajuda candidatos a ajustarem seus currículos e perfis profissionais com base nos termos mais buscados, aumentando suas chances de compatibilidade ("match") com as oportunidades.


 #### Funcionalidades

- Conta palavras individuais (unigramas) e combinações de palavras (n-gramas), como "power bi", "analista de dados", etc.

- Analisa automaticamente até o maior n-grama relevante (ou limitado pelo usuário).

- Permite configurar um número mínimo de repetições para exibir os termos.

- Filtro inteligente de palavras irrelevantes definidas em um arquivo externo - "stopwords.txt".

- Nas expressões n-gramas (2 ou mais palavras), as palavras irrelevantes (stopwords) só são ignoradas se estiverem no início ou no fim da expressão.

- Exportação dos resultados para um arquivo - "results.txt", organizado por tipo de expressão e ordenado por frequência.


#### Por que ignorar stopwords apenas nas extremidades

Ao montar expressões como "analista de dados", a palavra "de" é importante dentro do contexto, mesmo sendo uma stopword. Por isso, o script só ignora expressões como "de dados" ou "analista de" — onde o termo fraco está na borda e provavelmente não agrega significado ao conjunto.


#### Motivação

Ajustar seu currículo às palavras mais recorrentes nas vagas de interesse é uma maneira prática de:

- Aumentar a compatibilidade com os filtros de recrutadores (como ATS),

- Tornar seu perfil mais atrativo para recrutadores e sistemas automatizados,

- Alinhar melhor sua apresentação com as expectativas do mercado.


#### Requisitos

- Python 3.6 ou superior

- Apenas bibliotecas padrão (collections, re, os)


#### Como usar

##### Clone este repositório:

1. git clone https://github.com/stefaninilucas/job_keyword_analyzer.git

1. cd job_keyword_analyzer

##### Prepare seus arquivos:

1. Adicione ao arquivo "jobs_description.txt" as descrições das vagas de seu interesse (você pode copiar e colar diretamente do LinkedIn).

1. Adicione ao arquivo "stopwords.txt" as palavras que devem ser desconsideradas na análise (uma por linha).

##### Execute o script:

1. python main.py

1. Você será perguntado:

    - Quantas vezes um termo precisa se repetir para ser exibido.

    - Qual o maior tamanho de expressão (n-grama) a ser analisado (ou deixe em branco para automático).

1. Verifique o arquivo "result.txt" gerado com os termos mais frequentes.

##### Exemplo de saída (result.txt)

1-GRAMAS:
dados: 12  
projetos: 8  
relatórios: 6  

2-GRAMAS:
microsoft azure: 4  
power bi: 3  
pacote office: 2  

3-GRAMAS:
governança de dados: 4  
visualização de dados: 3  

4-GRAMAS:
aplicação de técnicas estatísticas: 2  

5-GRAMAS:
gestão e governança de dados: 3  



