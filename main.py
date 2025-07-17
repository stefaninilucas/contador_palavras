from collections import Counter
import re
import os

def load_stopwords(stopwords_file):
    if not os.path.exists(stopwords_file):
        print(f"Aviso: Arquivo '{stopwords_file}' não encontrado. Nenhuma palavra será ignorada.")
        return set()
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        return set(w.strip().lower() for w in f if w.strip())

def generate_ngrams(word_list, n, stopwords):
    ngrams = []
    for i in range(len(word_list) - n + 1):
        group = word_list[i:i+n]
        # Se n == 1, remove se a palavra for uma stopword
        if n == 1:
            if group[0] not in stopwords:
                ngrams.append(group[0])
        else:
            # Se a primeira OU última palavra for uma stopword, ignora
            if group[0] in stopwords or group[-1] in stopwords:
                continue
            ngrams.append(' '.join(group))
    return ngrams

def count_ngrams_in_file(input_file, stopwords_file, min_repeats=2, max_n=None):
    stopwords = load_stopwords(stopwords_file)

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = re.findall(r'\b\w+\b', text)

    counts = {}
    n = 1
    while True:
        ngram_list = generate_ngrams(words, n, stopwords)
        counter = Counter(ngram_list)
        # Só adiciona se houver pelo menos um n-grama com contagem >= min_repeats
        if any(qty >= min_repeats for qty in counter.values()):
            counts[f'{n}-gramas'] = counter
            n += 1
            if max_n is not None and n > max_n:
                break
        else:
            break

    return counts

def export_results(counts, output_file, min_repeats=2):
    with open(output_file, 'w', encoding='utf-8') as f:
        for ngram_type, counter in counts.items():
            f.write(f"{ngram_type.upper()}:\n")
            for item, qty in counter.most_common():
                if qty >= min_repeats:
                    f.write(f"{item}: {qty}\n")
            f.write("\n")

# Função principal para executar o script
if __name__ == "__main__":
    input_file = 'jobs_description.txt'         
    stopwords_file = 'stopwords.txt'     
    output_file = 'results.txt'      


    min_repeats = int(input("Mostrar apenas termos que se repetem pelo menos quantas vezes? [padrão=2]: ") or 2)
    max_n_input = input("Até qual N-grama deseja analisar? (deixe em branco para automático): ")
    max_n = int(max_n_input) if max_n_input.strip() else None

    results = count_ngrams_in_file(input_file, stopwords_file, min_repeats=min_repeats, max_n=max_n)

    # Imprimir no terminal
    for ngram_type, counter in results.items():
        print(f"\n{ngram_type.upper()}:")
        for item, qty in counter.most_common():
            if qty >= min_repeats:
                print(f"{item}: {qty}")

    # Exportar para .txt
    export_results(results, output_file, min_repeats=min_repeats)
    print(f"\nResultados exportados para: {output_file}")
