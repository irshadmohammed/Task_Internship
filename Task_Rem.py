#imports
from tkinter import *
import sqlite3
from tkinter import messagebox

#root setup
from pip._internal import index

root = Tk()
root.title("Remainder")
root.minsize(width = 500, height = 500)
root.maxsize(width = 600, height = 600)

#create the database
db = sqlite3.connect('Remainder.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS rem(id INTEGER PRIMARY KEY,TITLE TEXT,DESC TEXT,DATE TEXT,TIME TEXT)")
db.commit()
db.close()


#FRAME
frame = Frame(root,bg="", colormap="new")
frame.place(x=80,y=100)

#the basic elements for the root window
#the listbox that will get updated
list = Listbox(frame) 
list.pack(side=LEFT)

title = StringVar()
desc = StringVar()
date = StringVar()
time = StringVar()

#the insert window
def insert_window():

    inwin = Toplevel()
    inwin.minsize(width=500, height=500)
    inwin.title("Insert Box")
    lbins = Label(inwin,text="Insert Details",font='Helvetica 10 bold underline')
    lbins.place(x=25,y=30)

    lbd = Label(inwin, text="Enter title")
    lbd.place(x=25, y=90)
    pe = Entry(inwin, textvariable = title)
    pe.place(x=160, y=90)

    lbl = Label(inwin, text="Enter Description")
    lbl.place(x=25, y=160)
    de = Entry(inwin, textvariable=desc,width=30)
    de.place(x=160, y=160)

    lb = Label(inwin, text="Enter date")
    lb.place(x=25, y=230)
    ne = Entry(inwin, textvariable=date)
    ne.place(x=160, y=230)

    lb = Label(inwin, text="Enter time")
    lb.place(x=25, y=290)
    te = Entry(inwin, textvariable=time)
    te.place(x=160, y=290)

    button = Button(inwin, text = "Insert", command = insert)
    button.place(x=150,y=346)

#the insert function
def insert():
    global title_i,desc_i,date_i,time_i
    title_i = title.get()
    desc_i = desc.get()
    date_i = date.get()
    time_i = time.get()
    
    conn = sqlite3.connect('Remainder.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO rem(TITLE,DESC,DATE,TIME) VALUES(?,?,?,?)',(title_i,desc_i,date_i,time_i))
        lis = cursor.execute('SELECT TITLE FROM rem')
        messagebox.showinfo("Result","INSERTED SUCCESSFULLY")
        global list
        list.delete(0,END)
        for item in lis:
            list.insert(0, item)
        
        
        title.set('')
        desc.set('')
        date.set('')
        time.set('')

    db.close()

#load the stuff
connt = sqlite3.connect('Remainder.db')
with connt:
    cur = connt.cursor()
    lit = cur.execute('SELECT title DESC FROM rem')
    for item in lit:
        list.insert(0, item)
    db.close()

title_upd=StringVar()
desc_upd=StringVar()
date_upd=StringVar()
time_upd=StringVar()

id=None
titup=None
desup=None
datup=None
tiup=None

def updat():
    
    conn = sqlite3.connect('Remainder.db')
    with conn:
        curup = conn.cursor()
        global id
        global titup
        global desup
        global datup
        global tiup

        titup=str(title_upd.get())
        desup=str(desc_upd.get())
        datup=str(date_upd.get())
        tiup=str(time_upd.get())
        
        print(titup,desup,datup,tiup)
        curup.execute('UPDATE rem SET TITLE=?,DESC=?,DATE=?,TIME=? WHERE ID=?',(titup, desup, datup, tiup, id))
        print(id, titup,desup, datup, tiup)
        conn.commit()
        messagebox.showinfo("Result","UPDATED SUCCESSFULLY")
        lst = cur.execute('SELECT title DESC FROM rem')
        global list
        list.delete(0,END)
        for item in lst:
            list.insert(0, item)

def up():

    value = [list.get(i) for i in list.curselection()]
    for val in value:
        print('upline1', val)
        tit=val[0]
        print('Title: ', tit)
    connt = sqlite3.connect('Remainder.db')
    with connt:
        cur = connt.cursor()
        updtOrig=cur.execute('SELECT * FROM rem WHERE TITLE=?',(tit,))
        print('Original Data: ')
        for i in updtOrig:
            print(i[0],i[1],i[2],i[3],i[4])
            global id
            id=i[0]
            global titup
            titup=i[1]
            global desup
            desup=i[2]
            global datup
            datup=i[3]
            global tiup
            tiup=i[4]
        
    upwin = Toplevel()
    upwin.minsize(width=500, height=500)
    upwin.title("Remainder Details")
    lu=Label(upwin,text="Event Details",font='Helvetica 10 bold underline')
    lu.place(x=80,y=25)

    utit = Label(upwin, text="Enter title")
    utit.place(x=50, y=70)
    etit = Entry(upwin,textvariable=title_upd)
    etit.place(x=180, y=70)
    etit.delete(0,END)
    etit.insert(0,i[1])

    udesc = Label(upwin, text="Enter Description")
    udesc.place(x=45, y=120)
    edesc = Entry(upwin,textvariable=desc_upd)
    edesc.place(x=180, y=120)
    edesc.delete(0,END)
    edesc.insert(0, i[2])

    udate = Label(upwin, text="Enter date")
    udate.place(x=45, y=190)
    uedate = Entry(upwin,textvariable=date_upd)
    uedate.place(x=180, y=190)
    uedate.delete(0,END)
    uedate.insert(0, i[3])

    ultime = Label(upwin, text="Enter time")
    ultime.place(x=45, y=250)
    uetime = Entry(upwin,textvariable=time_upd)
    uetime.place(x=180, y=250)
    uetime.delete(0,END)
    uetime.insert(0, i[4])

    bb=Button(upwin,text="SUBMIT",command=updat)
    bb.place(x=150,y=300)


def view():
    vwin = Toplevel()
    vwin.minsize(width=500, height=500)
    vwin.title("Details")
    vlabel = Label(vwin, text="Reminder Details",font='Helvetica 10 bold underline')
    vlabel.place(x=80, y=25)
    vtit = Label(vwin, text="Title",font='Helvetica 10 bold')
    vtit.place(x=80, y=100)
    vdesc = Label(vwin, text="Description",font='Helvetica 10 bold')
    vdesc.place(x=80, y=150)
    vdate = Label(vwin, text="Date",font='Helvetica 10 bold')
    vdate.place(x=80, y=200)
    vtime = Label(vwin, text="Time",font='Helvetica 10 bold')
    vtime.place(x=80, y=250)
    value = [list.get(i) for i in list.curselection()]
    for val in value:
        print('upline1', val)
        tit=val[0]
        print('Title: ', tit)
    connt = sqlite3.connect('Remainder.db')
    with connt:
        cur = connt.cursor()
        updtOrig=cur.execute('SELECT * FROM rem WHERE TITLE=?',(tit,))
        print('Original Data: ')
        for i in updtOrig:
            print(i[0],i[1],i[2],i[3],i[4])
        print('ID  ----------: ',id)
        print('Titl----------: ',titup)
        print('Desc----------: ',desup)
        print('Date----------: ',datup)
        print('Time----------: ',tiup)
    titres = Label(vwin)
    titres.config(text=i[1])
    titres.place(x=220,y=100)
    descres = Label(vwin)
    descres.config(text=i[2])
    descres.place(x=220,y=150)
    dateres = Label(vwin)
    dateres.config(text=i[3])
    dateres.place(x=220,y=200)
    timeres = Label(vwin)
    timeres.config(text=i[4])
    timeres.place(x=220,y=250)
    

VB=Button(root,text="VIEW",command=view)
VB.place(x=355,y=230)
ub = Button(root,text="UPDATE",command=up)
ub.place(x=350,y=160)

#the insert button
ibutton = Button(root, text = "INSERT", command = insert_window)
ibutton.place(x=350,y=100)
lbhead = Label(root,text="Remainder Application",font='Helvetica 10 bold underline')
lbhead.place(x=180,y=10)
lhead=Label(root,text="Remainder Details",font='Helvetica 10 bold')
lhead.place(x=125,y=50)


#the main window
sb1=Scrollbar(frame,command = list.yview)
sb1.pack(side=LEFT,fill=Y)
sb1.configure(command=list.yview)
list.config(yscrollcommand=sb1.set)
root.mainloop()