from tkinter import *

root = Tk(screenName='To-Do list')
root.geometry('400x550')

task_list = []

def delete_list():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open(r'E:\portfolio_project\to-do_list\tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def add_task():
    
    task = entry.get()
    entry.delete(0,END)

    if task:
        with open(r'E:\portfolio_project\to-do_list\tasklist.txt','a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert(END,task)

def opentask():

    try:
        global task_list
        with open(r'E:\portfolio_project\to-do_list\tasklist.txt','r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file = open(r'E:\portfolio_project\to-do_list\tasklist.txt','w')
        file.close()

task = PhotoImage(file=r'to-do_list\img\task.png')
root.iconphoto(False,task)

topbar = PhotoImage(file=r'to-do_list\img\topbar.png')
Label(root,image=topbar).pack()

dock = PhotoImage(file=r'E:\portfolio_project\to-do_list\img\dock.png')
Label(root,image=dock,bg='black').place(x=350,y=30)

note = PhotoImage(file=r'E:\portfolio_project\to-do_list\img\task.png') 
Label(root,image=note,bg='#32405b').place(x=30,y=25)

Label(root,text='ALL TASK',font = 'arial 20 bold',fg='white', bg='#32405b').place(x=134,y=25)

frame = Frame(root,width=400,height=50,bg='white')
frame.place(x=0,y=140)

entry = Entry(frame,width=40,font='arial 20',bd=0)
entry.place(x=10,y=7)

button = Button(frame,text='ADD',font='arial 20 bold',width=6,bg='blue',bd=0,command=add_task)
button.place(x=292,y=2)

frame1 = Frame(root,bd=2,width=700,height=280,bg = '#32405b')
frame1.pack(pady=(130,0))

listbox = Listbox(frame1,font='arial 12', width=40,height=13,bg='#32405b')
listbox.pack(side=LEFT,fill=BOTH,padx=2)

del_img = PhotoImage(file=r'E:\portfolio_project\to-do_list\img\delete.png')


scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentask()

delete = Button(image=del_img,master=root,bd=0,command=delete_list)
delete.pack(side=BOTTOM,pady=13)

root.mainloop()