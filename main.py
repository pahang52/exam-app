from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase

# فونت فارسی
LabelBase.register(name="fa", fn_regular="assets/Vazirmatn.ttf")


class ExamApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.questions = []

        # عنوان
        self.add_widget(Label(
            text="برنامه طراحی سوالات نیکزادفرد",
            font_name="fa",
            size_hint=(1, 0.1)
        ))

        # اطلاعات عمومی
        self.school = TextInput(hint_text="اداره آموزش و پرورش / مدرسه", size_hint=(1, 0.08))
        self.student = TextInput(hint_text="نام و نام خانوادگی دانش آموز", size_hint=(1, 0.08))
        self.father = TextInput(hint_text="نام پدر", size_hint=(1, 0.08))
        self.grade = TextInput(hint_text="پایه", size_hint=(1, 0.08))
        self.lesson = TextInput(hint_text="نام درس", size_hint=(1, 0.08))
        self.date = TextInput(hint_text="تاریخ امتحان", size_hint=(1, 0.08))
        self.teacher = TextInput(hint_text="نام دبیر", size_hint=(1, 0.08))
        self.term = TextInput(hint_text="نوبت امتحانی", size_hint=(1, 0.08))

        # سوال
        self.qtype = TextInput(hint_text="نوع سوال (تستی، صحیح غلط، تشریحی...)", size_hint=(1, 0.08))
        self.question = TextInput(hint_text="متن سوال", size_hint=(1, 0.12))
        self.score = TextInput(hint_text="بارم (0.25 تا 10)", size_hint=(1, 0.08))

        for w in [
            self.school, self.student, self.father, self.grade,
            self.lesson, self.date, self.teacher, self.term,
            self.qtype, self.question, self.score
        ]:
            self.add_widget(w)

        # دکمه افزودن
        self.btn = Button(text="افزودن سوال", size_hint=(1, 0.1))
        self.btn.bind(on_press=self.add_question)
        self.add_widget(self.btn)

        # خروجی
        self.output = Label(text="سوالات ثبت شده:", font_name="fa")
        self.add_widget(self.output)

    def add_question(self, instance):
        q = self.question.text
        t = self.qtype.text
        s = self.score.text

        if q and s:
            self.questions.append(f"{t} | {q} | بارم: {s}")
            self.output.text = "\n".join(self.questions)

            self.question.text = ""
            self.score.text = ""
            self.qtype.text = ""


class MainApp(App):
    def build(self):
        return ExamApp()


if __name__ == "__main__":
    MainApp().run()
