from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from ExpEval import parseMatrix
from ExpEval import parseArray
from MasterA import EGS
from Matrix import Matrix

class G_S(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.varia=tk.StringVar(self)
        self.entradaF  = StringVar()
        self.entradaX  = StringVar()

        self.t = tk.Text(self)

        label = tk.Label(self, text="GAUSS SIMPLE", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        Listv=['Ingrese tamaño de la matriz','2','3','4','5','6','7']
        self.varia.set(Listv[0])

        opt=tk.OptionMenu(self, self.varia, *Listv)
        opt.config(width=40, font=('Helvetica', 10))
        opt.place(x=20,y=40)

        #A:
        label =tk.Label(self,text="A : ",fg="gray25", font=("Comic Seans MS",20),width="10",height="2")
        label.place(x=80,y=150)
        fdx=tk.Entry(self, textvariable=self.entradaF,width=50)
        fdx.place(x=20,y=280)

        #b:
        label =tk.Label(self,text="b : ",fg="gray25", font=("Comic Seans MS",20),width="10",height="2")
        label.place(x=80, y=380)
        Xcero=tk.Entry(self, textvariable=self.entradaX,width=50)
        Xcero.place(x=20,y=510)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=50,y=560)

        button2 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("PageTwo"),width="30",height="2",bg="#F50743",fg="gray25")

        button2.place(x=1100,y=40)

        button3 = tk.Button(self, text="REINICIAR",
                            command=self.borrarText,width="30",height="2",bg="gray25",fg="cyan2")

        button3.place(x=1100,y=140)

    def calcular(self):
        var1=str(self.entradaF.get())
        var2=str(self.entradaX.get()) 
        var3=int(self.varia.get())

        _A = parseMatrix(var1, var3)
        _B = parseArray(var2, var3)
        _matrix = Matrix(_A,_B, var3)
        _egs = EGS(_matrix)
        

        self.t.pack(side=tk.BOTTOM,padx=400, pady=20, expand= True,fill=tk.BOTH)
        self.t.insert(END,_egs.content + '\n')
        #print(_egs.content)

    def borrarText(self):
        self.t.delete('1.0', END)






