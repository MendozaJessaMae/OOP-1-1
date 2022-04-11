from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Welcome to Python Programming")

#add Button widget

btn = Button(window, text = "Click to add name" , fg="blue")
btn.place(x= 80, y = 100)

#Add label widget

lbl = Label(window, text = "Student Personal Information", fg = "Blue", bg = "orange")
lbl.place(x=250, y=70, anchor= 'center')
lbl2 = Label(window, text = "Gender", fg = "red")
lbl2.place(x = 80, y= 150)
#Add text field widget

txtfld = Entry(window, bd = 3, font = ("verdana",16))
txtfld.place(x=200, y=100)

#add ratio button

v1 = StringVar()
v2 = StringVar
v1.set(1)
r1 = Radiobutton(window,text="Male", value = 1 )
r1.place(x=80, y=200)

r2 = Radiobutton(window, text = "Female", value = v2)
r2.place(x=200, y=200)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox = Checkbutton(window, text="basketball", variable=v3)
chkbox2 = Checkbutton(window, text="tennis", variable=v4)
chkbox3 = Checkbutton(window, text="swimming", variable=v5)

chkbox.place(x=80 , y=300)
chkbox2.place(x=250, y= 300)
chkbox3.place(x=350, y= 300)

lbl3 = Label(window, text = "Sports", fg = "red")
lbl3.place(x=80, y=250)

lbl4 = Label(window, text = "Subjects", fg = "red")
lbl4.place(x=80, y=350)
var = StringVar()
var.set("arithmetic")
data1 = "arithmetic"
data2 = "reading"
data3 = "writing"
lstbox = Listbox(window, height=5, selectmode='multiple')
lstbox.insert(END, data1, data2, data3)
lstbox.place(x=80, y=400)

window.mainloop()