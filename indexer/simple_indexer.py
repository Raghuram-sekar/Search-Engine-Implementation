import json
import os
import re
from collections import defaultdict
import math

# Input and output files
CRAWLED_DATA_FILE = os.path.join('..', 'data', 'crawled_data.json')
INDEX_FILE = os.path.join('..', 'data', 'inverted_index.json')
TFIDF_FILE = os.path.join('..', 'data', 'tfidf.json')

# Helper function to tokenize text (split into lowercase words)
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Load crawled data
with open(CRAWLED_DATA_FILE, 'r', encoding='utf-8') as f:
    docs = json.load(f)

N = len(docs)

# Build inverted index: word -> list of doc indices
inverted_index = defaultdict(list)
# For TF calculation: doc_id -> word -> count
doc_word_counts = []
for idx, doc in enumerate(docs):
    words = tokenize(doc['text'])
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    doc_word_counts.append(word_count)
    for word in set(words):
        inverted_index[word].append(idx)

# Save the inverted index
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    json.dump(inverted_index, f, ensure_ascii=False, indent=2)

# Compute TF-IDF scores: tfidf[doc_id][word] = score
tfidf = [{} for _ in range(N)]
for word, doc_indices in inverted_index.items():
    df = len(doc_indices)  # Document frequency
    idf = math.log((N + 1) / (df + 1)) + 1  # Smoothed IDF
    for doc_id in doc_indices:
        tf = doc_word_counts[doc_id][word] / sum(doc_word_counts[doc_id].values())
        tfidf[doc_id][word] = tf * idf

# Save TF-IDF scores
with open(TFIDF_FILE, 'w', encoding='utf-8') as f:
    json.dump(tfidf, f, ensure_ascii=False, indent=2)

print(f'Indexing complete! Inverted index saved to {INDEX_FILE}, TF-IDF scores saved to {TFIDF_FILE}') 