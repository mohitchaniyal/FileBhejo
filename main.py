import socket
import os
import tkinter as tk
from tkinter import filedialog
class FileBhejo:
    name="FileBhejo"
    owner="Mohit Kumar Chaniyal"
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        
        host = socket.gethostbyname(socket.gethostname())
        port = 12345       
        self.local_address=(host,port)
        print(self.local_address)
    def send_file(self,remote_address):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        filename=file_path.split('/')[-1]
        self.s.connect(remote_address)
        
        filesize=os.path.getsize(file_path)
        file=open(file_path,"rb")
        self.s.sendall(filename.encode())
        self.s.sendall(str(filesize).encode())
        chunk=file.read(4096)
        while chunk:
            self.s.sendall(chunk)
            chunk=file.read(4096)
        file.close()
        self.s.close()
    def receive_file(self):
        self.s.bind(self.local_address)
        self.s.listen(1)
        conn,add=self.s.accept()
        print("Connected to:",add)
        filename=conn.recv(4096).decode()
        filesize=int(conn.recv(4096).decode())
        file=open(filename,"wb")
        recieved=0
        while recieved<filesize:
            chunk=conn.recv(4096)
            file.write(chunk)
            recieved+=len(chunk)
        file.close()
        conn.close()
app=FileBhejo()
while True :
    ask=input("S for send R for recieve")
    if ask.lower()=="s":
        remote_address=input("Enter IP"),12345
        app.send_file(remote_address)
    elif ask.lower()=="r":
        app.receive_file()