import socket
from tkinter import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
server.bind((HOST_NAME, PORT))
server.listen(1)
client, address = server.accept()

def send(listbox, entry):
    try:
       message = entry.get()
       if listbox:
              listbox.insert('end', "Server :"+ message)
              entry.delete(0, 'end')
              client.send(bytes(message, 'utf-8'))
              receive(listbox)

    except:
        pass


def receive(listbox):
    try:
       message_from_client = client.recv(50)
       if listbox:
             listbox.insert('end', "Client : "+ message_from_client.decode('utf-8'))


    except:
        pass

root = Tk()
root.title("Server")


entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()


button = Button(root, text="Send", command=lambda : send(listbox,entry))
button.pack(side=BOTTOM)
button = Button(root, text="Receive", command=lambda : receive(listbox))
button.pack(side=BOTTOM)

root.after(10, receive)

root.mainloop()

