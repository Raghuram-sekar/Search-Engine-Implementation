import json
import os

# Input and output files
CRAWLED_DATA_FILE = os.path.join('..', 'data', 'crawled_data.json')
PAGERANK_FILE = os.path.join('..', 'data', 'pagerank.json')

# PageRank parameters
DAMPING = 0.85
ITERATIONS = 20

# Load crawled data
with open(CRAWLED_DATA_FILE, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a mapping from URL to index
url_to_idx = {doc['url']: i for i, doc in enumerate(docs)}
N = len(docs)

# Build the link graph: for each page, list of indices it links to
out_links = []
for doc in docs:
    links = [url_to_idx[link] for link in doc.get('links', []) if link in url_to_idx]
    out_links.append(links)

# Initialize PageRank scores
pagerank = [1.0 / N] * N

for it in range(ITERATIONS):
    new_pagerank = [ (1 - DAMPING) / N ] * N
    for i in range(N):
        if out_links[i]:
            share = pagerank[i] / len(out_links[i])
            for j in out_links[i]:
                new_pagerank[j] += DAMPING * share
        else:
            # Distribute to all if no out links (dangling node)
            for j in range(N):
                new_pagerank[j] += DAMPING * (pagerank[i] / N)
    pagerank = new_pagerank

# Save PageRank scores as a dict: url -> score
pagerank_dict = {doc['url']: score for doc, score in zip(docs, pagerank)}
with open(PAGERANK_FILE, 'w', encoding='utf-8') as f:
    json.dump(pagerank_dict, f, indent=2)

print(f'PageRank calculation complete! Scores saved to {PAGERANK_FILE}') 