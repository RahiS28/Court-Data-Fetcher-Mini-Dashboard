import sqlite3

DB_PATH = "court_data.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            raw_html TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()

def log_query(case_type, case_number, filing_year, raw_html):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO queries (case_type, case_number, filing_year, raw_html) VALUES (?, ?, ?, ?)",
                  (case_type, case_number, filing_year, raw_html))
        conn.commit()
