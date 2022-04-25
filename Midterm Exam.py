from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Midterm in OOP")

#Add Label Widget

lbl = Label(window, text = "Enter Your Full Name:", fg = "Red")
lbl.place(x = 80, y = 100)

#Add Text Field Widget

txtfld = Entry(window, bd = 4, font = ("Verdana", 16))
txtfld.place(x = 300, y = 100)

txtfld1 = Entry(window, bd = 4, font = ("Verdana", 16))
txtfld1.place(x = 300, y = 150)
def Button_Command():
  txtfld1.insert(END, str(txtfld.get()))

#Add Button Widget

btn = Button(window, text = "Click to display your Fullname", fg = "Red", command = Button_Command)
btn.place(x = 70, y = 150)

window.mainloop()