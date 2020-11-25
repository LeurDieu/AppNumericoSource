from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from MasterM import rmultiples
from ExpEval import graphP
class R_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaF  = StringVar()
        self.entradaF1  = StringVar()
        self.entradaF2 = StringVar()
        self.entradaX = StringVar()
        self.entradaT  = StringVar()
        self.entradaN  = StringVar()

        self.t = tk.Text(self)

        self.f = None
        self.a = None
        self.b = None  
        self.s = None    

        label = tk.Label(self, text="RAICES MULTIPLES", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        #FUNCION:
        label =tk.Label(self,text="f(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=30,y=50)
        fdx=tk.Entry(self, textvariable=self.entradaF)
        fdx.place(x=30,y=110)

        #FUNCION':
        label =tk.Label(self,text="f'(x)  : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=200, y=50)
        at=tk.Entry(self, textvariable=self.entradaF1)
        at.place(x=200,y=110)

        #FUNCION'':
        label =tk.Label(self,text="f''(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=380,y=50)
        bt=tk.Entry(self, textvariable=self.entradaF2)
        bt.place(x=380,y=110)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=560, y=50)
        Xcero=tk.Entry(self, textvariable=self.entradaX)
        Xcero.place(x=560,y=110)

        #Tol:
        label =tk.Label(self,text="Tol : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=760,y=50)
        tt=tk.Entry(self, textvariable=self.entradaT)
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
                            command=lambda: controller.show_frame("PageOne"),width="30",height="2",bg="#F50743",fg="gray25")

        button2.place(x=1100,y=40)

        button3 = tk.Button(self, text="REINICIAR",
                            command=self.borrarText,width="30",height="2",bg="gray25",fg="cyan2")

        button3.place(x=1100,y=140)

        button4 = tk.Button(self, text="GRAFICAR",
                            command=self.graficar,width="30",height="2",bg="gray25",fg="cyan2")

        button4.place(x=1100,y=190)

    def calcular(self):
        self.f=str(self.entradaF.get())
        var2=str(self.entradaF1.get())
        var3=str(self.entradaF2.get())
        var4=float(self.entradaX.get())
        var5=float(self.entradaT.get())
        var6=float(self.entradaN.get())
        
        self.s=rmultiples(self.f,var2,var3,var4,var5,var6)
        self.t.pack(side=tk.BOTTOM,padx=50, pady=40, expand= True,fill=tk.BOTH)
        self.t.insert(END,self.s.content + '\n\n')
        self.t.pack()

        if( self.s.solution > 0 ):
            self.a = 0
            self.b = round(self.s.solution + 1)
        else :
            self.a = round(self.s.solution - 1)
            self.b = 0

    def borrarText(self):
        self.t.delete('1.0', END)

    def graficar(self):
        graphP(self.a,self.b,self.f,self.s.solution)

      