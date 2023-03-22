from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import socket  
import time
class HomeScreen(Screen):
    def on_kv_post(self,_):
        self.set_ip()
    def set_ip(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.s.connect(('10.255.255.255', 1))  # Try to connect to a public IP address
            self.local_ip_address = self.s.getsockname()[0]
        except:
            self.local_ip_address = socket.gethostbyname(socket.gethostname())

        self.port = 8888
        def_ip="192.168.0.1"
        if not self.local_ip_address.startswith("192.168"): 
            self.local_ip_address=def_ip
            self.ids.IP.text=f"IP Address:{self.local_ip_address}"
        else:
            self.ids.IP.text=f"IP Address:{self.local_ip_address}"
        self.ids.port.text=f"Port Address: {self.port}"

class FileChooserScreen(Screen):
    def selected(self,filepath):
        self.filepath=filepath
class RecieveScreen(Screen):
    def on_pre_enter(self, *args):
        sm=self.manager
        home_screen=sm.get_screen("home_screen")
        self.s=socket.socket()
        address=(home_screen.local_ip_address,home_screen.port)
        self.ids.status.text="Binding"
        self.s.bind(address)
        self.s.listen()
        self.ids.status.text="Wating For Conection"
        self.ids.address.text=f"{address}"
        conn,add=self.s.accept()
        print("Connected")
    def cancel(self):
        self.s.close()
class GetIPScreen(Screen):
    def on_pre_enter(self, *args):
        sm=self.manager
        
        self.home_screen=sm.get_screen("home_screen") 
        self.ids.address.text=f"{self.home_screen.local_ip_address,self.home_screen.port}"
    def connect(self):
        self.s=socket.socket()
        
        self.s.connect((self.ids.remote_ip,self.home_screen.port))
        self.ids.image.source="connected.png"
        self.ids.connect.text="connected"
        self.ids.connect.desabled=True
        self.ids.select_file=False
        


class SendScreen(Screen):
    def on_pre_enter(self, *args):
        sm=self.manager
        home_screen=sm.get_screen("home_screen")   
        file_chooser_screen=sm.get("file_chooser_screen")

class WindowManager(ScreenManager):
    pass
class FileBhejo(App):
    def build(self):
        return Builder.load_file("FileBhejo.kv")
    
FileBhejo().run()