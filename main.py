from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window


Window.clearcolor = (0.95, 0.95, 0.95, 1)


# ---------------- SCREEN 1: INFO ----------------
class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.school = TextInput(hint_text="اداره / آموزش و پرورش")
        self.school_name = TextInput(hint_text="نام دبیرستان")
        self.student = TextInput(hint_text="نام دانش آموز")
        self.father = TextInput(hint_text="نام پدر")
        self.grade = TextInput(hint_text="پایه")
        self.lesson = TextInput(hint_text="درس")
        self.date = TextInput(hint_text="تاریخ امتحان")
        self.teacher = TextInput(hint_text="نام دبیر")

        btn = Button(text="مرحله بعد", size_hint=(1, 0.2))
        btn.bind(on_press=self.go_next)

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

    def go_next(self, instance):
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


# ---------------- SCREEN 2: EXAM DESIGN ----------------
class ExamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.qtype = Spinner(
            text="نوع سوال",
            values=("صحیح/غلط", "تستی", "جای خالی", "تشریحی", "کوتاه پاسخ")
        )

        self.count = TextInput(hint_text="تعداد سوال")

        self.score = Spinner(
            text="بارم",
            values=("0.25", "0.5", "1", "2", "5", "10")
        )

        btn = Button(text="تولید آزمون")
        btn.bind(on_press=self.generate)

        self.result = TextInput(multiline=True)

        layout.add_widget(self.qtype)
        layout.add_widget(self.count)
        layout.add_widget(self.score)
        layout.add_widget(btn)
        layout.add_widget(self.result)

        self.add_widget(layout)

    def generate(self, instance):
        app = App.get_running_app()
        data = app.data

        text = f"""
آموزش و پرورش: {data['school']}
مدرسه: {data['school_name']}
دانش آموز: {data['student']}
پایه: {data['grade']}
درس: {data['lesson']}
تاریخ: {data['date']}
دبیر: {data['teacher']}

----------------------

نوع سوال: {self.qtype.text}
تعداد سوال: {self.count.text}
بارم: {self.score.text}

----------------------
1) سوال نمونه تولید شد
2) سوال نمونه تولید شد
3) سوال نمونه تولید شد

(نسخه حرفه‌ای در حال توسعه...)
"""
        self.result.text = text


# ---------------- APP ----------------
class ExamApp(App):
    def build(self):
        self.data = {}

        sm = ScreenManager()
        sm.add_widget(InfoScreen(name="info"))
        sm.add_widget(ExamScreen(name="exam"))

        return sm


ExamApp().run()
