import tkinter as tk
from tkinter import filedialog
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Get local machine name
host = socket.gethostname()      
print(host)
print(socket.gethostbyname(host))
root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()

print(folder_path)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path.split('/')[-1])
