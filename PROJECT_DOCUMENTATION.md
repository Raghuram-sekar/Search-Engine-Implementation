# Search Engine Project: Step-by-Step Documentation

## What Do the Crawler, Indexer, Backend, and Frontend Do?

### 1. Crawler
- **What it does:**
  The crawler is like a robot that visits web pages on the internet, downloads their content, and saves it for you.
- **In your project:**
  - The script `crawler/simple_crawler.py` fetches a list of web pages (URLs).
  - It extracts the page title and the visible text (ignoring scripts and styles).
  - It saves this information in a file called `data/crawled_data.json`.
- **Why it’s important:**
  You need real web content to search through—this is how you collect it!

### 2. Indexer
- **What it does:**
  The indexer reads all the text collected by the crawler and builds a “searchable map” called an inverted index.
- **In your project:**
  - The script `indexer/simple_indexer.py` reads `data/crawled_data.json`.
  - It splits the text into words and creates a dictionary: Each word points to a list of documents (web pages) where it appears.
  - It saves this map in `data/inverted_index.json`.
- **Why it’s important:**
  Searching through thousands of web pages would be slow. The index makes it fast to find which pages contain your search words.

### 3. Backend (API Server)
- **What it does:**
  The backend is a web server that listens for search requests from the frontend, looks up results using the index, and sends them back.
- **In your project:**
  - The FastAPI app in `backend/app/main.py` exposes a `/search` endpoint.
  - Soon, it will use the inverted index to return real search results.

### 4. Frontend (UI)
- **What it does:**
  The frontend is the user interface—a web page where you type your search and see results.
- **In your project:**
  - The React app in `frontend/` provides a search bar and displays results from the backend.

#### How They Work Together
1. **Crawler** collects web page data.
2. **Indexer** makes that data searchable.
3. **Backend** answers search queries using the index.
4. **Frontend** lets users search and see results.

---

Welcome! This file documents every step taken to build a modern search engine from scratch, including backend, frontend, and crawling/indexing. This is designed for beginners, so nothing is skipped.

---

## 1. Project Structure

```
Search-Engine/
├── backend/      # FastAPI app (API server)
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── frontend/     # React app (Vite)
├── data/         # For storing crawled/indexed data
├── PROJECT_DOCUMENTATION.md  # This file
└── README.md
```

---

## 2. Backend Setup (FastAPI)

- **Purpose:** Handles search requests and returns results to the frontend.
- **Tech:** Python, FastAPI, Uvicorn

### Steps:
1. **Create backend folder and files:**
   - `backend/app/main.py` — FastAPI app with `/search` endpoint (returns dummy results for now).
   - `backend/requirements.txt` — lists dependencies (`fastapi`, `uvicorn`).

2. **Install dependencies:**
   ```powershell
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend server:**
   ```powershell
   python -m uvicorn app.main:app --reload
   ```
   - The server runs at [http://localhost:8000](http://localhost:8000)
   - `/search` endpoint returns example results.

---

## 3. Frontend Setup (React + Vite)

- **Purpose:** User interface for entering search queries and displaying results.
- **Tech:** React, Vite, JavaScript

### Steps:
1. **Scaffold the frontend:**
   ```powershell
   npx create-vite@latest frontend --template react
   cd frontend
   npm install
   npm run dev
   ```
   - The app runs at [http://localhost:5173](http://localhost:5173)

2. **Replace default UI:**
   - Edited `frontend/src/App.jsx` to create a modern search bar UI that calls the backend and displays results.

---

## 4. Connecting Frontend and Backend

- The frontend sends search queries to the backend `/search` endpoint.
- The backend returns results (currently dummy data).
- You can test this by running both servers and searching in the UI.

---

## 5. Next Steps: Real Search Engine

### Plan:
1. **Crawler:** Fetch real web pages and save their content.
2. **Indexer:** Build a searchable index from crawled data.
3. **Backend:** Update `/search` to return real results.

---

## 6. Useful Commands

- **Start backend:**
  ```powershell
  cd backend
  python -m uvicorn app.main:app --reload
  ```
- **Start frontend:**
  ```powershell
  cd frontend
  npm install
  npm run dev
  ```

---

## 7. Resources for Beginners
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [Vite Docs](https://vitejs.dev/)
- [Python Requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 8. What’s Next in This Project?
- We will now add a simple crawler and indexer, and document every step in this file.

---

**If you are new, read this file as you go. Every step is explained!** 

---

## 9. Adding a Simple Web Crawler

- **Purpose:** Fetches real web pages, extracts their titles and visible text, and saves the data for indexing.
- **Tech:** Python, requests, BeautifulSoup

### Files:
- `crawler/simple_crawler.py` — The crawler script.
- Output: `data/crawled_data.json` — Stores crawled page data.

### How it works:
- The script fetches a list of URLs (you can add your own).
- For each page, it extracts the title and visible text (removes scripts/styles).
- It saves the results as a JSON file for later indexing.

### How to run the crawler:
1. **Install dependencies:**
   ```powershell
   pip install requests beautifulsoup4
   ```
2. **Run the crawler script:**
   ```powershell
   cd crawler
   python simple_crawler.py
   ```
3. **Check the output:**
   - The crawled data will be saved in `../data/crawled_data.json`.
   - You can open this file to see the titles, URLs, and text content.

---

**Next:** We will build an indexer to make this data searchable! 

---

## 10. Building a Simple Indexer

- **Purpose:** Reads the crawled data and builds an inverted index (maps each word to the documents it appears in).
- **Tech:** Python, JSON

### Files:
- `indexer/simple_indexer.py` — The indexer script.
- Input: `data/crawled_data.json` — Crawled web page data.
- Output: `data/inverted_index.json` — The inverted index.

### How it works:
- Reads the crawled data (list of documents).
- For each document, splits the text into words (tokenizes).
- Builds a dictionary: each word points to a list of document indices where it appears.
- Saves the index as a JSON file for fast searching.

### How to run the indexer:
1. **Run the indexer script:**
   ```powershell
   cd indexer
   python simple_indexer.py
   ```
2. **Check the output:**
   - The inverted index will be saved in `../data/inverted_index.json`.
   - You can open this file to see which words map to which documents.

---

**Next:** We will update the backend to use this index and return real search results! 

---

## 11. Updating the Backend for Real Search

- **Purpose:** The backend now uses the real inverted index and crawled data to answer search queries.
- **Tech:** Python, FastAPI

### Files:
- `backend/app/search.py` — Loads the crawled data and index, and provides a search function.
- `backend/app/main.py` — The `/search` endpoint now uses the real search logic.

### How it works:
- When you search from the frontend, the backend looks up your query in the index.
- It returns real matching documents (title, URL, snippet) from the crawled data.

### How to use:
1. **Restart the backend server:**
   If it’s already running, stop it (Ctrl+C) and start it again:
   ```powershell
   cd backend
   python -m uvicorn app.main:app --reload
   ```
2. **Use the frontend as before:**
   - Go to [http://localhost:5173](http://localhost:5173)
   - Enter a search query. You’ll now see real results from the web pages you crawled!

---

**Congratulations! You now have a real, working search engine!** 

---

## 12. Updating the Crawler for PageRank

- **Purpose:** The crawler now also saves all outgoing links (hyperlinks) found on each page. This is needed to calculate PageRank.
- **Tech:** Python, BeautifulSoup, urllib

### What’s new:
- Each document in `data/crawled_data.json` now has a `links` field: a list of all outgoing links from that page.
- This link information will be used to build the link graph for PageRank.

### How to update your data:
1. **Rerun the crawler to update your data with links:**
   ```powershell
   cd crawler
   python simple_crawler.py
   ```
2. **Check the output:**
   - Each entry in `../data/crawled_data.json` now includes a `links` field.

---

**Next:** We will build a PageRank calculator using this link data! 

---

## 13. Calculating PageRank

- **Purpose:** Assigns an "importance score" to each page based on the link structure, using the PageRank algorithm.
- **Tech:** Python, JSON

### Files:
- `pagerank/pagerank.py` — The PageRank calculation script.
- Input: `data/crawled_data.json` — Crawled web page data (with links).
- Output: `data/pagerank.json` — PageRank scores for each page.

### How it works:
- Builds a link graph from the `links` field in each document.
- Runs the PageRank algorithm for several iterations.
- Assigns a score to each page (higher means more "important").
- Saves the scores as a dictionary: URL → score.

### How to run the PageRank script:
1. **Run the script:**
   ```powershell
   cd pagerank
   python pagerank.py
   ```
2. **Check the output:**
   - The PageRank scores will be saved in `../data/pagerank.json`.
   - You can open this file to see the scores for each URL.

---

**Next:** We will update the backend to use PageRank for ranking search results! 

---

## 14. Using PageRank to Rank Search Results

- **Purpose:** The backend now sorts search results by PageRank, so the most "important" pages appear first.
- **Tech:** Python, FastAPI

### What’s new:
- The backend loads PageRank scores from `data/pagerank.json`.
- When you search, results are sorted by PageRank (highest score first).
- Each result includes its PageRank score (for learning/demo purposes).

### How to use:
1. **Restart the backend server:**
   If it’s already running, stop it (Ctrl+C) and start it again:
   ```powershell
   cd backend
   python -m uvicorn app.main:app --reload
   ```
2. **Use the frontend as before:**
   - Go to [http://localhost:5173](http://localhost:5173)
   - Enter a search query. Results are now ranked by PageRank!

---

**You now have a real search engine with PageRank-based ranking!** 

---

## 15. Recursive Crawling (Auto-Follow Links)

- **Purpose:** The crawler now automatically follows links from each page it downloads, discovering and indexing more pages (like a real search engine spider).
- **Tech:** Python, BeautifulSoup, urllib

### What’s new:
- The crawler starts from a list of seed URLs.
- For each page, it extracts links and adds them to a queue.
- It keeps crawling new links (up to a configurable `MAX_PAGES` limit).
- It avoids visiting the same page twice.

### How to use recursive crawling:
1. **Set your seed URLs and max pages:**
   - Edit `SEED_URLS` and `MAX_PAGES` at the top of `crawler/simple_crawler.py` as desired.
2. **Run the crawler:**
   ```powershell
   cd crawler
   python simple_crawler.py
   ```
3. **Check the output:**
   - The crawler will save up to `MAX_PAGES` pages in `../data/crawled_data.json`.
   - You can now index and search a much larger set of pages!

---

**Next:** We will re-index your new data and continue with the next improvements! 

---

## 16. TF-IDF Scoring for Better Search Relevance

- **Purpose:** The indexer now computes TF-IDF scores for each word in each document, making search results more relevant.
- **Tech:** Python, math, JSON

### What’s new:
- The indexer calculates TF-IDF (Term Frequency-Inverse Document Frequency) scores for every word in every document.
- These scores measure how important a word is to a document, compared to all documents.
- The scores are saved in `data/tfidf.json`.

### How to use TF-IDF:
1. **Re-run the indexer to compute TF-IDF scores:**
   ```powershell
   cd indexer
   python simple_indexer.py
   ```
2. **Check the output:**
   - The TF-IDF scores will be saved in `../data/tfidf.json`.
   - You can open this file to see the scores for each word in each document.

---

**Next:** We will update the backend to use TF-IDF for ranking search results! 

---

## 17. Using TF-IDF (and PageRank) to Rank Search Results

- **Purpose:** The backend now uses TF-IDF scores (and PageRank as a tiebreaker) to rank search results, making them much more relevant.
- **Tech:** Python, FastAPI

### What’s new:
- The backend loads TF-IDF scores from `data/tfidf.json`.
- When you search, results are sorted by TF-IDF (most relevant first), with PageRank as a secondary sort.
- Each result includes its TF-IDF and PageRank scores (for learning/demo purposes).

### How to use:
1. **Restart the backend server:**
   If it’s already running, stop it (Ctrl+C) and start it again:
   ```powershell
   cd backend
   python -m uvicorn app.main:app --reload
   ```
2. **Use the frontend as before:**
   - Go to [http://localhost:5173](http://localhost:5173)
   - Enter a search query. Results are now ranked by TF-IDF and PageRank!

---

**Your search engine is now much smarter and more relevant!** 