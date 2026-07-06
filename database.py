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
       def update_question(
        self,
        qid,
        lesson,
        question,
        option1,
        option2,
        option3,
        option4,
        answer
    ):
        """
        ویرایش سوال
        """

        self.cur.execute("""
        UPDATE questions
        SET
            lesson=?,
            question=?,
            option1=?,
            option2=?,
            option3=?,
            option4=?,
            answer=?
        WHERE id=?
        """,
        (
            lesson,
            question,
            option1,
            option2,
            option3,
            option4,
            answer,
            qid
        ))

        self.conn.commit()


    def delete_question(self, qid):
        """
        حذف سوال
        """

        self.cur.execute("""
        DELETE FROM questions
        WHERE id=?
        """, (qid,))

        self.conn.commit()


    def random_questions(self, lesson, count):
        """
        انتخاب تصادفی سوال
        """

        self.cur.execute("""
        SELECT *
        FROM questions
        WHERE lesson=?
        ORDER BY RANDOM()
        LIMIT ?
        """,
        (
            lesson,
            count
        ))

        return self.cur.fetchall()


    def random_by_type(self, lesson, count):
        """
        تابع کمکی برای آزمون ساز
        """

        return self.random_questions(
            lesson,
            count
        )


    def exists(self, qid):

        self.cur.execute("""
        SELECT COUNT(*)
        FROM questions
        WHERE id=?
        """, (qid,))

        return self.cur.fetchone()[0] > 0
         def get_lessons(self):
        """
        دریافت لیست درس‌ها
        """

        self.cur.execute("""
        SELECT DISTINCT lesson
        FROM questions
        ORDER BY lesson
        """)

        return [row[0] for row in self.cur.fetchall()]


    def clear_database(self):
        """
        حذف تمام سوالات
        """

        self.cur.execute("""
        DELETE FROM questions
        """)

        self.conn.commit()


    def import_questions(self, data):
        """
        ورود گروهی سوالات
        data = [
            (
                lesson,
                question,
                option1,
                option2,
                option3,
                option4,
                answer
            )
        ]
        """

        self.cur.executemany("""
        INSERT INTO questions(
            lesson,
            question,
            option1,
            option2,
            option3,
            option4,
            answer
        )
        VALUES(?,?,?,?,?,?,?)
        """, data)

        self.conn.commit()


    def export_questions(self):

        self.cur.execute("""
        SELECT *
        FROM questions
        ORDER BY lesson,id
        """)

        return self.cur.fetchall()


    def __del__(self):

        try:
            self.conn.close()
        except:
            pass
