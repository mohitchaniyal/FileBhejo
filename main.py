import socket
import os

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get local machine name
host = socket.gethostname()                           

# Reserve a port for your service
port = 12345                                           

# Connect to the server
s.connect((host, port))

# Open the file
filename = "file.txt"
filesize = os.path.getsize(filename)
file = open(filename, "rb")

# Send the file size
s.sendall(str(filesize).encode())

# Send the file
chunk = file.read(4096)
while chunk:
    s.sendall(chunk)
    chunk = file.read(4096)

# Close the file and socket
file.close()
s.close()
import socket
import os

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get local machine name
host = socket.gethostname()                           

# Reserve a port for your service
port = 12345                                           

# Connect to the server
s.connect((host, port))

# Open the file
filename = "file.txt"
filesize = os.path.getsize(filename)
file = open(filename, "rb")

# Send the file size
s.sendall(str(filesize).encode())

# Send the file
chunk = file.read(4096)
while chunk:
    s.sendall(chunk)
    chunk = file.read(4096)

# Close the file and socket
file.close()
s.close()
