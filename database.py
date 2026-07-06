import sqlite3
import random
import os

DB_NAME = "questions.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS questions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson TEXT NOT NULL,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            answer INTEGER NOT NULL
        )
        """)

        self.conn.commit()

    def add_question(
        self,
        lesson,
        question,
        option1,
        option2,
        option3,
        option4,
        answer
    ):

        self.cur.execute("""
        INSERT INTO questions
        (
        lesson,
        question,
        option1,
        option2,
        option3,
        option4,
        answer
        )
        VALUES
        (?,?,?,?,?,?,?)
        """,
        (
            lesson,
            question,
            option1,
            option2,
            option3,
            option4,
            answer
        ))

        self.conn.commit()

    def close(self):
        self.conn.close()
    
