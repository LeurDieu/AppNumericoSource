import numpy as np
import io
#from ExpEval import handleError
class Vandermonde():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None
        self.solution=None

    def solve(self):

        _n = len(self.X)
        _A = np.zeros([_n,_n])
    
        for _i in range(_n):
            _A[:,_i] = np.conjugate(np.power(self.X,(_n - _i-1 )))
        
        _res = np.linalg.solve(_A,np.transpose(self.Y))

        _exp = _n - 1
        _pol = ""
        for _coe in _res:
            _pol = _pol + str(_coe) + "x^"+str(_exp) + " + "
            _exp -= 1
        _pol = _pol[:-2]
        
        print ("\nMatriz de Vandermonde:\n",_A, file = self.output)
        print ("\nCoeficientes del polinomio:\n",_res, file = self.output)
        print ("\nPolinomio:\n",_pol, file = self.output)

        self.content = self.output.getvalue()
        a=_res
        self.output.close()
        return a


class DifDiv():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None
    

    def solve(self):
        _n = len(self.X) 
        _D = np.zeros([_n, _n])
    
        
        _D[:,0] = np.conjugate(self.Y)

        for _i in range (1,_n):
            _aux0 = _D[_i-1:_n, _i-1]
            _aux1 = np.diff(_aux0)
            _aux2 = np.subtract(self.X[_i:_n],self.X[0:_n-1-_i+1])
            _D[_i:_n,_i] = np.divide(_aux1,np.transpose(_aux2))

        _res = np.diag(_D)
    
        print ("\nTabla de diferencias divididas:\n",_D, file = self.output)        
        print ("\nCoeficientes del polinomio de Newton:\n",_res, file = self.output) 
        print ("\nPolinomio:\n", file = self.output)
        
        _pol=""
        b=""
        cont=0
        for f in _res:
            n=str(self.X[cont])
            _pol=_pol+" + ("+str(f)+")"+b
            b=b+"*(x - ("+n+"))"        
            cont+=1
        print(_pol[2:], file = self.output)
        a=_pol[2:]
        self.content = self.output.getvalue()
        self.output.close()
        return a

class Lagrange():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None


    def solve(self):
        _n = len(self.X)
        _L = np.zeros([_n,_n])
    
        for _i in range(0, _n):
            _aux0 = np.setdiff1d(self.X, self.X[_i])
            _aux1 = [1, (_aux0[0]*-1)]
            
            for _j in range(1,_n-1):
                _aux1 = np.convolve(_aux1, [1, (_aux0[_j]*-1)])

            _L[_i,:] = (_aux1)/(np.polyval(_aux1,self.X[_i]))
            
        _pols = []
        

        for _poli in _L:
            _exp = _n - 1
            _pol = ""
            for _val in _poli:
                _pol = _pol + str(_val) + "*x^" + str(_exp) + " + "
                _exp -= 1
            _pol = _pol[:-2]
            _pols.append(_pol)
                

        


        print ("\nPolinomios interpolantes de Lagrange:\n", file = self.output)
        _cont=0
        for _x in _pols:
            print(_x,"  //L",_cont, file = self.output)
            _cont+=1

        print("\nPolinomio\n", file = self.output)

        cont=0
        _polinom=""
        for f in self.Y:
            _f=str(f)
            n=_f+"*L"+str(cont)+"+"
            _polinom=_polinom+n
            cont+=1
        print(_polinom[:len(_polinom)-1], file = self.output)

        print("\nPolinomio extendido:\n", file = self.output)
        
        polext=""
        conta=0
        for v in self.Y:
            m=str(_pols[conta])
            n=str(v)
            z=" + "+n+"*("+m+")"
            polext=polext+z
            conta+=1
        print(polext[3:], file = self.output)

        self.content = self.output.getvalue()
        self.output.close()
        a=polext[3:]
        return a



class TLineal():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None


    def solve(self):
        _n = len(self.X)
        _m = 2 * (_n - 1)
        _A = np.zeros([_m, _m])
        _B = np.zeros(_m).reshape(_m, 1)
        _coef = np.zeros([_n-1, 2])


        for _i in range(0, len(self.X)-1):
            _A[(_i+1), [2*_i, 2*_i + 1]] = [self.X[_i+1], 1]
            _B[(_i+1)] = self.Y[_i+1]
  
        _A[0, [0, 1]] = [self.X[0], 1]
        _B[0] = self.Y[0]
        for _i in range(1, len(self.X)-1):
            _A[len(self.X)-1 + _i, 2*_i-2:2*_i+2] = [self.X[_i], 1, (self.X[_i]*-1), -1]
            _B[len(self.X)-1 + _i] = 0
        
        _res = np.linalg.solve(_A,_B)

        for _i in range(0,len(self.X)-1):
            _coef[_i,:] = _res[[2*_i, 2*_i+1]].reshape(1,2)

        print ("\nCoeficientes de los trazadores:\n", file = self.output)
        for _co in _coef:
            print(_co[0],' ',_co[1], file = self.output)
        print ("\nTrazadores:\n", file = self.output)
        a=[]
        for _tra in _coef:
            b=str(_tra[0])+'*x + '+str(_tra[1])
            print(b, file=self.output)
            a.append(b)

        self.content = self.output.getvalue()
        self.output.close()
        return a


class TCuad():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None

     

    def solve(self):
        _n = len(self.X)
        _m = 3 * (_n - 1)
        _A = np.zeros([_m, _m])
        _B = np.zeros(_m).reshape(_m, 1)
        _coef = np.zeros([_n-1, 3])


        for _i in range(0, _n-1):
            _A[(_i+1), 3*(_i+1)-3:3*(_i+1)] = [self.X[_i+1]**2, self.X[_i+1], 1]
            _B[(_i+1)] = self.Y[_i+1]

        _A[0, 0:3] = [self.X[0]**2, self.X[0], 1]
        _B[0] = self.Y[0]
        
        for _i in range(1, len(self.X)-1):
            _A[_n-1 + _i, 3*(_i+1)-6:3*(_i+1)] = [self.X[_i]**2,self.X[_i], 1,(self.X[_i]**2)*-1, (self.X[_i]*-1), -1]
            _B[_n-1 + _i] = 0

        for _i in range(1, len(self.X)-1):
            _A[2*_n-4+(_i+1),3*(_i+1)-6:3*(_i+1)] = [2*self.X[_i], 1 , 0 , -2*self.X[_i], -1, 0]
            _B[2*_n-3+(_i+1)] = 0

        _A[_m-1,0] = 2
        _B[_m-1] = 0

        
        
        _res = np.linalg.solve(_A,_B)
  

        for _i in range(0,len(self.X)-1):
            _coef[_i,:] = _res[3*(_i+1) - 3: 3*(_i+1)].reshape(1,3)

        print ("\nCoeficientes de los trazadores:\n", file = self.output)
        for _co in _coef:
            print(_co[0],' ',_co[1],' ',_co[2], file = self.output)
        print ("\nTrazadores:\n", file = self.output)
        
        a=[]
        for _tra in _coef:
            b=str(_tra[0])+'*x^2 + '+ str(_tra[1])+ '*x + '+str(_tra[2])
            print(str(b),file=self.output)
            a.append(b)
        self.content = self.output.getvalue()
        self.output.close()
        return a

class TCubic():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y
        self.output = io.StringIO()
        self.content = None



    def solve(self):
        _n = len(self.X)
        _m = 4 * (_n - 1)
        _A = np.zeros([_m, _m])
        _B = np.zeros(_m).reshape(_m, 1)
        _coef = np.zeros([_n-1, 4])

        #Condiciones de interpolacion
        for _i in range(0,_n-1):
            _A[(_i+1), 4*(_i+1)-4:4*(_i+1)] = [self.X[_i+1]**3, self.X[_i+1]**2, self.X[_i+1], 1]
            _B[(_i+1)] = self.Y[_i+1]

        _A[0,0:4] = [self.X[0]**3, self.X[0]**2, self.X[0], 1]
        _B[0] = self.Y[0]

        #Condiciones  de continuidad 
        for _i in range(1,_n-1):
            _A[_n-1 + _i, 4*(_i+1)-8: 4*(_i+1)] = [self.X[_i]**3, self.X[_i]**2, self.X[_i], 1, (self.X[_i]**3)*-1, (self.X[_i]**2)*-1, (self.X[_i])*-1, -1]
            _B[_n-1 + _i] = 0

        #Condiciones de suavidad
        for _i in range(1,_n-1):
            _A[2*_n-3+_i, 4*(_i+1)-8: 4*(_i+1)] = [3*self.X[_i]**2, 2*self.X[_i], 1, 0, -3*self.X[_i]**2, -2*self.X[_i], -1, 0]
            _B[2*_n-3+_i] = 0

        #Condiciones de concavidad
        for _i in range(1,_n-1):
            _A[3*_n-5+_i, 4*(_i+1)-8: 4*(_i+1)] = [6*self.X[_i], 2, 0, 0, -6*self.X[_i], -2, 0, 0]
            _B[_n+5+_i] = 0
        
        #Condiciones frontera
        _A[_m-2,0:2] = [6*self.X[0], 2]
        _B[_m-2] = 0
        _A[_m-1, _m-4:_m-2] = [6*self.X[_n-1], 2]
        _B[_m-1] = 0

        #
        _res = np.linalg.solve(_A,_B)

        for _i in range(0,len(self.X)-1):
            _coef[_i,:] = _res[4*(_i+1) - 4: 4*(_i+1)].reshape(1,4)
        
        print ("\nCoeficientes de los trazadores:\n", file = self.output)
        for _co in _coef:
            print(_co[0],' ',_co[1],' ',_co[2],' ',_co[3], file = self.output)

        print ("\nTrazadores:\n", file = self.output)   
        a=[]
        for _tra in _coef:
            b=str(_tra[0])+'*x^3 + '+ str(_tra[1])+'*x^2 + '+str(_tra[2])+ '*x + '+str(_tra[3])
            print(b, file=self.output)
            a.append(b)
        self.content = self.output.getvalue()
        self.output.close()
        return a