import re
from collections import Counter

TOP_K = 20
N_GRAM = 3


# Generate all the n-grams for value n
def ngrams(n, text):
    for i in range(len(text) - n + 1):
        # Ignore n-grams containing white space
        if not re.search(r"\s", text[i : i + n]):
            yield text[i : i + n]


# Read the data from the ciphertext
with open("ciphertext.txt") as f:
    text = f.read()

# Count, sort, and print out the n-grams
for N in range(N_GRAM):
    print("-------------------------------------")
    print(f"{N + 1}-gram (top {TOP_K}):")
    counts = Counter(ngrams(N + 1, text))  # Count
    sorted_counts = counts.most_common(TOP_K)  # Sort
    for ngram, count in sorted_counts:
        print(f"{ngram}: {count}")  # Print
