# Search Engine Project
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green.svg)

A modern, full-stack search engine project with a FastAPI backend and React frontend.

## Project Structure

```
Search-Engine/
├── backend/      # FastAPI app (API server)
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── frontend/     # React app (to be created)
├── data/         # For storing crawled/indexed data (to be used later)
└── README.md
```

## Running the Backend (API)

1. Open a terminal and navigate to `backend`:
   ```sh
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
2. The API will be available at [http://localhost:8000](http://localhost:8000)

## Running the Frontend (UI)

1. The frontend will be a React app (instructions will be added after scaffolding).

---

## Next Steps
- Scaffold the React frontend
- Connect frontend to backend
- Add real search/indexing logic 

---