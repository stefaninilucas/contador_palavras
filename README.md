### Análise de Termos Frequentes em Descrições de Vagas

 Este projeto foi criado com o objetivo de analisar descrições de vagas de emprego (por exemplo, coletadas do LinkedIn) e identificar as palavras e expressões mais recorrentes nos anúncios. Essa análise ajuda candidatos a ajustarem seus currículos e perfis profissionais com base nos termos mais buscados, aumentando suas chances de compatibilidade ("match") com as oportunidades.

 #### Funcionalidades

Contagem de palavras individuais (1-gramas) e expressões compostas (2-gramas e 3-gramas).

Filtro inteligente de palavras irrelevantes (stopwords) definidas em um arquivo externo.

Nas expressões (n-gramas), palavras irrelevantes são ignoradas apenas se estiverem no início ou no fim da expressão — permitindo capturar termos relevantes mesmo com preposições no meio.

Exportação dos resultados para um arquivo .txt, organizado por tipo de expressão e ordenado por frequência.

#### Motivação
Ajustar seu currículo às palavras mais recorrentes nas vagas de interesse é uma maneira prática de:

Aumentar a compatibilidade com os filtros de recrutadores (como ATS),

Tornar seu perfil mais atrativo para recrutadores e sistemas automatizados,

Alinhar melhor sua apresentação com as expectativas do mercado.

#### Requisitos
Python 3.7 ou superior
Apenas bibliotecas padrão (collections, re, os)

#### Como usar

Clone este repositório:

git clone https://github.com/seuusuario/analise-vagas.git
cd analise-vagas
Prepare seus arquivos:

Crie um arquivo seuarquivo.txt contendo várias descrições de vagas (você pode copiar e colar diretamente do LinkedIn).

Crie um arquivo stopwords.txt com palavras que devem ser desconsideradas na análise (uma por linha).

Execute o script:

python analise_vagas.py
Verifique o arquivo resultado.txt gerado com os termos mais frequentes.

Exemplo de saída (resultado.txt)

1-GRAMAS:
dados: 12
projetos: 8
relatórios: 6

2-GRAMAS:
análise de: 5
modelagem de: 4

3-GRAMAS:
análise de dados: 3
ferramentas de bi: 2





