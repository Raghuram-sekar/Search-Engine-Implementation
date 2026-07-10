# Custom Web Search Engine
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Overview
A complete search engine architecture including a multi-threaded web crawler, database indexer, PageRank ranking algorithm, and a web search interface.

## System Architecture
```\n[Relational Database / Core API Architecture]\n```

## Features
- Multi-threaded web crawler gathering HTML pages.
- Database indexer creating inverted indexes of crawled text.
- PageRank scoring algorithm for relevance ranking.
- Web search interface for user queries.

## Tech Stack
- HTML/CSS/JavaScript search interface UI
- Python search logic and PageRank algorithms
- File-based database indexing

## Getting Started
To configure and run the project locally, clone the repository and execute the setup instructions:

```bash
git clone https://github.com/Raghuram-sekar/Search-Engine-Implementation.git
cd Search-Engine-Implementation

# Execute local setup commands:
cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
python crawler.py
```
