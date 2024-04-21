
from tkinter import *
from tkinter import ttk
from array import *
from tkinter import messagebox
import csv
import math
import sys
import time
import datetime
import os

from PIL import Image, ImageTk

global listbox
# end of module importing
try:
    currentDirectory = os.getcwd()
    ###Started("C:\Users\ERICKA JANE ALEGRE\Downloads\memo.py")
except:
    print(" Error : Cannot find the Current Directory. ")

root = Tk()
root.title("Single Contiguous Memory Management")
root.resizable(width=FALSE, height=FALSE)
root.geometry("900x650")
#root.config(bg="#2f2e2c")


windowbg = PhotoImage(file="MMWINDOWBG.png")
windowbg_label = Label(root, image=windowbg)
windowbg_label.place(x=0, y=0, relwidth=1, relheight=1)
image_1 = PhotoImage(file="sizebtnbg.png")
image_2 = PhotoImage(file="sizebtnbg1.png")
image_3 = PhotoImage(file="frontlogo.png")
image_4 = PhotoImage(file="entrytopper1.png")
image_5 = PhotoImage(file="entrytopper.png")
image_6 = PhotoImage(file="info.png")
image_7 = PhotoImage(file="homebtn.png")
image_8 = PhotoImage(file="groupname.png")

BUTTONSCMM = PhotoImage(file = 'BUTTONSCMM.png')
BUTTONMPMM = PhotoImage(file = 'BUTTONMPMM.png')
BUTTONT3MM = PhotoImage(file = 'BUTTONT3MM.png')
BUTTONT4MM = PhotoImage(file = 'BUTTONT4MM.png')
class mainUI:
    def __init__(self):
        pass

    def mainscreen(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.mainscreenlogo = Label(root, image=image_3, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.mainscreenlogo.place(x=0, y=0)
        self.basicWidgetList.append(self.mainscreenlogo)


        self.bg1LBL = Label(root,bg="black")
        self.bg1LBL.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL)

        self.LOGOBUTTON1 = Button(root, image=BUTTONSCMM, command=self.mainInput1_window,
                              bg="#f77f00",  relief="sunken")
        self.LOGOBUTTON1.place(x=60, y=460)
        self.basicWidgetList.append(self.LOGOBUTTON1)

        self.LOGOBUTTON2 = Button(root, image=BUTTONMPMM,
                              bg="#f77f00",  relief="sunken")
        self.LOGOBUTTON2.place(x=260, y=460)
        self.basicWidgetList.append(self.LOGOBUTTON2)

        self.LOGOBUTTON3 = Button(root, image=BUTTONT3MM,
                                  bg="#f77f00", relief="sunken")
        self.LOGOBUTTON3.place(x=460, y=460)
        self.basicWidgetList.append(self.LOGOBUTTON3)

        self.LOGOBUTTON4 = Button(root, image=BUTTONT4MM,
                                  bg="#f77f00", relief="sunken")
        self.LOGOBUTTON4.place(x=660, y=460)
        self.basicWidgetList.append(self.LOGOBUTTON4)

        self.LOGOBUTTON5 = Button(root, image=image_6, command=self.Batmassonic_screen,
                                  bg="#f77f00", relief="sunken")
        self.LOGOBUTTON5.place(x=20, y=20)
        self.basicWidgetList.append(self.LOGOBUTTON5)


    def Batmassonic_screen(self):
        self.mainscreenlogo = Label(root, image=image_8, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.mainscreenlogo.place(x=0, y=0)
        self.basicWidgetList.append(self.mainscreenlogo)

        self.LOGOBUTTON6 = Button(root, image=image_7, command=self.mainscreen,
                                  bg="#f77f00", relief="sunken")
        self.LOGOBUTTON6.place(x=20, y=20)
        self.basicWidgetList.append(self.LOGOBUTTON6)

    # For getting the current date
    def current_date(self):
        self.dateString = datetime.date.today().strftime("%B %d, %Y")
        self.dateLBL.config(text=self.dateString)

    # This updates the clock widget
    def tick(self):
        if self.tick_on:
            self.timeString = time.strftime("%H:%M:%S")
            self.clockLBL.config(text=self.timeString)
            self.clockLBL.after(200, self.tick)
        else:
            pass

    def isNotTimeFormat(self, timeInput):
        try:
            time.strptime(timeInput, '%H:%M')
            return False
        except ValueError:
            return True


    def isNotInteger(self, integerInput):
        try:
            self.intTest = int(integerInput)
            return False
        except ValueError:
            return True


    def clearWidgets(self):
        try:
            self.tick_on = False
            self.clearWidgetList(self.basicWidgetList)
            self.clearWidgetList(self.physicalMemWidgets)
        except:
            pass
        return


    def clearWidgetList(self, widgetsToClear):
        for widget in widgetsToClear:
            widget.destroy()

    def displayMap(self, tempPointer, tempColor, tempText, tempPercentage, tempTotalSize):
        self.tempPointer = int(tempPointer)
        self.tempColor = tempColor
        self.tempText = tempText
        self.tempPercentage = tempPercentage
        self.tempTotalSize = tempTotalSize

        if self.tempPercentage != 0:
            self.tempLBL = Label(root, text="          " * 25, font=('Poppins', 1), bg=self.tempColor)
            self.tempLBL.place(x=80, y=self.yCounter)
            self.yCounter += 7
            self.physicalMemWidgets.append(self.tempLBL)

            self.tempLBL = Label(root, text=self.tempText, font=('Poppins', 10), bg=self.tempColor)
            self.tempLBL.place(x=350, y=self.yCounter)
            self.physicalMemWidgets.append(self.tempLBL)
        for i in range(int(self.tempPercentage / 2)):
            if self.tempPointer != 0:
                self.tempLBL = Label(root, text="          " * 25, font=('Poppins', 1), bg=self.tempColor)
                self.tempLBL.place(x=80, y=self.yCounter)
                self.yCounter += 7
                self.physicalMemWidgets.append(self.tempLBL)
                self.tempPointer -= 1
            else:
                pass
        if self.tempPercentage != 0:
            self.tempLBL = Label(root, text=tempTotalSize, font=('Poppins', 10), bg=self.tempColor)
            self.tempLBL.place(x=50, y=self.yCounter - 20)
            self.physicalMemWidgets.append(self.tempLBL)
        return

    # This functions has all the necessary computations for the computation result.
    def mainInput1_computeBTN_Pressed(self):
        if messagebox.askyesno("Confirmation...", " Are you sure you want to compute? ") == True:
            self.size1 = self.size1ENTRY.get()
            self.size2 = self.size2ENTRY.get()
            self.size3 = self.size3ENTRY.get()
            self.size4 = self.size4ENTRY.get()
            self.size5 = self.size5ENTRY.get()

            self.memSize = self.memSizeENTRY.get()
            self.osSize = self.osSizeENTRY.get()

            self.memSize_Check = self.isNotInteger(self.memSize)
            self.osSize_Check = self.isNotInteger(self.osSize)

            self.size1_Check = self.isNotInteger(self.size1)
            self.size2_Check = self.isNotInteger(self.size2)
            self.size3_Check = self.isNotInteger(self.size3)
            self.size4_Check = self.isNotInteger(self.size4)
            self.size5_Check = self.isNotInteger(self.size5)

            self.arrivalTime1 = self.arrivalTime1ENTRY.get()
            self.arrivalTime2 = self.arrivalTime2ENTRY.get()
            self.arrivalTime3 = self.arrivalTime3ENTRY.get()
            self.arrivalTime4 = self.arrivalTime4ENTRY.get()
            self.arrivalTime5 = self.arrivalTime5ENTRY.get()

            self.arrivalTime1_Check = self.isNotTimeFormat(self.arrivalTime1)
            self.arrivalTime2_Check = self.isNotTimeFormat(self.arrivalTime2)
            self.arrivalTime3_Check = self.isNotTimeFormat(self.arrivalTime3)
            self.arrivalTime4_Check = self.isNotTimeFormat(self.arrivalTime4)
            self.arrivalTime5_Check = self.isNotTimeFormat(self.arrivalTime5)

            self.runTime1 = self.runTime1ENTRY.get()
            self.runTime2 = self.runTime2ENTRY.get()
            self.runTime3 = self.runTime3ENTRY.get()
            self.runTime4 = self.runTime4ENTRY.get()
            self.runTime5 = self.runTime5ENTRY.get()

            self.runTime1_Check = self.isNotTimeFormat(self.runTime1)
            self.runTime2_Check = self.isNotTimeFormat(self.runTime2)
            self.runTime3_Check = self.isNotTimeFormat(self.runTime3)
            self.runTime4_Check = self.isNotTimeFormat(self.runTime4)
            self.runTime5_Check = self.isNotTimeFormat(self.runTime5)

            if self.memSize_Check or self.osSize_Check:
                print("Error: Invalid Memory or OS Size input.")
                messagebox.showinfo("Compute Error", "Error: Invalid Memory or OS Size input.")
            elif int(self.memSize) < int(self.osSize):
                print(" Error: Os Size can't exceed Memory Size. ")
                messagebox.showinfo("Compute Error", "Error: Os Size can't exceed Memory Size.")
            elif self.size1_Check or self.size2_Check or self.size3_Check or self.size4_Check or self.size5_Check:
                print("Error: Size input detected as not an integer.")
                messagebox.showinfo("Compute Error", "Error: Size input detected as not an integer.")
            elif (int(self.size1) > (int(self.memSize) - int(self.osSize))) or (
                    int(self.size2) > (int(self.memSize) - int(self.osSize))) or (
                    int(self.size3) > (int(self.memSize) - int(self.osSize))) or (
                    int(self.size4) > (int(self.memSize) - int(self.osSize))) or (
                    int(self.size5) > (int(self.memSize) - int(self.osSize))):
                print("Error: Size input should not exceed ( Memory Size - OS Size ).")
                messagebox.showinfo("Compute Error", "Error: Size input should not exceed ( Memory Size - OS Size ).")
            elif self.arrivalTime1_Check or self.arrivalTime2_Check or self.arrivalTime3_Check or self.arrivalTime4_Check or self.arrivalTime5_Check:
                print(" Error in arrival time input ")
                messagebox.showinfo("Compute Error", "Error: Invalid Arrival Time Input.")
            elif self.runTime1_Check or self.runTime2_Check or self.runTime3_Check or self.runTime4_Check or self.runTime5_Check:
                print("Error: Invalid Run Time Input.")
                messagebox.showinfo("Compute Error", "Error: Invalid Run Time Input.")
            else:
                self.osPercentage = float((int(self.osSize) / int(self.memSize)) * 100)
                self.job1Percentage = float((int(self.size1) / int(self.memSize)) * 100)
                self.wasted1 = float(self.memSize) - (int(self.osSize) + int(self.size1))
                self.wasted1Percentage = int((int(self.wasted1) / int(self.memSize)) * 100)
                # self.physicalMemInfo1 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job1Percentage), "#c2c4c3", "Job 1 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size1))]]

                self.job2Percentage = float((int(self.size2) / int(self.memSize)) * 100)
                self.wasted2 = float(self.memSize) - (int(self.osSize) + int(self.size2))
                self.wasted2Percentage = float((int(self.wasted2) / int(self.memSize)) * 100)
                # self.physicalMemInfo2 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job2Percentage), "#c2c4c3", "Job 2 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size2))]]

                self.job3Percentage = float((int(self.size3) / int(self.memSize)) * 100)
                self.wasted3 = float(self.memSize) - (int(self.osSize) + int(self.size3))
                self.wasted3Percentage = float((int(self.wasted3) / int(self.memSize)) * 100)
                # self.physicalMemInfo3 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job3Percentage), "#c2c4c3", "Job 3 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size3))]]

                self.job4Percentage = float((int(self.size4) / int(self.memSize)) * 100)
                self.wasted4 = float(self.memSize) - (int(self.osSize) + int(self.size4))
                self.wasted4Percentage = float((int(self.wasted4) / int(self.memSize)) * 100)
                # self.physicalMemInfo4 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job4Percentage), "#c2c4c3", "Job 4 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size4))]]

                self.job5Percentage = float((int(self.size5) / int(self.memSize)) * 100)
                self.wasted5 = float(self.memSize) - (int(self.osSize) + int(self.size5))
                self.wasted5Percentage = float((int(self.wasted5) / int(self.memSize)) * 100)
                # self.physicalMemInfo5 = [ [ self.osPercentage, "#f2f5f4", "OS Size", "" ], [ (self.osPercentage + self.job5Percentage), "#c2c4c3", "Job 5 Size", self.osSize], [ 0, "#979998", "Wasted", (int(self.osSize) + int(self.size5))]]

                self.time_zero = datetime.datetime.strptime('00:00', '%H:%M')

                self.startTime1 = datetime.datetime.strptime(self.arrivalTime1, '%H:%M')
                if (self.startTime1 - datetime.datetime.strptime(self.arrivalTime1, '%H:%M')).total_seconds() < 0:
                    self.cpuWait1 = "0:00:00"
                    self.startTime1 = datetime.datetime.strptime(self.arrivalTime1, '%H:%M')
                else:
                    self.cpuWait1 = self.startTime1 - datetime.datetime.strptime(self.arrivalTime1, '%H:%M')

                self.finishTime1 = (
                            self.startTime1 - self.time_zero + (datetime.datetime.strptime(self.runTime1, '%H:%M')))
                self.startTime2 = self.finishTime1

                if (self.startTime2 - datetime.datetime.strptime(self.arrivalTime2, '%H:%M')).total_seconds() < 0:
                    self.cpuWait2 = "0:00:00"
                    self.startTime2 = datetime.datetime.strptime(self.arrivalTime2, '%H:%M')
                else:
                    self.cpuWait2 = self.startTime2 - datetime.datetime.strptime(self.arrivalTime2, '%H:%M')

                self.finishTime2 = (
                            self.startTime2 - self.time_zero + (datetime.datetime.strptime(self.runTime2, '%H:%M')))
                self.startTime3 = self.finishTime2

                if (self.startTime3 - datetime.datetime.strptime(self.arrivalTime3, '%H:%M')).total_seconds() < 0:
                    self.cpuWait3 = "0:00:00"
                    self.startTime3 = datetime.datetime.strptime(self.arrivalTime3, '%H:%M')
                else:
                    self.cpuWait3 = self.startTime3 - datetime.datetime.strptime(self.arrivalTime3, '%H:%M')

                self.finishTime3 = (
                            self.startTime3 - self.time_zero + (datetime.datetime.strptime(self.runTime3, '%H:%M')))
                self.startTime4 = self.finishTime3

                if (self.startTime4 - datetime.datetime.strptime(self.arrivalTime4, '%H:%M')).total_seconds() < 0:
                    self.startTime4 = datetime.datetime.strptime(self.arrivalTime4, '%H:%M')
                    self.cpuWait4 = "0:00:00"
                else:
                    self.cpuWait4 = self.startTime4 - datetime.datetime.strptime(self.arrivalTime4, '%H:%M')

                self.finishTime4 = (
                            self.startTime4 - self.time_zero + (datetime.datetime.strptime(self.runTime4, '%H:%M')))
                self.startTime5 = self.finishTime4

                if (self.startTime5 - datetime.datetime.strptime(self.arrivalTime5, '%H:%M')).total_seconds() < 0:
                    self.startTime5 = datetime.datetime.strptime(self.arrivalTime5, '%H:%M')
                    self.cpuWait5 = "0:00:00"
                else:
                    self.cpuWait5 = self.startTime5 - datetime.datetime.strptime(self.arrivalTime5, '%H:%M')

                self.finishTime5 = (
                            self.startTime5 - self.time_zero + (datetime.datetime.strptime(self.runTime5, '%H:%M')))
                self.mainResult1_window()

    def mainInput1_window(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root,bg="black")
        self.bg1LBL.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL)

        self.clockLBL = Label(root, font=('Poppins', 16), bg="#ffffff")
        self.clockLBL.place(x=730, y=165)
        self.tick_on = True
        self.tick()
        self.basicWidgetList.append(self.clockLBL)

        #self.clockLBL1 = Label(root, text="Time:", font=('Poppins', 13), bg="#FFD53E")
        #self.clockLBL1.place(x=630, y=190)
        #self.basicWidgetList.append(self.clockLBL1)

        self.dateLBL = Label(root, font=('Poppins', 16), bg="#ffffff")
        self.dateLBL.place(x=730, y=125)
        self.current_date()
        self.basicWidgetList.append(self.dateLBL)

        #self.dateLBL1 = Label(root, text="Date:", font=('Poppins', 13), bg="#FFD53E")
        #self.dateLBL1.place(x=630, y=150)
        #self.basicWidgetList.append(self.dateLBL1)

        #self.title1LBL = Label(root, text="SINGLE CONTIGUOUS MEMORY MANAGEMENT", font=('Poppins', 20), bg="#ffff00")
        #self.title1LBL.place(x=150, y=40)
        #self.basicWidgetList.append(self.title1LBL)

        #self.title2LBL = Label(root, text="GROUP NAMIN", font=('Poppins', 20), bg="#ffd400")
        #self.title2LBL.place(x=390, y=90)
        #self.basicWidgetList.append(self.title2LBL)

        self.jobLBL = Label(root, text="Job", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.jobLBL.place(x=32, y=258)
        self.basicWidgetList.append(self.jobLBL)

        self.job1LBL = Label(root, text="1", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job1LBL.place(x=32, y=317)
        self.basicWidgetList.append(self.job1LBL)

        self.job2LBL = Label(root, text="2", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job2LBL.place(x=32, y=367)
        self.basicWidgetList.append(self.job2LBL)

        self.job3LBL = Label(root, text="3", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job3LBL.place(x=32, y=417)
        self.basicWidgetList.append(self.job3LBL)

        self.job4LBL = Label(root, text="4", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job4LBL.place(x=32, y=467)
        self.basicWidgetList.append(self.job4LBL)

        self.job5LBL = Label(root, text="5", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job5LBL.place(x=32, y=517)
        self.basicWidgetList.append(self.job5LBL)

        self.sizeLBL = Label(root, text="Size", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.sizeLBL.place(x=135, y=257)
        self.basicWidgetList.append(self.sizeLBL)

        self.size1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size1ENTRY.place(x=135, y=320)
        self.basicWidgetList.append(self.size1ENTRY)

        self.size2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size2ENTRY.place(x=135, y=370)
        self.basicWidgetList.append(self.size2ENTRY)

        self.size3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size3ENTRY.place(x=135, y=420)
        self.basicWidgetList.append(self.size3ENTRY)

        self.size4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size4ENTRY.place(x=135, y=470)
        self.basicWidgetList.append(self.size4ENTRY)

        self.size5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.size5ENTRY.place(x=135, y=520)
        self.basicWidgetList.append(self.size5ENTRY)

        self.arrivalTimeLBL = Label(root, text="Arrival Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.arrivalTimeLBL.place(x=390, y=257)
        self.basicWidgetList.append(self.arrivalTimeLBL)

        self.arrivalTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime1ENTRY.place(x=390, y=320)
        self.basicWidgetList.append(self.arrivalTime1ENTRY)

        self.arrivalTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime2ENTRY.place(x=390, y=370)
        self.basicWidgetList.append(self.arrivalTime2ENTRY)

        self.arrivalTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime3ENTRY.place(x=390, y=420)
        self.basicWidgetList.append(self.arrivalTime3ENTRY)

        self.arrivalTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime4ENTRY.place(x=390, y=470)
        self.basicWidgetList.append(self.arrivalTime4ENTRY)

        self.arrivalTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.arrivalTime5ENTRY.place(x=390, y=520)
        self.basicWidgetList.append(self.arrivalTime5ENTRY)

        self.runTimeLBL = Label(root, text="Run Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.runTimeLBL.place(x=640, y=257)
        self.basicWidgetList.append(self.runTimeLBL)

        self.runTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime1ENTRY.place(x=640, y=320)
        self.basicWidgetList.append(self.runTime1ENTRY)

        self.runTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime2ENTRY.place(x=640, y=370)
        self.basicWidgetList.append(self.runTime2ENTRY)

        self.runTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime3ENTRY.place(x=640, y=420)
        self.basicWidgetList.append(self.runTime3ENTRY)

        self.runTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime4ENTRY.place(x=640, y=470)
        self.basicWidgetList.append(self.runTime4ENTRY)

        self.runTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.runTime5ENTRY.place(x=640, y=520)
        self.basicWidgetList.append(self.runTime5ENTRY)

        #img label for date and time
        self.memSizeLBL = Label(root, image=image_2, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.memSizeLBL.place(x=585, y=120)
        self.basicWidgetList.append(self.memSizeLBL)

        self.topper = Label(root, image=image_4, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.topper.place(x=0, y=0)
        self.basicWidgetList.append(self.topper)


        self.memSizeENTRY = Entry(root, font=('Poppins', 13, 'bold'), justify="center", bg="#ffffff")
        self.memSizeENTRY.place(x=210, y=125)
        self.basicWidgetList.append(self.memSizeENTRY)


        self.osSizeLBL = Label(root, image=image_1, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.osSizeLBL.place(x=68, y=120)
        self.basicWidgetList.append(self.osSizeLBL)

        self.osSizeENTRY = Entry(root, font=('Poppins', 13, 'bold'), justify="center", bg="#ffffff")
        self.osSizeENTRY.place(x=210, y=165)
        self.basicWidgetList.append(self.osSizeENTRY)

        self.computeBTN = Button(root, text='Compute', command=self.mainInput1_computeBTN_Pressed, font=('Poppins', 16, 'bold'),
                                 width=12, bg="#eae2b7",  height=1, borderwidth=5, relief="sunken")
        self.computeBTN.place(x=70, y=570)
        self.basicWidgetList.append(self.computeBTN)

        self.exitBTN = Button(root, text='Exit', command=root.destroy, font=('Poppins', 16, 'bold'), width=12,
                              activebackground="#f77f00", height=1, borderwidth=5, relief="sunken")
        self.exitBTN.place(x=660, y=570)
        self.basicWidgetList.append(self.exitBTN)

    def mainResult1_window(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL = Label(root, bg="black")
        self.bg1LBL.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL)

        #self.title1LBL = Label(root, text="SINGLE CONTIGUOUS MEMORY MANAGEMENT", font=('Helvetica', 20),
         #                      bg="#ffff00")
        #self.title1LBL.place(x=150, y=40)
        #self.basicWidgetList.append(self.title1LBL)

        #self.title2LBL = Label(root, text="GROUP NAMIN", font=('Poppins', 20), bg="#ffd400")
        #self.title2LBL.place(x=390, y=90)
        #self.basicWidgetList.append(self.title2LBL)

        #self.dateLBL = Label(root, font=('Poppins', 16), bg="#ffffff")
        #self.dateLBL.place(x=730, y=125)
        #self.current_date()
        #self.basicWidgetList.append(self.dateLBL)

        self.jobLBL = Label(root, text="Job", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.jobLBL.place(x=32, y=210)
        self.basicWidgetList.append(self.jobLBL)

        self.job1LBL = Label(root, text="1", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job1LBL.place(x=32, y=277)
        self.basicWidgetList.append(self.job1LBL)

        self.job2LBL = Label(root, text="2", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job2LBL.place(x=32, y=337)
        self.basicWidgetList.append(self.job2LBL)

        self.job3LBL = Label(root, text="3", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job3LBL.place(x=32, y=397)
        self.basicWidgetList.append(self.job3LBL)

        self.job4LBL = Label(root, text="4", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job4LBL.place(x=32, y=457)
        self.basicWidgetList.append(self.job4LBL)

        self.job5LBL = Label(root, text="5", font=('Poppins', 15), bg="#FFD53E", height=1, width=5, borderwidth=7, relief="raised")
        self.job5LBL.place(x=32, y=517)
        self.basicWidgetList.append(self.job5LBL)

        self.startTimeLBL = Label(root, text="Start Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.startTimeLBL.place(x=130, y=210)
        self.basicWidgetList.append(self.startTimeLBL)

        self.startTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime1ENTRY.place(x=130, y=280)
        self.startTime1ENTRY.insert(0, self.startTime1.time())
        self.startTime1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime1ENTRY)

        self.startTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime2ENTRY.place(x=130, y=340)
        self.startTime2ENTRY.insert(0, self.startTime2.time())
        self.startTime2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime2ENTRY)

        self.startTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime3ENTRY.place(x=130, y=400)
        self.startTime3ENTRY.insert(0, self.startTime3.time())
        self.startTime3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime3ENTRY)

        self.startTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime4ENTRY.place(x=130, y=460)
        self.startTime4ENTRY.insert(0, self.startTime4.time())
        self.startTime4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime4ENTRY)

        self.startTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.startTime5ENTRY.place(x=130, y=520)
        self.startTime5ENTRY.insert(0, self.startTime5.time())
        self.startTime5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.startTime5ENTRY)

        self.finishTimeLBL = Label(root, text="Finish Time", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.finishTimeLBL.place(x=380, y=210)
        self.basicWidgetList.append(self.finishTimeLBL)

        self.finishTime1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime1ENTRY.place(x=380, y=280)
        self.finishTime1ENTRY.insert(0, self.finishTime1.time())
        self.finishTime1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime1ENTRY)

        self.finishTime2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime2ENTRY.place(x=380, y=340)
        self.finishTime2ENTRY.insert(0, self.finishTime2.time())
        self.finishTime2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime2ENTRY)

        self.finishTime3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime3ENTRY.place(x=380, y=400)
        self.finishTime3ENTRY.insert(0, self.finishTime3.time())
        self.finishTime3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime3ENTRY)

        self.finishTime4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime4ENTRY.place(x=380, y=460)
        self.finishTime4ENTRY.insert(0, self.finishTime4.time())
        self.finishTime4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime4ENTRY)

        self.finishTime5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.finishTime5ENTRY.place(x=380, y=520)
        self.finishTime5ENTRY.insert(0, self.finishTime5.time())
        self.finishTime5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.finishTime5ENTRY)

        self.cpuWaitLBL = Label(root, text="CPU Wait", font=('Poppins', 15), bg="#FFD53E", height=1, width=19, borderwidth=7, relief="raised")
        self.cpuWaitLBL.place(x=630, y=210)
        self.basicWidgetList.append(self.cpuWaitLBL)

        self.cpuWait1ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait1ENTRY.place(x=630, y=280)
        self.cpuWait1ENTRY.insert(0, self.cpuWait1)
        self.cpuWait1ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait1ENTRY)

        self.cpuWait2ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait2ENTRY.place(x=630, y=340)
        self.cpuWait2ENTRY.insert(0, self.cpuWait2)
        self.cpuWait2ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait2ENTRY)

        self.cpuWait3ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait3ENTRY.place(x=630, y=400)
        self.cpuWait3ENTRY.insert(0, self.cpuWait3)
        self.cpuWait3ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait3ENTRY)

        self.cpuWait4ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait4ENTRY.place(x=630, y=460)
        self.cpuWait4ENTRY.insert(0, self.cpuWait4)
        self.cpuWait4ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait4ENTRY)

        self.cpuWait5ENTRY = Entry(root, font=('Poppins', 15, 'bold'), justify="center")
        self.cpuWait5ENTRY.place(x=630, y=520)
        self.cpuWait5ENTRY.insert(0, self.cpuWait5)
        self.cpuWait5ENTRY.config(state="readonly")
        self.basicWidgetList.append(self.cpuWait5ENTRY)

        self.topper1 = Label(root, image=image_4, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.topper1.place(x=0, y=0)
        self.basicWidgetList.append(self.topper1)


        self.backBTN = Button(root, text='BACK', command=self.mainInput1_window, font=('Poppins', 16, 'bold'), width=12,
                              bg="#f77f00",  height=1, borderwidth=5, relief="sunken")
        self.backBTN.place(x=70, y=580)
        self.basicWidgetList.append(self.backBTN)

        self.nextBTN = Button(root, text='NEXT', command=self.mainResult2_window, font=('Poppins', 16, 'bold'),
                              width=12, bg="#f77f00",  height=1, borderwidth=5, relief="sunken")
        self.nextBTN.place(x=250, y=580)
        self.basicWidgetList.append(self.nextBTN)

        self.exitBTN = Button(root, text='Exit', command=root.destroy, font=('Poppins', 16, 'bold'), width=12,
                              bg="#f77f00",  height=1, borderwidth=5, relief="sunken")
        self.exitBTN.place(x=680, y=580)
        self.basicWidgetList.append(self.exitBTN)



programStart = mainUI()
programStart.mainscreen()
root.mainloop()
