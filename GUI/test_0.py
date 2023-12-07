from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.dialogBox()
'''










class Example(MDApp):
 

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def dialogBox(self):
        self.dialog = MDDialog()
        self.dialog.text = "Dialog Box"
        self.dialog.buttons = [
            MDFlatButton(
                text = "DISCARD",
                on_press = self.close_dialog()

            )
        ]
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()



Example().run()