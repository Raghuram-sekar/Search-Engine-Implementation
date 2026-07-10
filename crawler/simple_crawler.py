import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime

# Seed URLs to start crawling from
SEED_URLS = [
    'https://www.wikipedia.org/',
    'https://www.python.org/'
]

# Output file
OUTPUT_FILE = os.path.join('..', 'data', 'crawled_data.json')

# Maximum number of pages to crawl (to avoid infinite crawling)
MAX_PAGES = 20

# Helper function to extract visible text from HTML
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(['script', 'style']):
        script.decompose()
    text = soup.get_text(separator=' ', strip=True)
    return text

# Helper function to extract outgoing links from a page
def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        full_url = urljoin(base_url, href)
        if urlparse(full_url).scheme in ('http', 'https'):
            links.add(full_url)
    return list(links)

# Main recursive crawling logic
visited = set()
queue = list(SEED_URLS)
results = []

while queue and len(results) < MAX_PAGES:
    url = queue.pop(0)
    if url in visited:
        continue
    print(f'Crawling: {url}')
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No Title'
        text = extract_text(resp.text)
        links = extract_links(resp.text, url)
        crawled_at = datetime.utcnow().isoformat() + 'Z'
        results.append({
            'url': url,
            'title': title,
            'text': text[:2000],
            'links': links,
            'crawled_at': crawled_at
        })
        for link in links:
            if link not in visited and link not in queue and len(results) + len(queue) < MAX_PAGES:
                queue.append(link)
    except Exception as e:
        print(f'Failed to crawl {url}: {e}')
    visited.add(url)
    time.sleep(0.5)

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f'Recursive crawling complete! {len(results)} pages saved to {OUTPUT_FILE}') 