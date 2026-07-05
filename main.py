from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class ExamApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.questions = []

        # عنوان
        self.title = Label(
            text="برنامه طراحی سوالات - نیکزادفرد",
            size_hint=(1, 0.1)
        )
        self.add_widget(self.title)

        # اطلاعات پایه (اختیاری)
        self.school = TextInput(hint_text="نام مدرسه", size_hint=(1, 0.08))
        self.student = TextInput(hint_text="نام دانش آموز", size_hint=(1, 0.08))
        self.lesson = TextInput(hint_text="نام درس", size_hint=(1, 0.08))

        self.add_widget(self.school)
        self.add_widget(self.student)
        self.add_widget(self.lesson)

        # نوع سوال
        self.qtype = TextInput(hint_text="نوع سوال (تستی، تشریحی...)", size_hint=(1, 0.08))
        self.add_widget(self.qtype)

        # متن سوال
        self.question = TextInput(hint_text="متن سوال", size_hint=(1, 0.1))
        self.add_widget(self.question)

        # بارم
        self.score = TextInput(hint_text="بارم (0.25 تا 10)", size_hint=(1, 0.08))
        self.add_widget(self.score)

        # دکمه افزودن
        self.btn_add = Button(text="افزودن سوال", size_hint=(1, 0.1))
        self.btn_add.bind(on_press=self.add_question)
        self.add_widget(self.btn_add)

        # نمایش سوالات
        self.output = Label(text="لیست سوالات:", size_hint=(1, 0.4))
        self.add_widget(self.output)

    def add_question(self, instance):
        qtype = self.qtype.text
        qtext = self.question.text
        score = self.score.text

        if qtext and score:
            self.questions.append(f"{qtype} | {qtext} | بارم: {score}")

            self.output.text = "لیست سوالات:\n\n" + "\n".join(self.questions)

            # پاک کردن فیلدها
            self.qtype.text = ""
            self.question.text = ""
            self.score.text = ""


class MainApp(App):
    def build(self):
        return ExamApp()


if __name__ == "__main__":
    MainApp().run()
