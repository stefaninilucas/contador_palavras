from collections import Counter
import re
import os

def carregar_stopwords(caminho_stopwords):
    if not os.path.exists(caminho_stopwords):
        print(f"Aviso: Arquivo '{caminho_stopwords}' não encontrado. Nenhuma palavra será ignorada.")
        return set()
    with open(caminho_stopwords, 'r', encoding='utf-8') as f:
        return set(p.strip().lower() for p in f if p.strip())

def gerar_ngrams(lista_palavras, n, stopwords):
    ngrams = []
    for i in range(len(lista_palavras) - n + 1):
        grupo = lista_palavras[i:i+n]
        # Se n == 1, removemos se a palavra for stopword
        if n == 1:
            if grupo[0] not in stopwords:
                ngrams.append(grupo[0])
        else:
            # Se a primeira OU a última palavra for uma stopword, ignorar
            if grupo[0] in stopwords or grupo[-1] in stopwords:
                continue
            ngrams.append(' '.join(grupo))
    return ngrams

def contar_ngrams_arquivo(caminho_arquivo, caminho_stopwords):
    stopwords = carregar_stopwords(caminho_stopwords)

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read().lower()

    palavras = re.findall(r'\b\w+\b', texto)

    contagem = {
        '1-gramas': Counter(gerar_ngrams(palavras, 1, stopwords)),
        '2-gramas': Counter(gerar_ngrams(palavras, 2, stopwords)),
        '3-gramas': Counter(gerar_ngrams(palavras, 3, stopwords)),
    }

    return contagem

def exportar_resultado(contagens, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        for tipo, contador in contagens.items():
            f.write(f"{tipo.upper()}:\n")
            for item, qtd in contador.most_common():
                if qtd > 1:
                    f.write(f"{item}: {qtd}\n")
            f.write("\n")

# Exemplo de uso
if __name__ == "__main__":
    caminho_texto = 'base_dados_texto.txt'         # Substitua pelo seu arquivo .txt
    caminho_stopwords = 'palavras_desconsideradas.txt'      # Substitua pelo seu stopwords.txt
    caminho_saida = 'resultado.txt'          # Arquivo de saída

    resultado = contar_ngrams_arquivo(caminho_texto, caminho_stopwords)

    # Mostra no terminal
    for tipo, contador in resultado.items():
        print(f"\n{tipo.upper()}:")
        for item, qtd in contador.most_common():
            if qtd > 1:
                print(f"{item}: {qtd}")

    # Exporta para .txt
    exportar_resultado(resultado, caminho_saida)
    print(f"\nResultado exportado para: {caminho_saida}")
