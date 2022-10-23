from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.lang.builder import Builder
import cv2
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from pyzbar.pyzbar import decode

import time
from kivymd.uix.toolbar import MDTopAppBar

Window.size = (300,500)

class Qrcodedetector(MDApp):

    def build(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.primary_palette='DeepPurple'
        layout=MDBoxLayout(orientation='vertical')
        TopBar = MDTopAppBar(title = "QRScanner", left_action_items = [["arrow-left-circle-outline"]])
        layout.add_widget(TopBar)
        self.image=Image()
        layout.add_widget(self.image)
        #self.save_img_button=(MDFillRoundFlatButton(text="Detect URL",pos_hint={'center_x':0.5,'center_y':0.3},size_hint=(None,None)))
        #self.save_img_button.bind(on_press=self.take_picture)
        #layout.add_widget(self.save_img_button)
        self.capture=cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        Clock.schedule_interval(self.load_video,1.0/30.0)
        return layout
    def load_video(self,*args):
        ret,frame=self.capture.read()
        for code in decode(frame):
            print(code.data.decode('utf-8'))
            time.sleep(5)
        self.image_frame=frame
        buffer=cv2.flip(frame,0).tobytes()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    #def take_picture(self, *args):
       #self.b = self.load_video
        
if __name__ == '__main__':
    Qrcodedetector().run()