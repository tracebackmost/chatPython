import threading
import socket
import time
import random
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import webbrowser
from tkinter.messagebox import askyesno

join = False
shutdown = False

host = socket.gethostbyname(socket.gethostname())
port = 0
server = (socket.gethostbyname(socket.gethostname()), 9090)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))


def receving(s, txt1, txt):
    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            txt1.config(state=NORMAL)
            if 'https://www.' in data:
                yes_no = askyesno('Open website', 'Do you want to open the website,which was send to you?')
                if yes_no:
                    webbrowser.open(data[data.index('[') + 1:data.index(']')])
                    txt.delete('1.0', END)
                    txt1.config(state=DISABLED)
                else:
                    pass
            txt1.insert(INSERT, data.strip() + '\n')
            txt.delete('1.0', END)
            txt1.config(state=DISABLED)
        except:
            pass


def sending(event):
    try:
        message = txt.get('1.0', END)
        time.sleep(0.2)
        if message != '':
            s.sendto(('@' + username + ' : ' + message).encode('utf-8'), server)
    except:
        s.sendto(('@' + username + " : left chat " + '\n').encode("utf-8"), server)


root = Tk()
username = askstring('Type your Username', 'Username:')
bgcolor = askstring('Choose Layout', 'Bg color:', initialvalue='blue')
fgcolor = askstring('Choose Layout', 'Fg color:', initialvalue='red')

try:
    s.sendto(('@' + username + " : join chat " + '\n').encode("utf-8"), server)
    root.config(bg=bgcolor, highlightthickness=0, height=33, width=90)
    txt = ScrolledText(root, width=20, height=8, bg=bgcolor, fg=fgcolor, highlightthickness=0, borderwidth=3,
                       relief='solid')
    txt.pack(side=BOTTOM, expand=YES, fill=BOTH)
    txt1 = ScrolledText(root, width=50, height=25, state=DISABLED, bg=bgcolor, fg=fgcolor, highlightthickness=0,
                        borderwidth=3, relief='solid', font=('Arial Black', 15))
    txt1.pack(side=TOP, expand=YES, fill=BOTH)
except:
    showinfo('ERROR', 'Произошла Ошибка' + '\n' * 3 + 'Повторите попытку позже')
    sys.exit()
else:
    root.bind('<Return>', sending)
    t = threading.Thread(target=receving, args=(s, txt1, txt))
    t.daemon = True
    t.start()

root.mainloop()
