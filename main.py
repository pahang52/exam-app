from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ExamApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.school = TextInput(hint_text="نام دبیرستان")
        self.student = TextInput(hint_text="نام دانش آموز")

        btn = Button(text="ساخت سوال")
        btn.bind(on_press=self.create_exam)

        self.result = Label(text="")

        layout.add_widget(self.school)
        layout.add_widget(self.student)
        layout.add_widget(btn)
        layout.add_widget(self.result)

        return layout

    def create_exam(self, instance):
        self.result.text = f"سوالات ساخته شد برای {self.student.text}"


ExamApp().run()
