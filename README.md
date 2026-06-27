### ASSIGNMENT OF WEB CHAT APPLICATION
## This assignment is a demonstration of basic web application in which chat is convey 
   between client and server.

## Technologies used
  - Python 3.14
  - Pycharm
  - Socket
  - Port

## HOW TO RUN?
  - Clone the git repository https://github.com/singhnav0309-creator/urban-umbrella

  - Open the Server.py

  - Then, Client.py

  - Run one by one

  - send message to client

  - Client receive it.

## For Example
  - import socket
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
client.connect((HOST_NAME, PORT))



def send(listbox, entry):
    try:
        message = entry.get()
        if listbox:
             listbox.insert('end', "Client :"+ message)
             entry.delete(0, 'end')
             client.send(bytes(message, 'utf-8'))
             receive(listbox)
    except:
        pass


def receive(listbox):
    try:
       message_from_client = client.recv(50)
       if listbox:
              listbox.insert('end', "Server :"+ message_from_client.decode('utf-8'))

    except:
        pass

root = Tk()
root.title("Client")

entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()


button = Button(root, text="Send", command=lambda : send(listbox,entry))
button.pack(side=BOTTOM)
button = Button(root, text="Receive", command=lambda : receive(listbox))
button.pack(side=BOTTOM)



root.mainloop()

## ERRORS REMOVED
  - try- except block is used,
  - in order to prevent crashing the program.

### AUTHOR
     NAVJOT SINGH
