import sqlite3

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

    def get_all_questions(self):

        self.cur.execute("""
        SELECT *
        FROM questions
        ORDER BY id DESC
        """)

        return self.cur.fetchall()

    def get_questions_by_lesson(self, lesson):

        self.cur.execute("""
        SELECT *
        FROM questions
        WHERE lesson=?
        ORDER BY RANDOM()
        """, (lesson,))

        return self.cur.fetchall()

    def get_question(self, qid):

        self.cur.execute("""
        SELECT *
        FROM questions
        WHERE id=?
        """, (qid,))

        return self.cur.fetchone()

    def search(self, text):

        self.cur.execute("""
        SELECT *
        FROM questions
        WHERE question LIKE ?
        ORDER BY id DESC
        """, (f"%{text}%",))

        return self.cur.fetchall()

    def count(self):

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

        self.cur.execute("""
        DELETE FROM questions
        WHERE id=?
        """, (qid,))

        self.conn.commit()

    def random_questions(self, lesson, count):

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

        self.cur.execute("""
        SELECT DISTINCT lesson
        FROM questions
        ORDER BY lesson
        """)

        return [row[0] for row in self.cur.fetchall()]

    def clear_database(self):

        self.cur.execute("""
        DELETE FROM questions
        """)

        self.conn.commit()

    def import_questions(self, data):

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

    def close(self):

        self.conn.close()

    def __del__(self):

        try:
            self.conn.close()
        except Exception:
            pass
