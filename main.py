import socket
import os
import tkinter as tk
from tkinter import filedialog
class FileBhejo:
    name="FileBhejo"
    owner="Mohit Kumar Chaniyal"
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host = socket.gethostname() 
        port = 12345       
        self.local_address=(host,port)
    def send_file(self,remote_address):
        self.s.connect(remote_address)
        filename="file.txt"
        filesize=os.path.getsize(filename)
        file=open(filename,"rb")
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
        filename=self.s.recv(4096).decode()
        filesize=self.s.recv(4096).decode()
        file=open(filename,"wb")
        recieved=0
        while recieved<filesize:
            chunk=conn.recv(4096)
            file.write(chunk)
            recieved+=len(chunk)
        file.close()
        conn.close()

