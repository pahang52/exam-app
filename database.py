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
       def get_all_questions(self):
        """
        دریافت همه سوالات
        """
        self.cur.execute("""
            SELECT *
            FROM questions
            ORDER BY id DESC
        """)
        return self.cur.fetchall()


    def get_questions_by_lesson(self, lesson):
        """
        دریافت سوالات یک درس
        """
        self.cur.execute("""
            SELECT *
            FROM questions
            WHERE lesson=?
            ORDER BY RANDOM()
        """, (lesson,))
        return self.cur.fetchall()


    def get_question(self, qid):
        """
        دریافت یک سوال با شناسه
        """
        self.cur.execute("""
            SELECT *
            FROM questions
            WHERE id=?
        """, (qid,))
        return self.cur.fetchone()


    def search(self, text):
        """
        جستجوی سوال
        """
        self.cur.execute("""
            SELECT *
            FROM questions
            WHERE question LIKE ?
            ORDER BY id DESC
        """, (f"%{text}%",))
        return self.cur.fetchall()


    def count(self):
        """
        تعداد کل سوالات
        """
        self.cur.execute("""
            SELECT COUNT(*)
            FROM questions
        """)
        return self.cur.fetchone()[0] 
