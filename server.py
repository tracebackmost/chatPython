from gui_outputs import GuiOutput
import socket
from tkinter import *
from tkinter.messagebox import askyesno

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(False)


def main_func():
    try:
        data, addr = s.recvfrom(2048)
        if addr not in clients:
            clients.append(addr)
        print("[" + addr[0] + "][" + str(addr[1]) + "]",
              end="")
        if not crypt:
            print((data.decode('utf-8')).strip() + '\n')
        else:
            print(': The message was delivered successfully')
        for client in clients:
            if '[https://www.' in data.decode('utf-8'):
                if addr != client:
                    s.sendto(data, client)
            else:
                s.sendto(data, client)
    except BlockingIOError:
        pass
    root.after(10, main_func)


root = Tk()
sys.stdout = GuiOutput(root, 75, 25)
print("[ Server Started ]")
crypt = askyesno('Information', 'Should the chat be encrypted')
a = askyesno('Socket', 'Do you need the server information?')
if not a:
    root.iconify()
main_func()

root.mainloop()
