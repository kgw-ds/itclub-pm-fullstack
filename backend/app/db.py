import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "app.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def list_posts() -> list[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_post(post_id: int) -> sqlite3.Row | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    row = cur.fetchone()
    conn.close()
    return row


def create_post(title: str, content: str, created_at: str) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)",
        (title, content, created_at),
    )
    conn.commit()
    post_id = cur.lastrowid
    conn.close()
    return int(post_id)


def delete_post(post_id: int) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()
def get_prev_post_id(current_id: int) -> int | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM posts WHERE id < ? ORDER BY id DESC LIMIT 1",
        (current_id,),
    )
    row = cur.fetchone()
    conn.close()
    return int(row["id"]) if row else None


def get_next_post_id(current_id: int) -> int | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM posts WHERE id > ? ORDER BY id ASC LIMIT 1",
        (current_id,),
    )
    row = cur.fetchone()
    conn.close()
    return int(row["id"]) if row else None
def search_posts_by_title(keyword: str) -> list[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()

    pattern = f"%{keyword}%"
    cur.execute(
        """
        SELECT * FROM posts
        WHERE title LIKE ? OR content LIKE ?
        ORDER BY id DESC
        """,
        (pattern, pattern),
    )

    rows = cur.fetchall()
    conn.close()
    return rows

