#-------------------------------------------------------#
# https://www.github.com/VitorSilvaAlvesLucas/CalcPy-v1.0
#-------------------------------------------------------#
#-Imports------------------------------------#
try:
   from tkinter import *
   import os
except Exception as error_import:
    messagebox.showerror("Error",error_import)
#--------------------------------------------#

class CalcPy:
    def __init__(self,window_tk):
        #-Window Attributes-----------------#
        directory = os.getcwd()
        self.window_tk = window_tk
        self.window_tk.title("CalcPy")
        self.window_tk.geometry("250x320")
        self.window_tk.iconbitmap("{}\icon_calcpy.ico".format(directory))
        self.window_tk["bg"] = "#424242"
        self.window_tk.resizable(False,False)
        #-----------------------------------#
        #-Frames---------------------------#
        result_frame = Frame(self.window_tk)
        button_frame = Frame(self.window_tk)
        button_frame1 = Frame(self.window_tk)
        button_frame2 = Frame(self.window_tk)
        button_frame3 = Frame(self.window_tk)
        button_frame4 = Frame(self.window_tk)
        #-----------------------------------#
        #-Entry------------------------------------------------------------------------#
        self.entry = Entry(result_frame,width=18,fg="white",bg="#848484",font=("Calibri",18))
        #------------------------------------------------------------------------------#
        #-Buttons------------------------------------------------------------------------------#
        sqrt = Button(button_frame,text="√",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bsqrt) 
        div = Button(button_frame,text="/",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bdiv) 
        mul = Button(button_frame,text="*",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bmul) 
        sub = Button(button_frame,text="-",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bsub)
        #--------------------------------------------------------------------------------------#
        #-Buttons 1----------------------------------------------------------------------------#
        n7 = Button(button_frame1,text="7",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b7)
        n8 = Button(button_frame1,text="8",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b8)
        n9 = Button(button_frame1,text="9",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b9)
        som = Button(button_frame1,text="+",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bsom)
        #--------------------------------------------------------------------------------------#
        #-Buttons 2----------------------------------------------------------------------------#
        n4 = Button(button_frame2,text="4",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b4)
        n5 = Button(button_frame2,text="5",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b5)
        n6 = Button(button_frame2,text="6",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b6)
        rest = Button(button_frame2,text="%",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.brest)
        #--------------------------------------------------------------------------------------#
        #-Buttons 3-------------------------------------------------------------------------------#
        n1 = Button(button_frame3,text="1",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b1)
        n2 = Button(button_frame3,text="2",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b2)
        n3 = Button(button_frame3,text="3",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.b3)
        dele = Button(button_frame3,text="Del",bg="#2E2E2E",fg="white",font=("Calibri",16),width=4,command=self.bdel)
        #-----------------------------------------------------------------------------------------#
        #-Buttons 4--------------------------------------------------------------------------------#
        n0 = Button(button_frame4,text="0",bg="#2E2E2E",fg="white",font=("Calibri",16),width=9,command=self.b0) 
        ent = Button(button_frame4,text="=",bg="#2E2E2E",fg="white",font=("Calibri",16),width=9,command=self.bent)
        #------------------------------------------------------------------------------------------#
        #-Pack Frames/Entry------#
        result_frame.pack(pady=10)
        button_frame.pack()
        button_frame1.pack()
        button_frame2.pack()
        button_frame3.pack()
        button_frame4.pack()
        self.entry.pack(ipady=13)
        #------------------------#
        #-Pack Buttons 0---#
        sqrt.pack(side=LEFT)
        div.pack(side=LEFT)
        mul.pack(side=LEFT)
        sub.pack(side=LEFT)
        #-----------------#
        #-Pack Buttons 1--#
        n7.pack(side=LEFT)
        n8.pack(side=LEFT)
        n9.pack(side=LEFT)
        som.pack(side=LEFT)
        #-----------------#
        #-Pack Buttons 2--#
        n4.pack(side=LEFT)
        n5.pack(side=LEFT)
        n6.pack(side=LEFT)
        rest.pack(side=LEFT)
        #-----------------#
        #-Pack Buttons 3---#
        n1.pack(side=LEFT)
        n2.pack(side=LEFT)
        n3.pack(side=LEFT)
        dele.pack(side=LEFT)
        #------------------#
        #-Pack Buttons 4--#
        n0.pack(side=LEFT)
        ent.pack(side=LEFT)
        #-----------------#
        #-MainLoop Window-------#
        self.window_tk.mainloop()
        #-----------------------#
    def b0(self):
        self.entry.insert(END,"0")
    def b1(self):
        self.entry.insert(END,"1")
    def b2(self):
        self.entry.insert(END,"2")
    def b3(self):
        self.entry.insert(END,"3")
    def b4(self):
        self.entry.insert(END,"4")
    def b5(self):
        self.entry.insert(END,"5")
    def b6(self):
        self.entry.insert(END,"6")
    def b7(self):
        self.entry.insert(END,"7")
    def b8(self):
        self.entry.insert(END,"8")
    def b9(self):
        self.entry.insert(END,"9")
    def bsom(self):
        self.op = 0
        self.v1 = self.entry.get()
        self.entry.delete(first=0,last=100)
    def bsub(self):
        self.op = 1
        self.v1 = self.entry.get()
        self.entry.delete(first=0,last=100)
    def bmul(self):
        self.op = 2
        self.v1 = self.entry.get()
        self.entry.delete(first=0,last=100)
    def bdiv(self):
        self.op = 3
        self.v1 = self.entry.get()
        self.entry.delete(first=0,last=100)
    def bdel(self):
        self.entry.delete(first=0,last=100)
    def bsqrt(self):
        try:
            self.v1 = self.entry.get()
            self.entry.delete(first=0,last=100)
            r = (float(self.v1) ** (1/2))
            r = str(r)
            self.entry.insert(END,r)
        except Exception as error_sqrt:
            pass
    def brest(self):
        self.op = 4
        self.v1 = self.entry.get()
        self.entry.delete(first=0,last=100)
    def bent(self):
        try:
            if self.op == 0:
                self.v2 = self.entry.get()
                r = float(self.v2) + float(self.v1)
                r = str(r)
                self.entry.delete(first=0,last=100)
                self.entry.insert(END,r)
            elif self.op == 1:
                self.v2 = self.entry.get()
                r = float(self.v2) - float(self.v1)
                r = str(r)
                self.entry.delete(first=0,last=100)
                self.entry.insert(END,r)
            elif self.op == 2:
                self.v2 = self.entry.get()
                r = float(self.v2) * float(self.v1)
                r = str(r)
                self.entry.delete(first=0,last=100)
                self.entry.insert(END,r)
            elif self.op == 3:
                self.v2 = self.entry.get()
                r = float(self.v1) / float(self.v2)
                r = str(r)
                self.entry.delete(first=0,last=100)
                self.entry.insert(END,r)
            elif self.op == 4:
                self.v2 = self.entry.get()
                r = float(self.v1) % float(self.v2)
                r = str(r)
                self.entry.delete(first=0,last=100)
                self.entry.insert(END,r)
        except Exception as error:
            self.entry.delete(first=0,last=100)

object_tk = Tk()
CalcPy(object_tk)
object_tk.mainloop()
