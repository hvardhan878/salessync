import sqlite3
from contextlib import contextmanager
import os

DB_PATH = os.getenv("SQLITE_DB_PATH", os.path.join(os.path.dirname(__file__), "sales_sync.db"))

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        # Users table
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
        """)
        # Accounts table
        c.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            industry TEXT NOT NULL
        )
        """)
        # Opportunities table
        c.execute("""
        CREATE TABLE IF NOT EXISTS opportunities (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            stage TEXT NOT NULL,
            amount REAL NOT NULL
        )
        """)
        # Insert demo user if not exists
        c.execute("INSERT OR IGNORE INTO users (username, password, full_name) VALUES (?, ?, ?)",
                  ("demo", "password", "Demo User"))
        conn.commit()

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# --- User CRUD ---
def get_user(username):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        return c.fetchone()

def create_user(username, password, full_name):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, full_name) VALUES (?, ?, ?)",
                  (username, password, full_name))
        conn.commit()

# --- Accounts CRUD ---
def get_accounts():
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM accounts")
        return c.fetchall()

def create_account(id, name, industry):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO accounts (id, name, industry) VALUES (?, ?, ?)", (id, name, industry))
        conn.commit()

def delete_account(account_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
        conn.commit()
        return c.rowcount

# --- Opportunities CRUD ---
def get_opportunities():
    with get_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM opportunities")
        return c.fetchall()

def create_opportunity(id, name, stage, amount):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO opportunities (id, name, stage, amount) VALUES (?, ?, ?, ?)",
                  (id, name, stage, amount))
        conn.commit()

def delete_opportunity(opportunity_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM opportunities WHERE id = ?", (opportunity_id,))
        conn.commit()
        return c.rowcount