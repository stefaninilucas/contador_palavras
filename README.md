### Análise de Termos Frequentes em Descrições de Vagas

 Este projeto foi criado com o objetivo de analisar descrições de vagas de emprego (por exemplo, coletadas do LinkedIn) e identificar as palavras e expressões mais recorrentes nos anúncios. Essa análise ajuda candidatos a ajustarem seus currículos e perfis profissionais com base nos termos mais buscados, aumentando suas chances de compatibilidade ("match") com as oportunidades.


 #### Funcionalidades

- Contagem de palavras individuais (1-gramas) e expressões compostas (2-gramas a 5-gramas).

- Filtro inteligente de palavras irrelevantes definidas em um arquivo externo.

- Nas expressões (n-gramas), palavras irrelevantes são ignoradas apenas se estiverem no início ou no fim da expressão — permitindo capturar termos relevantes mesmo com preposições no meio.

- Exportação dos resultados para um arquivo .txt, organizado por tipo de expressão e ordenado por frequência.


#### Motivação

Ajustar seu currículo às palavras mais recorrentes nas vagas de interesse é uma maneira prática de:

- Aumentar a compatibilidade com os filtros de recrutadores (como ATS),

- Tornar seu perfil mais atrativo para recrutadores e sistemas automatizados,

- Alinhar melhor sua apresentação com as expectativas do mercado.


#### Requisitos

- Python 3.7 ou superior

- Apenas bibliotecas padrão (collections, re, os)


#### Como usar

##### Clone este repositório:

1. git clone https://github.com/stefaninilucas/contador_palavras.git

1. cd analise-vagas

##### Prepare seus arquivos:

1. Adicione ao arquivo "base_vagas.txt" as descrições das vagas de seu interesse (você pode copiar e colar diretamente do LinkedIn).

1. Adicione ao arquivo "palavras_irrelevantes.txt" as palavras que devem ser desconsideradas na análise (uma por linha).

##### Execute o script:

1. python contador_palavras.py

1. Verifique o arquivo resultado.txt gerado com os termos mais frequentes.

##### Exemplo de saída (resultado.txt)

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



