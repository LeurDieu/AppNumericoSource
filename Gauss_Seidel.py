from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from MasterA import GSeidel
from ExpEval import parseMatrix
from ExpEval import parseArray
from Matrix import Matrix

class G_SE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaA  = StringVar()
        self.entradaB  = StringVar()
        self.entradaX  = StringVar()
        self.entradaT  = StringVar()
        self.entradaN  = StringVar()
        self.varia=tk.StringVar(self)

        self.t = tk.Text(self)

        label = tk.Label(self, text="GAUSS SEIDEL", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        Listv=['Ingrese tamaño de la matriz','2','3','4','5','6','7']
        self.varia.set(Listv[0])

        opt=tk.OptionMenu(self, self.varia, *Listv)
        opt.config(width=40, font=('Helvetica', 10))
        opt.place(x=20,y=20)

        #A:
        label =tk.Label(self,text="A : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=60,y=50)
        fdx=tk.Entry(self, textvariable=self.entradaA)
        fdx.place(x=60,y=110)

        #b:
        label =tk.Label(self,text="b : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=250, y=50)
        at=tk.Entry(self, textvariable=self.entradaB)
        at.place(x=250,y=110)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=450,y=50)
        bt=tk.Entry(self, textvariable=self.entradaX)
        bt.place(x=450,y=110)

        #Tol:
        label =tk.Label(self,text="Tol : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=650,y=50)
        tt=tk.Entry(self, textvariable=self.entradaT)
        tt.place(x=650,y=110)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=850,y=50)
        nt=tk.Entry(self, textvariable=self.entradaN)
        nt.place(x=850,y=110)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=1100,y=90)

        button2 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("PageTwo"),width="30",height="2",bg="#F50743",fg="gray25")

        button2.place(x=1100,y=40)

        button3 = tk.Button(self, text="REINICIAR",
                            command=self.borrarText,width="30",height="2",bg="gray25",fg="cyan2")

        button3.place(x=1100,y=140)

    def calcular(self):

        var1=str(self.entradaA.get())
        var2=str(self.entradaB.get())
        var3=str(self.entradaX.get())
        var4=float(self.entradaT.get())
        var5=int(self.entradaN.get())
        var6=int(self.varia.get())

        _A = parseMatrix(var1, var6)
        _B = parseArray(var2, var6)
        _X = parseArray(var3, var6)
        _matrix = Matrix(_A,_B, var6)
        _egpp= GSeidel(_matrix,_X,var4,var5)

        self.t.pack(side=tk.BOTTOM,padx=50, pady=40, expand= True,fill=tk.BOTH)
        self.t.insert(END,_egpp.content + '\n')

    def borrarText(self):
        self.t.delete('1.0', END)