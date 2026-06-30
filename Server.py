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

