from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3

except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from MasterM import busqueda
from ExpEval import graph

class B_I(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaF  = StringVar()
        self.entradaX  = StringVar()
        self.entradaD  = StringVar()
        self.entradaN  = StringVar()

        self.t = tk.Text(self)

        self.f = None
        self.a = None
        self.b = None 

       


        label = tk.Label(self, text="BUSQUEDA INCREMENTAL", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        #FUNCION:
        label =tk.Label(self,text="f(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=60,y=50)
        fdx=tk.Entry(self, textvariable=self.entradaF)
        fdx.place(x=60,y=110)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=250, y=50)
        Xcero=tk.Entry(self, textvariable=self.entradaX)
        Xcero.place(x=250,y=110)

        #DX:
        label =tk.Label(self,text="DX : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=450,y=50)
        dx=tk.Entry(self, textvariable=self.entradaD)
        dx.place(x=450,y=110)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=650,y=50)
        Vn=tk.Entry(self, textvariable=self.entradaN)
        Vn.place(x=650,y=110)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=1100,y=90)

        button2 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("PageOne"),width="30",height="2",bg="#F50743",fg="gray25")

        button2.place(x=1100,y=40)

        button3 = tk.Button(self, text="REINICIAR",
                            command=self.borrarText,width="30",height="2",bg="gray25",fg="cyan2")

        button3.place(x=1100,y=140)

        button4 = tk.Button(self, text="GRAFICAR",
                            command=self.graficar,width="30",height="2",bg="gray25",fg="cyan2")

        button4.place(x=1100,y=190)
        

    def calcular(self):
        self.f =str(self.entradaF.get())
        self.a =float(self.entradaX.get())
        var3=float(self.entradaD.get())
        var4=int(self.entradaN.get())
        self.s=busqueda(self.f,self.a,var3,var4)

        self.t.pack(side=tk.BOTTOM,padx=50, pady=40, expand= True,fill=tk.BOTH)
        self.t.insert(END,self.s.content + '\n\n')
        self.t.pack()
        self.b = round((var3 * var4) + 1 )

    def borrarText(self):
        self.t.delete('1.0', END)

    def graficar(self):

        graph(self.a,self.b,self.f)