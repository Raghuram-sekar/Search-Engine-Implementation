import os
import json
import re

# Paths to data files
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
CRAWLED_DATA_FILE = os.path.join(DATA_DIR, 'crawled_data.json')
INDEX_FILE = os.path.join(DATA_DIR, 'inverted_index.json')
PAGERANK_FILE = os.path.join(DATA_DIR, 'pagerank.json')
TFIDF_FILE = os.path.join(DATA_DIR, 'tfidf.json')

# Load crawled documents
with open(CRAWLED_DATA_FILE, 'r', encoding='utf-8') as f:
    documents = json.load(f)

# Load inverted index
with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    inverted_index = json.load(f)

# Load PageRank scores
with open(PAGERANK_FILE, 'r', encoding='utf-8') as f:
    pagerank_scores = json.load(f)

# Load TF-IDF scores
with open(TFIDF_FILE, 'r', encoding='utf-8') as f:
    tfidf_scores = json.load(f)

# Helper: tokenize query string
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Main search function
def search_documents(query):
    words = tokenize(query)
    if not words:
        return []
    # Find document indices that contain all query words
    doc_sets = []
    for word in words:
        doc_sets.append(set(inverted_index.get(word, [])))
    if not doc_sets:
        return []
    matching_indices = set.intersection(*doc_sets)
    # Prepare results with TF-IDF and PageRank
    results = []
    for idx in matching_indices:
        doc = documents[int(idx)]
        snippet = doc['text'][:200] + ('...' if len(doc['text']) > 200 else '')
        pr_score = pagerank_scores.get(doc['url'], 0)
        tfidf_score = sum(tfidf_scores[int(idx)].get(word, 0) for word in words)
        results.append({
            'title': doc['title'],
            'url': doc['url'],
            'snippet': snippet,
            'pagerank': pr_score,
            'tfidf': tfidf_score
        })
    # Sort by combined score: TF-IDF (primary), PageRank (secondary)
    results.sort(key=lambda r: (r['tfidf'], r['pagerank']), reverse=True)
    return results 