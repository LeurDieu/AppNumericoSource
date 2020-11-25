from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from MasterA import Sor
from ExpEval import parseMatrix
from ExpEval import parseArray
from Matrix import Matrix

class SO(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaA  = StringVar()
        self.entradaB  = StringVar()
        self.entradaX  = StringVar()
        self.entradaT  = StringVar()
        self.entradaN  = StringVar()
        self.entradaW  = StringVar()
        self.varia=tk.StringVar(self)

        self.t = tk.Text(self)

        label = tk.Label(self, text="SOR", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
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
        label.place(x=30,y=50)
        fdx=tk.Entry(self, textvariable=self.entradaA)
        fdx.place(x=30,y=110)

        #B:
        label =tk.Label(self,text="b : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=200, y=50)
        at=tk.Entry(self, textvariable=self.entradaB)
        at.place(x=200,y=110)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=380,y=50)
        bt=tk.Entry(self, textvariable=self.entradaX)
        bt.place(x=380,y=110)

        #Tol:
        label =tk.Label(self,text="Tol : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=560, y=50)
        Xcero=tk.Entry(self, textvariable=self.entradaT)
        Xcero.place(x=560,y=110)

        #w:
        label =tk.Label(self,text="W : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=760,y=50)
        tt=tk.Entry(self, textvariable=self.entradaW)
        tt.place(x=760,y=110)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=960,y=50)
        nt=tk.Entry(self, textvariable=self.entradaN)
        nt.place(x=960,y=110)

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
        var5=float(self.entradaW.get())
        var6=float(self.entradaN.get())
        var7=int(self.varia.get())

        _A = parseMatrix(var1, var7)
        _B = parseArray(var2, var7)
        _X = parseArray(var3, var7)
        _matrix = Matrix(_A,_B, var7)
        _egpp= Sor(_matrix,_X,var5,var4,var6)

        self.t.pack(side=tk.BOTTOM,padx=50, pady=40, expand= True,fill=tk.BOTH)
        self.t.insert(END,_egpp.content + '\n')
    
    def borrarText(self):
        self.t.delete('1.0', END)