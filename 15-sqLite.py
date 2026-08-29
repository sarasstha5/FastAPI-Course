import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("mydatabase.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

@app.post("/user/")
async def create_user(name: str, email: str):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    return {"message": "User created successfully"}