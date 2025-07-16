from collections import Counter
import re
import os

def load_stopwords(stopwords_file):
    if not os.path.exists(stopwords_file):
        print(f"Warning: File '{stopwords_file}' not found. No words will be ignored.")
        return set()
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        return set(w.strip().lower() for w in f if w.strip())

def generate_ngrams(word_list, n, stopwords):
    ngrams = []
    for i in range(len(word_list) - n + 1):
        group = word_list[i:i+n]
        # If n == 1, remove if the word is a stopword
        if n == 1:
            if group[0] not in stopwords:
                ngrams.append(group[0])
        else:
            # If the first OR last word is a stopword, ignore
            if group[0] in stopwords or group[-1] in stopwords:
                continue
            ngrams.append(' '.join(group))
    return ngrams

def count_ngrams_in_file(input_file, stopwords_file):
    stopwords = load_stopwords(stopwords_file)

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = re.findall(r'\b\w+\b', text)

    counts = {
        '1-grams': Counter(generate_ngrams(words, 1, stopwords)),
        '2-grams': Counter(generate_ngrams(words, 2, stopwords)),
        '3-grams': Counter(generate_ngrams(words, 3, stopwords)),
        '4-grams': Counter(generate_ngrams(words, 4, stopwords)),
        '5-grams': Counter(generate_ngrams(words, 5, stopwords)),
    }

    return counts

def export_results(counts, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for ngram_type, counter in counts.items():
            f.write(f"{ngram_type.upper()}:\n")
            for item, qty in counter.most_common():
                if qty > 1:
                    f.write(f"{item}: {qty}\n")
            f.write("\n")

# Example usage
if __name__ == "__main__":
    input_file = 'jobs_base.txt'         
    stopwords_file = 'stopwords.txt'     
    output_file = 'results.txt'      

    results = count_ngrams_in_file(input_file, stopwords_file)

    # Print to terminal
    for ngram_type, counter in results.items():
        print(f"\n{ngram_type.upper()}:")
        for item, qty in counter.most_common():
            if qty > 1:
                print(f"{item}: {qty}")

    # Export to .txt
    export_results(results, output_file)
    print(f"\nResults exported to: {output_file}")
