from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from android.permissions import request_permissions, Permission
from fpdf import FPDF
import os


# ---------------- PDF CLASS ----------------
class PDFGenerator:
    def get_path(self, filename):
        base = "/storage/emulated/0/Documents"
        if not os.path.exists(base):
            base = "/storage/emulated/0/Download"
        return os.path.join(base, filename)

    def create_pdf(self, text, filename="exam.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for line in text.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)

        path = self.get_path(filename)
        pdf.output(path)
        return path


# ---------------- SCREEN 1 ----------------
class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=8, padding=10)

        self.school = TextInput(hint_text="اداره آموزش و پرورش")
        self.school_name = TextInput(hint_text="نام دبیرستان")
        self.student = TextInput(hint_text="نام دانش آموز")
        self.father = TextInput(hint_text="نام پدر")
        self.grade = TextInput(hint_text="پایه")
        self.lesson = TextInput(hint_text="درس")
        self.date = TextInput(hint_text="تاریخ امتحان")
        self.teacher = TextInput(hint_text="نام دبیر")

        btn = Button(text="مرحله بعد")
        btn.bind(on_press=self.next)

        layout.add_widget(self.school)
        layout.add_widget(self.school_name)
        layout.add_widget(self.student)
        layout.add_widget(self.father)
        layout.add_widget(self.grade)
        layout.add_widget(self.lesson)
        layout.add_widget(self.date)
        layout.add_widget(self.teacher)
        layout.add_widget(btn)

        self.add_widget(layout)

    def next(self, instance):
        app = App.get_running_app()
        app.data = {
            "school": self.school.text,
            "school_name": self.school_name.text,
            "student": self.student.text,
            "father": self.father.text,
            "grade": self.grade.text,
            "lesson": self.lesson.text,
            "date": self.date.text,
            "teacher": self.teacher.text,
        }
        self.manager.current = "exam"


# ---------------- SCREEN 2 ----------------
class ExamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=8, padding=10)

        self.qtype = Spinner(
            text="نوع سوال",
            values=("صحیح/غلط", "تستی", "جای خالی", "تشریحی", "کوتاه پاسخ")
        )

        self.count = TextInput(hint_text="تعداد سوال")
        self.score = Spinner(text="بارم", values=("0.25","0.5","1","2","5","10"))

        self.result = TextInput(multiline=True)

        btn_make = Button(text="تولید آزمون")
        btn_make.bind(on_press=self.generate)

        btn_pdf = Button(text="ذخیره PDF در گوشی")
        btn_pdf.bind(on_press=self.save_pdf)

        layout.add_widget(self.qtype)
        layout.add_widget(self.count)
        layout.add_widget(self.score)
        layout.add_widget(btn_make)
        layout.add_widget(btn_pdf)
        layout.add_widget(self.result)

        self.add_widget(layout)

    def generate(self, instance):
        app = App.get_running_app()
        d = app.data

        self.text = f"""
آموزش و پرورش: {d['school']}
مدرسه: {d['school_name']}
دانش آموز: {d['student']}
درس: {d['lesson']}
تاریخ: {d['date']}
دبیر: {d['teacher']}

------------------
نوع سوال: {self.qtype.text}
تعداد: {self.count.text}
بارم: {self.score.text}

1) سوال نمونه
2) سوال نمونه
3) سوال نمونه
"""

        self.result.text = self.text

    def save_pdf(self, instance):

        request_permissions([
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ])

        if not hasattr(self, "text"):
            self.result.text = "اول آزمون را تولید کنید"
            return

        pdf = PDFGenerator()
        path = pdf.create_pdf(self.text)

        self.result.text = "PDF ذخیره شد:\n" + path


# ---------------- APP ----------------
class ExamApp(App):
    def build(self):
        self.data = {}
        sm = ScreenManager()
        sm.add_widget(InfoScreen(name="info"))
        sm.add_widget(ExamScreen(name="exam"))
        return sm


ExamApp().run()
