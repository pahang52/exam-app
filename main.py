from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from database import Database
from utils.persian import fa

db = Database()


class HomeScreen(Screen):
    pass


class AddQuestionScreen(Screen):

    status = StringProperty("")

    def save_question(self):

        lesson = self.ids.lesson.text.strip()
        question = self.ids.question.text.strip()

        option1 = self.ids.option1.text.strip()
        option2 = self.ids.option2.text.strip()
        option3 = self.ids.option3.text.strip()
        option4 = self.ids.option4.text.strip()

        answer = self.ids.answer.text.strip()

        if lesson == "":
            self.status = fa("نام درس را وارد کنید.")
            return

        if question == "":
            self.status = fa("متن سؤال را وارد کنید.")
            return

        if option1 == "" or option2 == "" or option3 == "" or option4 == "":
            self.status = fa("همه گزینه‌ها را وارد کنید.")
            return

        if answer not in ("1", "2", "3", "4"):
            self.status = fa("پاسخ صحیح باید عدد 1 تا 4 باشد.")
            return

        db.add_question(
            lesson,
            question,
            option1,
            option2,
            option3,
            option4,
            int(answer)
        )

        self.ids.lesson.text = ""
        self.ids.question.text = ""
        self.ids.option1.text = ""
        self.ids.option2.text = ""
        self.ids.option3.text = ""
        self.ids.option4.text = ""
        self.ids.answer.text = ""

        self.status = fa("سؤال با موفقیت ذخیره شد.")


class QuestionListScreen(Screen):

    status = StringProperty("")
    questions = []

    def on_pre_enter(self):
        self.load_questions()

    def load_questions(self):

        self.questions = db.get_all_questions()

        txt = ""

        if not self.questions:
            txt = fa("بانک سؤال خالی است.")
        else:
            for q in self.questions:
                txt += (
                    f"ID: {q[0]}\n"
                    f"{fa('درس')}: {fa(q[1])}\n"
                    f"{fa(q[2])}\n"
                    "----------------------\n"
                )

        self.ids.questions_label.text = txt

    def delete_question(self):

        qid = self.ids.delete_id.text.strip()

        if qid == "":
            self.status = fa("شناسه را وارد کنید.")
            return

        if not qid.isdigit():
            self.status = fa("شناسه نامعتبر است.")
            return

        if not db.exists(int(qid)):
            self.status = fa("این شناسه وجود ندارد.")
            return

        db.delete_question(int(qid))

        self.ids.delete_id.text = ""
        self.status = fa("سؤال حذف شد.")

        self.load_questions()


class ScreenManagement(ScreenManager):
    pass


class ExamApp(App):

    def build(self):

        Builder.load_file("ui.kv")

        sm = ScreenManagement()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(AddQuestionScreen(name="add"))
        sm.add_widget(QuestionListScreen(name="list"))

        return sm


if __name__ == "__main__":
    ExamApp().run()
