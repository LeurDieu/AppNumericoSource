try:
    import tkinter as tk 
    from tkinter import font as tkfont 
except ImportError:
    import Tkinter as tk
    import tkFont as tkfont 

#Metodos Numericos
from Busq_incre import B_I
from Biseccion import BIS
from Newton import NEW
from Punto_Fijo import P_F
from Raices_mult import R_M
from Regla_falsa import R_F
from Secante import SEC
#Metodos matriciales
from Gauss_Simple import G_S
from Gauss_P_Parcial import G_P_P
from Gauss_P_Total import G_P_T
from LU_Gauss_Simple import LU_G_S
from LU_P_Parcial import LU_P_P
from Crout import CRO
from Doolittle import DOO
from Cholesky import CHO
from Gauss_Seidel import G_SE
from Jacobi import JA
from Sor import SO
from Vandermonde import VA
from Newton_M import N_M
from Lagrange import LA
from Traz_Lineales import T_L
from Traz_Cuadraticos import T_C
from Traz_Cubicos import T_CU

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree, B_I, BIS , NEW , P_F, R_M, R_F,SEC, G_S, G_P_P, G_P_T,LU_G_S,LU_P_P,CRO,DOO,CHO,G_SE,JA,SO,VA,N_M,LA,T_L,T_C,T_CU):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="PROYECTO FINAL 2020-2", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="5")
        label.pack()

        label =tk.Label(self,text="*En esta herramienta va a encontrar tres opciones para resolver sistemas de ecuaciones,",fg="gray25", font=("Comic Seans MS",15),width="80",height="2",bg="light sea green")
        label.pack()

        label =tk.Label(self,text="puede ser por medio de metodos numericos, por medio de metodos matriciales o por trazadores:*",fg="gray25", font=("Comic Seans MS",15),width="80",height="2",bg="light sea green")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="5")
        label.pack()

        button1 = tk.Button(self, text="METODOS NUMERICOS",
                            command=lambda: controller.show_frame("PageOne"),width="100",height="5",bg="gray25",fg="cyan2",activebackground="#F50743")

        button2 = tk.Button(self, text="METODOS MATRICIALES",
                            command=lambda: controller.show_frame("PageTwo"),width="100",height="5",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button3 = tk.Button(self, text="METODOS INTERPOLACION",
                            command=lambda: controller.show_frame("PageThree"),width="100",height="5",bg="gray25",fg="cyan2",activebackground="#F50743")
        button1.pack()
        button2.pack()
        button3.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="METODOS NUMERICOS", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        button1 = tk.Button(self, text="Busquedas incrementales",
                            command=lambda: controller.show_frame("B_I"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button2 = tk.Button(self, text="Newton",
                            command=lambda: controller.show_frame("NEW"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button3 = tk.Button(self, text="Biseccion",
                            command=lambda: controller.show_frame("BIS"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button4 = tk.Button(self, text="Regla Falsa",
                            command=lambda: controller.show_frame("R_F"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button5 = tk.Button(self, text="Punto Fijo",
                            command=lambda: controller.show_frame("P_F"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button6 = tk.Button(self, text="Secante",
                            command=lambda: controller.show_frame("SEC"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button7 = tk.Button(self, text="Raices Multiples",
                            command=lambda: controller.show_frame("R_M"),width="100",height="4",bg="gray25",fg="cyan2",activebackground="#F50743")

        button8 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("StartPage"),width="30",height="2",bg="cyan2",fg="gray25",activebackground="#F50743")
        

        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="METODOS MATRICIALES", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        button1 = tk.Button(self, text="Gauss Simple",
                            command=lambda: controller.show_frame("G_S"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button2 = tk.Button(self, text="Gauss Pivoteo Parcial",
                            command=lambda: controller.show_frame("G_P_P"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button3 = tk.Button(self, text="Gauss Pivoteo Total",
                            command=lambda: controller.show_frame("G_P_T"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button4 = tk.Button(self, text="LU Gauss Simple",
                            command=lambda: controller.show_frame("LU_G_S"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button5 = tk.Button(self, text="LU Pivoteo Parcial",
                            command=lambda: controller.show_frame("LU_P_P"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button6 = tk.Button(self, text="Crout",
                            command=lambda: controller.show_frame("CRO"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button7 = tk.Button(self, text="Doolittle",
                            command=lambda: controller.show_frame("DOO"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button8 = tk.Button(self, text="Cholesky",
                            command=lambda: controller.show_frame("CHO"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button9 = tk.Button(self, text="Gauss Seidel",
                            command=lambda: controller.show_frame("G_SE"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button10 = tk.Button(self, text="Jacobi",
                            command=lambda: controller.show_frame("JA"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button11 = tk.Button(self, text="Sor",
                            command=lambda: controller.show_frame("SO"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button18 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("StartPage"),width="30",height="2",bg="cyan2",fg="gray25",activebackground="#F50743")
        #button18.place(x=200,y=950)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()
        button8.pack()
        button9.pack()
        button10.pack()
        button11.pack()
        button18.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="METODOS INTERPOLACION", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        button12 = tk.Button(self, text="Vandermonde",
                            command=lambda: controller.show_frame("VA"),width="100",height="2",bg="gray25",fg="cyan2")

        button13 = tk.Button(self, text="Newton",
                            command=lambda: controller.show_frame("N_M"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button14 = tk.Button(self, text="Lagrange",
                            command=lambda: controller.show_frame("LA"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button15 = tk.Button(self, text="Trazadores Lineales",
                            command=lambda: controller.show_frame("T_L"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button16 = tk.Button(self, text="Trazadores Cuadraticos",
                            command=lambda: controller.show_frame("T_C"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")

        button17 = tk.Button(self, text="Trazadores Cubicos",
                            command=lambda: controller.show_frame("T_CU"),width="100",height="2",bg="gray25",fg="cyan2",activebackground="#F50743")
        
        button18 = tk.Button(self, text="VOLVER",
                            command=lambda: controller.show_frame("StartPage"),width="30",height="2",bg="cyan2",fg="gray25",activebackground="#F50743")
        
        button12.pack()
        button13.pack()
        button14.pack()
        button15.pack()
        button16.pack()
        button17.pack()
        button18.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()