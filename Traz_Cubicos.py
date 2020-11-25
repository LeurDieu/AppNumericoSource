from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from MasterT import TCubic
from ExpEval import parseMatrix
from ExpEval import parseArray
from ExpEval import graphTrazador

from Matrix import Matrix
class T_CU(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaX  = StringVar()
        self.entradaY  = StringVar()
        self.varia=tk.StringVar(self)

        self.t = tk.Text(self)

        label = tk.Label(self, text="TRAZADORES CUBICOS", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        Listv=['Ingrese tamaño del Array','2','3','4','5','6','7']
        self.varia.set(Listv[0])

        opt=tk.OptionMenu(self, self.varia, *Listv)
        opt.config(width=40, font=('Helvetica', 10))
        opt.place(x=20,y=20)

        #X:
        label =tk.Label(self,text="Valores de X : ",fg="gray25", font=("Comic Seans MS",15),width="15",height="2")
        label.place(x=50,y=60)
        fdx=tk.Entry(self, textvariable=self.entradaX,width=50)
        fdx.place(x=50,y=110)

        #Y:
        label =tk.Label(self,text="Valores de Y : ",fg="gray25", font=("Comic Seans MS",15),width="15",height="2")
        label.place(x=550, y=60)
        Xcero=tk.Entry(self, textvariable=self.entradaY,width=50)
        Xcero.place(x=550,y=110)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=1100,y=90)

        button2 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("PageThree"),width="30",height="2",bg="#F50743",fg="gray25")

        button2.place(x=1100,y=40)

        button3 = tk.Button(self, text="REINICIAR",
                            command=self.borrarText,width="30",height="2",bg="gray25",fg="cyan2")

        button3.place(x=1100,y=140)
        button4 = tk.Button(self, text="GRAFICAR",
                            command=self.graficar,width="30",height="2",bg="gray25",fg="cyan2")

        button4.place(x=1100,y=190)
    
    def calcular(self):
        var1=str(self.entradaX.get())
        var2=str(self.entradaY.get()) 
        var3=int(self.varia.get())

        _X = parseArray(var1, var3)
        _Y = parseArray(var2, var3)

        _egpt= TCubic(_X,_Y)
        _egpt.solve()
        self.t.pack(side=tk.BOTTOM,padx=50, pady=40, expand= True,fill=tk.BOTH)
        self.t.insert(END,_egpt.content + '\n')
    
    def borrarText(self):
        self.t.delete('1.0', END)

    def graficar(self):
        var1=str(self.entradaX.get())
        var2=str(self.entradaY.get()) 
        var3=int(self.varia.get())
        _X = parseArray(var1, var3)
        _Y = parseArray(var2, var3)
        graphTrazador(_X,_Y,3)