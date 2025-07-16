from collections import Counter
import re
import os

def carregar_irrelevantes(arquivo_irrelevantes):
    if not os.path.exists(arquivo_irrelevantes):
        print(f"Aviso: Arquivo '{arquivo_irrelevantes}' não encontrado. Nenhuma palavra será ignorada.")
        return set()
    with open(arquivo_irrelevantes, 'r', encoding='utf-8') as f:
        return set(p.strip().lower() for p in f if p.strip())

def gerar_ngrams(lista_palavras, n, irrelevantes):
    ngrams = []
    for i in range(len(lista_palavras) - n + 1):
        grupo = lista_palavras[i:i+n]
        # Se n == 1, removemos se a palavra for irrelevante
        if n == 1:
            if grupo[0] not in irrelevantes:
                ngrams.append(grupo[0])
        else:
            # Se a primeira OU a última palavra for uma irrelevante, ignorar
            if grupo[0] in irrelevantes or grupo[-1] in irrelevantes:
                continue
            ngrams.append(' '.join(grupo))
    return ngrams

def contar_ngrams_arquivo(caminho_arquivo, arquivo_irrelevantes):
    irrelevantes = carregar_irrelevantes(arquivo_irrelevantes)

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read().lower()

    palavras = re.findall(r'\b\w+\b', texto)

    contagem = {
        '1-gramas': Counter(gerar_ngrams(palavras, 1, irrelevantes)),
        '2-gramas': Counter(gerar_ngrams(palavras, 2, irrelevantes)),
        '3-gramas': Counter(gerar_ngrams(palavras, 3, irrelevantes)),
        '4-gramas': Counter(gerar_ngrams(palavras, 4, irrelevantes)),
        '5-gramas': Counter(gerar_ngrams(palavras, 5, irrelevantes)),
    }

    return contagem

def exportar_resultado(contagens, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for tipo, contador in contagens.items():
            f.write(f"{tipo.upper()}:\n")
            for item, qtd in contador.most_common():
                if qtd > 1:
                    f.write(f"{item}: {qtd}\n")
            f.write("\n")

# Exemplo de uso
if __name__ == "__main__":
    arquivo_base = 'base_vagas.txt'         
    arquivo_irrelevantes = 'palavras_irrelevantes.txt'     
    arquivo_saida = 'resultado.txt'      

    resultado = contar_ngrams_arquivo(arquivo_base, arquivo_irrelevantes)

    # Mostra no terminal
    for tipo, contador in resultado.items():
        print(f"\n{tipo.upper()}:")
        for item, qtd in contador.most_common():
            if qtd > 1:
                print(f"{item}: {qtd}")

    # Exporta para .txt
    exportar_resultado(resultado, arquivo_saida)
    print(f"\nResultado exportado para: {arquivo_saida}")
