from ExpEval import expEval
from ExpEval import graph
from ExpEval import graphP
import pandas as pd
pd.set_option("precision",10)

class busqueda():
    def __init__(self,f,x0,dx,n):
        self.content = None
        
        self.solve(f,x0,dx,n)

    def solve(self,f,x0,dx,n):
        xant=x0
        xact=xant+dx
        fant=expEval(f,xant)
        fact=expEval(f,xact)
        cont=1
        resul=""
        while cont<n:
            xant=xact
            xact=xant+dx
            fant=expEval(f,xant)
            fact=expEval(f,xact)
            
            if fant*fact<0:
                resul = resul + (str("Hay una raiz de f en: [" +str(xant)+" , "+str(xact)+" ]\n"))
                #print("Hay una raiz de f en: ","[ ",xant," , ",xact," ]")
            cont+=1
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + resul

class bisec():
    def __init__(self,f,a,b,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,a,b,tol,n)

    def solve(self,f,a,b,tol,n):
        
        cont = 1
        error=-1
        resul=[]
        while cont<n:
            if (error < tol and error != -1):
                break
            p1=(a+b)/2
            fa=expEval(f,a)
            fp1=expEval(f,p1)
            raiz=0
            if fp1==0:
                p1=raiz
                break
            elif fa*fp1<0:
                b=p1
            else:
                a=p1
            raiz=p1
            error=abs(fp1)
            resul.append([cont, a, p1, b, fp1, error])
            self.solution = p1
            cont += 1

        enc=["iter" ,"a" , "Xm"," b" , "f(Xm) ", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + output.to_string(index=False)
        
    
class falsaposicion():
    def __init__(self,f,a,b,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,a,b,tol,n)

    def solve(self,f,a,b,tol,n):
        error=10
        cont = 1
        raiz=0
        resul=[]
        while error>tol:
            fa=expEval(f,a)
            fb=expEval(f,b)
            p=b-((fb*(b-a))/(fb-fa))
            fp=expEval(f,p)
            if fp==0:
                p=raiz
                break
            elif fa*fp<0:
                b=p
            else:
                a=p
            raiz=p
            error=abs(fp)
            resul.append ([cont,a , p, b , fp , error])
            self.solution = p
            #print(cont,"    |",a," | ",p," | ",b," | ",fp," | ",error)
            cont += 1

        enc=["iter" ,"a" , "p"," b" , "f(p) ", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + output.to_string(index=False)

class newton():
    def __init__(self,f,fp,p0,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,fp,p0,tol,n)

    def solve(self,f,fp,p0,tol,n):
        error=10
        resul=[]
        nx=0
        resul.append([nx, p0, expEval(f,p0), ""])
        #print("|",n,"      ||   ",p0,"                      ||",f(p0),"    ||                        |")
        while error>tol and nx<n:
            a=expEval(f,p0)
            b=expEval(fp,p0)
            p=p0-(a/b)
            error=abs(p-p0)
            p0=p
            nx=nx+1
            self.solution = p
            resul.append([nx, p, a, error])    
            #print("|",n,"      ||   ",p,"       ||",a,"    ||  ",error,"|")
        enc=["iter", "p", " a", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + output.to_string(index=False)

class puntofijo():
    def __init__(self,f,g,p0,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,g,p0,tol,n)

    def solve(self,f,g,p0,tol,n):
        error=100
        p=expEval(g,p0)
        p1=expEval(f,p0)
        resul=[]
        p0=p
        nx=0
        while error>=tol and nx<n:
        
            p=expEval(g,p0)
            p1=expEval(f,p0)
            error=abs(p-p0)
            nx=nx+1
            self.solution = p
            resul.append ([nx,p0,p,p1,error])
            #print("|",n,"         |""|   ",p0,"||",p,"||",p1,"||",error,"|")
            p0=p
        enc=["iter", "xi", " g(xi)","f(xi)", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f 
        self.content = self.content + "\nf(g) = " + g +"\n\n"
        self.content = self.content + output.to_string(index=False)

class secant():
    def __init__(self,f,p0,p1,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,p0,p1,tol,n)

    def solve(self,f,p0,p1,tol,n):
        resul=[]
        nx=0
        resul.append([nx, p0, expEval(f,p0), ""])
        error=10
        nx+=1
        resul.append([nx, p1, expEval(f,p1), ""])
        fp0=expEval(f,p0)
        fp1=expEval(f,p1)
        #print("|",n,"      | "                  ,p0,"                        |"   ,fp0,   "    |                       |")
        #nx=nx+1
        #print("|",n,"      | "                  ,p1,"                          |"   ,fp1,   "    |                       |")
        while error>tol and nx<n :
            fp0=expEval(f,p0)
            fp1=expEval(f,p1)
            p=p1-(((fp1)*(p1-p0))/((fp1-fp0)))
            p0=p1
            p1=p
            error=abs((p0-p1))
            aux=expEval(f,p)
            nx=nx+1
            self.solution = p
            resul.append([nx,p,aux,error])
            #resul.append(" | "+str(nx)+" | "+str(p)+"  |  " +str(aux)+"  |  "+str(error)+"     |")
        enc=["iter", "xi", "f(xi)", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + output.to_string(index=False)

class rmultiples():
    def __init__(self,f,fp,fpp,x0,tol,n):
        self.content = None
        self.solution = None

        self.solve(f,fp,fpp,x0,tol,n)

    def solve(self,f,fp,fpp,x0,tol,n):
        x=x0
        resul=[]
        f1=float(expEval(f,x))
        f2=float(expEval(fp,x))
        f3=float(expEval(fpp,x))
        p=x-((f1*f2)/((f2**2)-(f1*f3)))
        error=1
        g2=0
        cont=0
        while error>tol and cont<n:
            x=p
            f1=expEval(f,x)
            f2=expEval(fp,x)
            f3=expEval(fpp,x)
            g2=p
            p=g2-((f1*f2)/((f2**2)-(f1*f3)))
            error=abs(p-g2)
            cont+=1
            #print(cont,p,f1,error)
            self.solution = p
            resul.append([cont,p,f1,error])
            #resul.append(" | "+str(cont)+" | "+str(p)+" | "+str(f1)+" | "+str(error)+" | ")
        enc=["iter", "xi", "f(xi)", "E"]
        output = pd.DataFrame(resul,columns= enc)
        
        self.content = "\n\nf(x) = " + f +"\n\n"
        self.content = self.content + output.to_string(index=False)
