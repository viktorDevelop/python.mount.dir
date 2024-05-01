from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import os


win = Tk()
win.title("METANIT.COM")
win.geometry("250x200") 

win.title('создание расшариной  папки ssh sf')
win.geometry('500x600+300+100')
# win.resizable(False,False)
win.minsize(300,400)
win.maxsize(500,600)

photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False,photo)


dataServer = []
with open('sites.json') as f:
        tmp = json.load(f)

for item in tmp:
    dataServer.append( (item['name'],item['user'],item['url'],item['mount'], item['server_path']))
  

label = ttk.Label()
label.pack(anchor=N, fill=X)

# определяем столбцы
columns = ("name", "user", "url","mount","server_path")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
tree.heading("name", text="проект")
tree.heading("user", text="пользователь")
tree.heading("url", text="адрес сайта")
tree.heading("mount", text="путь на пк")
tree.heading("server_path", text="путь на сервере")
 
# добавляем данные
for person in dataServer:
    tree.insert("", END, values=person)
    

btn = ttk.Button(text="Монтировать",state=[''])
btn.pack(anchor='sw')


def mounted(event):
    global label
    global os
    global win
    if label['text']:
    
        name, user, url,mount,server_path = label['text'][0]
        comand = 'sshfs '+ user + '@'+ url + ':' + server_path + ' ' + mount
        if os.path.isdir(mount):
            print("Directory exists "+ mount)
        else:
            os.makedirs(mount)
            print("Directory not exists")
             
        win.destroy()
        os.system(comand)
    else:
        label['text'] = 'error'


btn.bind("<ButtonPress-1>", mounted)

def item_selected(event):
    selected_people = ""
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        person = item["values"]
        selected_people = f"{selected_people}{person}\n"
    label["text"]=[person]
 
tree.bind("<<TreeviewSelect>>", item_selected)

win.mainloop()