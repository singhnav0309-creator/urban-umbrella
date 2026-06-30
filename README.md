### ASSIGNMENT OF WEB CHAT APPLICATION
## This assignment is a demonstration of basic web application in which chat is convey 
   between client and server.

## Technologies used
  - Python 3.14
  - Pycharm
  - Socket
  - Port
  - Tkinter
  - Threading

## HOW TO RUN?
  - Clone the git repository https://github.com/singhnav0309-creator/urban-umbrella

  - Open the Server.py

  - Then, Client.py

  - Run one by one

  - send message to client

  - Client receive it.

  - Here, Screenshot is there.

## Destination
|-Client.py
|-Server.py
|-Screenshot
|-main.py

## For Example
   import socket
from tkinter import *
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
conn.bind((HOST_NAME, PORT))
conn.listen(1)
client, address = conn.accept()

root = Tk()
root.title("Jota")

entry = Entry()
entry.pack(side=BOTTOM)

def send(listbox, entry):
    try:
       message = entry.get()
       if message:
              listbox.insert('end', "Server :"+ message)
              entry.delete(0, 'end')
              client.send(message.encode('utf-8'))

    except Exception as error:
        print(error)


def receive(listbox):
    while True:
     try:
        message = client.recv(1024).decode('utf-8')

        if not message:
            break

        listbox.insert('end', "Client :"+ message)


     except Exception as error:
        print(error)

listbox = Listbox(root)
listbox.pack()

thread = threading.Thread(target=receive, args=(listbox,))
thread.daemon =True
thread.start()



def close_window():
    client.close()
    conn.close()

    root.destroy()

button = Button(root, text="Send", command=lambda : send(listbox,entry))
button.pack(side=BOTTOM)


root.mainloop()


## ERRORS REMOVED
  - try- except block is used,
  - in order to prevent crashing the program.

### AUTHOR
     NAVJOT SINGH
