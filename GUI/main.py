from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ObjectProperty, BooleanProperty,StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton ,MDRaisedButton,MDFillRoundFlatIconButton,MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.uix.image import Image
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivy.animation import Animation
from kivymd.uix.fitimage import FitImage
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivymd.uix.navigationdrawer import MDNavigationDrawerLabel

import cv2
from kivy.graphics.texture import Texture
import cvzone



from password import allow_login,update
from attendance import face_rec
import random

from CONSTANTS import DEFAULT_PATH_IMAGE

RECOGNIZER  = cv2.face.LBPHFaceRecognizer_create()
RECOGNIZER.read(r'data\Model\trained_model2.yml')


global ID
ID = None

global EMP_LST
EMP_LST = []





# Attandance Card Class
class CardItem(MDCard):
    def __init__(self,ID, *args, **kwargs):
        super().__init__(*args, **kwargs)
        info = face_rec(ID)
        self.name = info[0]
        self.des = info[1]
        self.image_path = info[2]
        self.time = info[3]
        self.status = info[4]
        self.elevation = 3

        self.leave = False

        if self.status == "True":
            self.present = True
            self.absent = False
        else:
            self.present = False
            self.absent = True

        
        self.size_hint_y = None
        self.height = dp(100)
        self.padding = dp(4)
        self.radius = 12

        image = FitImage(
            source=self.image_path,
            radius=self.radius,
            size_hint_x=None,
            width=self.height,
        )

        labels_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="6dp",
            padding=("12dp", 0, 0, 0),
            pos_hint={"center_y": 0.5},
        )

        name_label = MDLabel(
            id = "emp_name",
            text=self.name,
            font_style="H5",
            bold=True,
            adaptive_height=True,
        )

        designation_label = MDLabel(
            id = "emp_des",
            text=self.des,
            theme_text_color="Hint",
            adaptive_height=True,
        )

        time_label = MDLabel(
            id = "time_entry",
            text = self.time,
            theme_text_color="Hint",
            adaptive_height=True
        )
        
        cheak_box = MDBoxLayout(
            id ="cheak_box",
            adaptive_size=True,
            spacing="8dp",
        )

        cheak_present = MDCheckbox(
            group = f"group_{ID}",
            size_hint= (None, None),
            size= ("48dp", "48dp"),
            pos_hint= {'center_x': .5, 'center_y': .5},
            active = self.present
        )
        cheak_absent = MDCheckbox(
            group = f"group_{ID}",
            size_hint= (None, None),
            size= ("48dp", "48dp"),
            pos_hint= {'center_x': .5, 'center_y': .5},
            active = self.absent
        )
        cheak_leave = MDCheckbox(
            group = f"group_{ID}",
            size_hint= (None, None),
            size= ("48dp", "48dp"),
            pos_hint= {'center_x': .5, 'center_y': .5},
            active = self.leave
        )

        present_label = MDLabel(
            text = "P",
            theme_text_color="Hint",
            adaptive_height=True,
            halign= 'center',
            pos_hint= {'center_x': .5, 'center_y': .5}
        )
        Aabsent_label = MDLabel(
            text = "A",
            theme_text_color="Hint",
            adaptive_height=True,
            halign= 'center',
            pos_hint= {'center_x': .5, 'center_y': .5}
        )
        Leave_label = MDLabel(
            text = "L",
            theme_text_color="Hint",
            adaptive_height=True,
            halign= 'center',
            pos_hint= {'center_x': .5, 'center_y': .5}
        )
        p_Box = MDBoxLayout(
            # orientation = "vertical",
            adaptive_size=True,
            spacing="8dp"
            
        )
        a_Box = MDBoxLayout(
            # orientation = "vertical",
            adaptive_size=True,
            spacing="8dp"
        )
        l_Box = MDBoxLayout(
            # orientation = "vertical",
            adaptive_size=True,
            spacing="8dp"
        )

        p_Box.add_widget(present_label)
        p_Box.add_widget(cheak_present)

        p_Box.add_widget(Aabsent_label)
        p_Box.add_widget(cheak_absent)

        p_Box.add_widget(Leave_label)
        p_Box.add_widget(cheak_leave)

        cheak_box.add_widget(p_Box)
        cheak_box.add_widget(a_Box)
        cheak_box.add_widget(l_Box)






        labels_layout.add_widget(name_label)
        labels_layout.add_widget(designation_label)
        labels_layout.add_widget(time_label)


        self.add_widget(image)
        self.add_widget(labels_layout)
        self.add_widget(cheak_box)

    def cheaked(self, text):
        print(text)
    
# Login Screen Class    
class LoginScreen(Screen):


    error_username = BooleanProperty(False)
    error_password = BooleanProperty(False)
    def auth(self):
        user = self.ids["username"]
        pass_ = self.ids["password"]
    
        
        if user.text != "" and pass_.text != "":
            print("Inside Allow")
            bool_ = allow_login(user.text,pass_.text)
            user.text = ""
            pass_.text = ""
            if not bool_:
                self.error_username = True
                self.error_password = True

            return bool_

        else:
            # print("Inside else")
            if user.text == "":
                self.error_username = True
                
                
            
            if pass_.text == "":
                self.error_password = True

            user.text = ""
            pass_.text = "" 
            return False
    
# Reset password Screen class
class ResetScreen(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"
        self.padding = "12dp"
        self.size_hint_y = None
        self.height = "150dp"

        self.user_textfeild = MDTextField(
            
            hint_text= "New Username",
            helper_text= "Invalid Input",
            helper_text_mode = "on_error",
            pos_hint = {"center_x": .5, "center_y": .5},
            size_hint_x = .5,
            error = False
        )

        self.pass_textfeild = MDTextField(
            hint_text= "New Password",
            helper_text= "Invalid Input",
            helper_text_mode = "on_error",
            pos_hint = {"center_x": .5, "center_y": .5},
            size_hint_x = .5,
            error = False
        )

        self.button = MDRaisedButton(
            text= "OK",
            pos_hint= {"center_x": .5, "center_y": .5},
            disabled = False,
            on_press= self.update_pass
        )

        self.add_widget(self.user_textfeild)
        self.add_widget(self.pass_textfeild)
        self.add_widget(self.button)


    def update_pass(self,obj):



        if self.user_textfeild.text != "" and  self.pass_textfeild.text != "":
            print(self.user_textfeild.text,self.pass_textfeild.text)
            # update(user.text,password.text)
            self.user_textfeild = ""
            self.pass_textfeild = ""
            self.button.disabled = True        

        else:
            self.user_textfeild.error = True
            self.pass_textfeild.error = True

# Main Screen Class
class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.capture = cv2.VideoCapture(0)
        self.employess_list = []

        self.cascade = cv2.CascadeClassifier("D:\Bank FaceRecognization\haarcascade_frontalface_alt.xml")

    def start_vedio(self):
        self.event = Clock.schedule_interval(self.update, 1.0 / 30.0)

    def stop_vedio(self):
        if hasattr(self,"event"):
            Clock.unschedule(self.event)

    def update(self, obj):
        image = self.ids.Video

        ret, frame = self.capture.read()
        grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = self.cascade.detectMultiScale(grey)
        
        for (x,y,w,h) in faces:
            bbx = x,y,w,h
            cvzone.cornerRect(frame,bbx, rt=1)
            Id, conf = RECOGNIZER.predict(grey[y:y+h,x:x+w])
            if 100 > int(conf) > 70:
                # info = face_rec(Id)
                # name = info[0]
                # des = info[1]
                # image = info[2]
                # status = info[3]
                if Id not in self.employess_list:
                    self.employess_list.append(Id)
                    global EMP_LST
                    global ID
                    ID = Id
                    EMP_LST.append(Id)
                    # View().add_item(self)
                cvzone.putTextRect(frame,f"{Id}_{int(conf)}",(x,y))

            
            

        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        image.texture = texture
    
    def on_enter(self):
        self.start_vedio()
    def on_leave(self, *args):
        self.stop_vedio()


# View Screen Class    
class View(Screen):

    def on_enter(self):
        global EMP_LST

        for x in EMP_LST:
            self.ids.container.add_widget(CardItem(ID=x))
    
    def on_leave(self, *args):
        global EMP_LST
        EMP_LST.clear()
    
    def add_item(self,obj):
        global ID
        for x in range(10):
            self.ids.container.add_widget(CardItem())
        



# Reset password Class On Login Screen 
class Content(MDBoxLayout):
    vari_code = StringProperty("")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"
        self.spacing = "12dp"
        self.size_hint_y = None
        self.height = "100dp"

        self.text_feild_ = self.text_feild()
        self.add_widget(self.text_feild_)

        self.button = MDFlatButton(text = "OK", pos_hint= {"center_x": .5},on_press = self.varify,disabled = False)

        self.add_widget(self.button)
        

    
    def text_feild(self):
        text_feild = MDTextField(id = "var" , hint_text="CODE",helper_text =  "Invalid varification Code",helper_text_mode= "on_error",error=False)
        return text_feild
    
    def varify(self,obj):
        varification_code = 1234 # Dummy Varification Code Have to Change it,
        if self.text_feild_.text != "":
            if int(self.text_feild_.text) == varification_code :
                self.dialog_box_pass()
                self.button.disabled = True
       
                self.text_feild_.text = ""
            else: 
                self.text_feild_.error = True
                self.text_feild_.text = ""
        else:
            self.text_feild_.error = True
            self.text_feild_.text = "" 



    def dialog_box_pass(self):
        self.dialog = MDDialog(#text = "A verification Code has Been sent to Your Email Please Enter it to Reset Your Password.",
                                content_cls=ResetScreen(), 
                                size_hint=(0.8, 1),
                                

                                type="custom",
                               buttons=[MDFlatButton(text='Close', on_release=self.dialog_close_pass)
                                        ]
                               )
        self.dialog.open()

    def dialog_close_pass(self,obj):
        self.dialog.dismiss()
    

class ResetTime(MDBoxLayout):
    pass




sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(View(name = "view"))


class MainApp(MDApp):
    
    def build(self):

        # Create the screen manager
        app = Builder.load_file(r"D:\Bank FaceRecognization\GUI\main.kv")


        return app
    
    def dialog_box(self):
        self.dialog = MDDialog(title = "Enter Code",
                                content_cls=ResetScreen(), 
                                size_hint=(0.4, 1),
                                type="custom",
                               buttons=[MDRaisedButton(text='Close', on_release=self.dialog_close)
                                        ]
                               )
        self.dialog.open()

    def dialog_close(self,obj):
        self.dialog.dismiss()

    def dialog_box_reset_admin(self):
        self.dialog_admin = MDDialog(title = "Change Password",
                                content_cls=ResetScreen(), 
                                size_hint=(0.4, 1),
                                type="custom",
                               buttons=[MDRaisedButton(text='Close', on_release=self.dialog_box_reset_admin_close)
                                        ]
                               )
        self.dialog_admin.open()
    
    def dialog_box_reset_admin_close(self,obj):
        self.dialog_admin.dismiss()
    
    def change_time(self):
        self.dialog_time_reset = MDDialog(title = "Change Time",
                                content_cls=ResetTime(), 
                                size_hint=(0.4, 1),
                                type="custom",
                               buttons=[MDRaisedButton(text='Close', on_release=self.dialog_close)
                                        ]
                               )
        self.dialog_time_reset.open()
    
    def close_change_time(self,obj):
        self.dialog_time_reset.dismiss()


    def export_data(self):
        pass

    
    


    


          

if __name__ == '__main__':
    MainApp().run()