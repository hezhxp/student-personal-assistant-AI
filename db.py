import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).with_name("assistant.db")

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL,
            is_done INTEGER NOT NULL DEFAULT 0
        )
        """)
        conn.commit()

def add_goal(text: str) -> int:
    text = text.strip()
    if not text:
        raise ValueError("Goal text is empty")

    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO goals (text, created_at, is_done) VALUES (?, ?, 0)",
            (text, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()
        return cur.lastrowid

def list_goals(include_done: bool = True):
    with get_conn() as conn:
        if include_done:
            rows = conn.execute(
                "SELECT id, text, created_at, is_done FROM goals ORDER BY id DESC"
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT id, text, created_at, is_done FROM goals WHERE is_done=0 ORDER BY id DESC"
            ).fetchall()
    return rows

def mark_goal_done(goal_id: int):
    with get_conn() as conn:
        conn.execute("UPDATE goals SET is_done=1 WHERE id=?", (goal_id,))
        conn.commit()

def clear_goals():
    with get_conn() as conn:
        conn.execute("DELETE FROM goals")
        conn.commit()
