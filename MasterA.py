from Matrix import Matrix
import numpy as np
import copy
import cmath
import io
import pandas as pd
pd.set_option("precision",10)

class EGS():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()
        

    def solve(self):
        self.checkIfFirstZero()
        
        _i = 0
        _j = 1
        self.output = self.matrix.showMatrix(self.matrix.ext,self.output)
        for _i in range(self.matrix.size - 1):
            _j = _i + 1
            while (_j <= self.matrix.size - 1):
                if (self.matrix.ext[_j][_i] != 0):
                    _s = self.matrix.ext[_j][_i] / self.matrix.ext[_i][_i]
                    self.matrix.susRows(_i, _j , _s)
                _j += 1
            print("\nStage #",_i + 1, file=self.output)
            self.output = self.matrix.showMatrix(self.matrix.ext,self.output)

        self.output = self.matrix.solveMatrix(self.output)
        self.content = self.output.getvalue()
        self.output.close()

    def checkIfFirstZero(self):

        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class EGPP():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.content = self.matrix.showMatrix(self.matrix.ext,self.output)
        _i = 0
        _j = 1
        for _i in range(self.matrix.size - 1):
            
            _index = _i + 1
            
            while (_index < self.matrix.size):
                if (self.matrix.ext[_i][_i] < self.matrix.ext[_index][_i]):
                    self.matrix.switchRows(_i, _index)
                _index += 1

            _j = _i + 1
            while (_j <= self.matrix.size - 1):
                if (self.matrix.ext[_j][_i] != 0):
                    _s = self.matrix.ext[_j][_i] / self.matrix.ext[_i][_i]
                    self.matrix.susRows(_i, _j , _s)
                _j += 1
            print("\nStage #",_i + 1,file=self.content)
            self.content = self.matrix.showMatrix(self.matrix.ext,self.content)

        self.content = self.matrix.solveMatrix(self.content)
        self.content = self.output.getvalue()
        self.output.close()

class EGPT():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()
    
    def solve(self):
        self.output = self.matrix.showMatrix(self.matrix.ext,self.output)

        _i = 0
        _j = 1
        for _i in range(self.matrix.size - 1):
            _index = _i + 1

            while (_index < self.matrix.size):
                #print(self.matrix.ext[_i][_i] , ' - ', self.matrix.ext[_i][_index])
                if (self.matrix.ext[_i][_i] < self.matrix.ext[_i][_index]):
                    self.matrix.switchCols(_i, _index)
                _index += 1
            
            _index = _i + 1
            

            while (_index < self.matrix.size):
                #print(self.matrix.ext[_i][_i] , ' - ', self.matrix.ext[_index][_i])
                if (self.matrix.ext[_i][_i] < self.matrix.ext[_index][_i]):
                    self.matrix.switchRows(_i, _index)
                _index += 1

            

            _j = _i + 1
            while (_j <= self.matrix.size - 1):
                if (self.matrix.ext[_j][_i] != 0):
                    _s = self.matrix.ext[_j][_i] / self.matrix.ext[_i][_i]
                    self.matrix.susRows(_i, _j , _s)
                _j += 1
            print("\nStage #",_i + 1, file=self.output)
            self.output = self.matrix.showMatrix(self.matrix.ext,self.output)

        self.output = self.matrix.solveMatrix(self.output)
        self.content = self.output.getvalue()
        self.output.close()

class LUSM():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.checkIfFirstZero()    
        n=self.matrix.size
        L=np.eye(n)
        U=np.zeros([n,n])
        M=self.matrix.A
     
        for i in range(self.matrix.size -1):
            
            for j in range(i+1,self.matrix.size):
                if (M[j,i]!=0):
                    L[j,i]=M[j,i]/M[i,i]
                    M[j,i:n]=(M[j,i:n]-(M[j,i]/M[i,i])*(M[i,i:n]))          
            U[i,i:n]=M[i,i:n]
            U[i+1,i+1:n]=M[i+1,i+1:n]

            U[n-1,n-1]=M[n-1,n-1]
            print("\nStage #",i + 1,file=self.output)
            self.output = self.matrix.showMatrix(M,self.output)
            print("\nL: ", file = self.output)
            self.output = self.matrix.showMatrix(L,self.output)
            print("\nU: ", file = self.output)
            self.output = self.matrix.showMatrix(U,self.output)
        z=self.matrix.solvepro(L,self.matrix.B)
        self.output=self.matrix.solvereg(U,z,self.output)
        self.content = self.output.getvalue()
        self.output.close()
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class LUPP():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.checkIfFirstZero()   
        n=self.matrix.size
        L=np.eye(n)
        U=np.zeros([n,n])
        P=np.eye(n)
        M=self.matrix.A
     
        for i in range(self.matrix.size-1 ):
          

            aux0=max(abs(M[i+1:n,i]))
            aux=len(M[i+1:n,i])
       
            if (aux0>abs(M[i,i])):
                aux2=M[i+aux,i:n].copy()
                aux3=P[i+aux,:].copy()
                
                M[aux+i,i:n]=M[i,i:n]
                
                P[aux+i,0:n]=P[i,:]
                
                M[i,i:n]=aux2
                P[i,:]=aux3

                
                if i>0:
                    aux4=L[i+aux,1:i-1].copy()
                    L[i+aux,1:i-1]=L[i,1:i-1]
                    L[i,1:i-1]=aux4
            
            for j in range(i+1,self.matrix.size):
                if (M[j,i]!=0):
                    L[j,i]=M[j,i]/M[i,i]
                    M[j,i:n]=(M[j,i:n]-(M[j,i]/M[i,i])*(M[i,i:n]))          
            U[i,i:n]=M[i,i:n]
            U[i+1,i+1:n]=M[i+1,i+1:n]

            
            print("\nStage #",i + 1, file = self.output)
            self.output = self.matrix.showMatrix(M,self.output)
            print("\nL: " , file=self.output)
            self.output = self.matrix.showMatrix(L,self.output)
            print("\nU: " , file=self.output)
            self.output = self.matrix.showMatrix(U,self.output)
            print("\nP: " , file=self.output)
            self.output = self.matrix.showMatrix(P,self.output)
        U[n-1,n-1]=M[n-1,n-1]
        z=self.matrix.solvepro(L,np.dot(P,self.matrix.B))

        self.output =self.matrix.solvereg(U,z,self.output)
        self.content = self.output.getvalue()
        self.output.close()
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class CROUT():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.checkIfFirstZero()    
        n=self.matrix.size
        L=np.eye(n)
        U=np.eye(n)
        M=self.matrix.A
        print(n)
        for i in range(0,n):
            
            for j in range(i,n):
                L[j,i]=M[j,i]-np.dot(L[j,0:i],np.transpose(U[0:i,i]))

            for j in range(i+1,n):
                U[i,j]=(M[i,j]-np.dot(L[i,0:i],np.transpose(U[0:i,j])))/L[i,i]

            print("\nStage #",i + 1,file=self.output)

            print("\nL: ",file=self.output)
            self.output = self.matrix.showMatrix(L,self.output)
            print("\nU: ",file=self.output)
            self.output = self.matrix.showMatrix(U,self.output)

        L[n-1,n-1]=M[n-1,n-1]-np.dot(L[n-1,0:n-1],np.transpose(U[0:n-1,n-1]))

        z=self.matrix.solvepro(L,self.matrix.B)
        self.output=self.matrix.solvereg(U,z,self.output)
        self.content = self.output.getvalue()
        self.output.close()
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class DOOL():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.checkIfFirstZero()    
        n=self.matrix.size
        L=np.eye(n)
        U=np.eye(n)
        M=self.matrix.A
  
        for i in range(0,n):
            
            for j in range(i,n):
                U[i,j]=M[i,j]-np.dot(L[i,0:i],np.transpose(U[0:i,j]))

            for j in range(i+1,n):
                L[j,i]=(M[j,i]-np.dot(L[j,0:i],np.transpose(U[0:i,i])))/U[i,i]

            print("\nStage #",i + 1,file=self.output)

            print("\nL: ",file=self.output)
            self.output = self.matrix.showMatrix(L,self.output)
            print("\nU: ",file=self.output)
            self.output = self.matrix.showMatrix(U,self.output)

        U[n-1,n-1]=M[n-1,n-1]-np.dot(L[n-1,0:n-1],np.transpose(U[0:n-1,n-1]))

        z=self.matrix.solvepro(L,self.matrix.B)
        self.output = self.matrix.solvereg(U,z,self.output)
        self.content = self.output.getvalue()
        self.output.close()
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class CHOL():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        self.checkIfFirstZero()    
        n=self.matrix.size
        L=np.eye(n,dtype=np.complex)
        U=np.eye(n,dtype=np.complex)
        M=self.matrix.A

        for i in range(0,n):
            aux=(M[i,i]-np.dot(L[i,0:i],np.transpose(U[0:i,i])))
            f=float(aux)
            L[i,i]=cmath.sqrt(f)
        
            U[i,i]=L[i,i]
            for j in range(i+1,n):
               U[i,j]=(M[i,j]-np.dot(L[i,0:i],np.transpose(U[0:i,j])))/L[i,i]

            for j in range(i+1,n):
                L[j,i]=(M[j,i]-np.dot(L[j,0:i],np.transpose(U[0:i,i])))/U[i,i]

            print("\nStage #",i + 1,file=self.output)

            print("\nL: ",file=self.output)
            self.output = self.matrix.showMatrix(L,self.output)
            print("\nU: ",file=self.output)
            self.output = self.matrix.showMatrix(U,self.output)

        L[n-1,n-1]=cmath.sqrt(M[n-1,n-1]-np.dot(L[n-1,0:n-1],np.transpose(U[0:n-1,n-1])))
        U[n-1,n-1]=L[n-1,n-1]

        z=self.matrix.solvepro(L,self.matrix.B)
        self.output=self.matrix.solvereg(U,z,self.output)
        self.content = self.output.getvalue()
        self.output.close()
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

class GSeidel():
    def __init__(self, _matrix:Matrix, _x0, _tol, _nMax):
        self.matrix = _matrix
        self.x0 = _x0.reshape(len(_x0),1)
        self.tol = _tol
        self.nMax = _nMax

        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        _D = np.diag(np.diag(self.matrix.A))
        _L = (np.tril(self.matrix.A) * -1) + _D
        _U = (np.triu(self.matrix.A) * -1) + _D
        _T = np.linalg.inv(_D - _L).dot(_U)
        _C = np.linalg.inv(_D - _L).dot(self.matrix.B)
        [val,vec]=np.linalg.eig(_T)
        ro=max(abs(val))	
        
        if ro>=1:
            print("\nEl radio espectral > 1\n",file = self.output)

        print("\nT:\n", _T,file = self.output)
        print("\nC:\n", _C,file = self.output)
        print("\nradio espectral:\n",ro,file = self.output)

        _xant = self.x0
        _E = 1
        _i = 0
        resul=[]

        enc = ["Iter","E"]
        _xcont = 0
        for _val in _xant:
            enc.append("x" + str(_xcont))
            _xcont+=1
        #print("\n| Iter |    E     | ")

        while ((_E > self.tol) and (_i < self.nMax)):
            _xact = _T.dot(_xant) + _C
            _E = np.linalg.norm(_xant - _xact)
            _xant = _xact
            _i += 1
            _auxRes = [_i,_E]
            #_aux = _xant.reshape(1,self.matrix.size)
            #print(_aux)
            for _val in _xant.reshape(1,self.matrix.size)[0]:
                _auxRes.append(_val)
            resul.append(_auxRes)

        table = pd.DataFrame(resul,columns= enc)
        #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))
        
        print("\n",table.to_string(index=False), file = self.output)
        self.content = self.output.getvalue()
        self.output.close()

class Jacobi():
    def __init__(self, _matrix:Matrix, _x0, _tol, _nMax):
        self.matrix = _matrix
        self.x0 = _x0.reshape(len(_x0),1)
        self.tol = _tol
        self.nMax = _nMax

        self.output = io.StringIO()
        self.content = None
        self.solve()

    def solve(self):
        _D = np.diag(np.diag(self.matrix.A))
        _L = (np.tril(self.matrix.A) * -1) + _D
        _U = (np.triu(self.matrix.A) * -1) + _D
        _T = np.linalg.inv(_D).dot(_L + _U)
        _C = np.linalg.inv(_D).dot(self.matrix.B)
        [val,vec]=np.linalg.eig(_T)
        ro=max(abs(val))
        
        if ro>=1:
            print("\nEl radio espectral > 1\n",file = self.output)

        print("\nT:\n", _T,file = self.output)
        print("\nC:\n", _C,file = self.output)
        print("\nradio espectral:\n",ro,file = self.output)
        _xant = self.x0
        _E = 1
        _i = 0
        resul=[]
        enc = ["Iter","E"]
        _xcont = 0
        for _val in _xant:
            enc.append("x" + str(_xcont))
            _xcont+=1

        while ((_E > self.tol) and (_i < self.nMax)):
            _xact = _T.dot(_xant) + _C
            _E = np.linalg.norm(_xant - _xact)
            _xant = _xact
            _i += 1

            _auxRes = [_i,_E]
            #_aux = _xant.reshape(1,self.matrix.size)
            #print(_aux)
            for _val in _xant.reshape(1,self.matrix.size)[0]:
                _auxRes.append(_val)
            resul.append(_auxRes)
            #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))

        table = pd.DataFrame(resul,columns= enc)
        #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))
        
        print("\n",table.to_string(index=False), file = self.output)
        self.content = self.output.getvalue()
        self.output.close()

class Sor():
    def __init__(self, _matrix:Matrix, _x0, _w, _tol, _nMax):
        self.matrix = _matrix
        self.x0 = _x0.reshape(len(_x0),1)
        self.w = _w
        self.tol = _tol
        self.nMax = _nMax

        self.output = io.StringIO()
        self.content = None

        self.solve()

    def solve(self):
        _D = np.diag(np.diag(self.matrix.A))
        _L = (np.tril(self.matrix.A) * -1) + _D
        _U = (np.triu(self.matrix.A) * -1) + _D
        _T = np.linalg.inv(_D - (self.w * _L)).dot((1-self.w) * _D + (self.w * _U))
        _C = self.w * np.linalg.inv(_D - (self.w * _L)).dot(self.matrix.B)
        [val,vec]=np.linalg.eig(_T)
        ro=max(abs(val))

        if ro>=1:
            print("\nEl radio espectral > 1\n",file = self.output)
            
        print("\nT:\n", _T,file = self.output)
        print("\nC:\n", _C,file = self.output)
        print("\nradio espectral:\n",ro,file = self.output)
        _xant = self.x0
        _E = 1
        _i = 0

        resul=[]
        enc = ["Iter","E"]
        _xcont = 0
        for _val in _xant:
            enc.append("x" + str(_xcont))
            _xcont+=1

        while ((_E > self.tol) and (_i < self.nMax)):
            _xact = _T.dot(_xant) + _C
            _E = np.linalg.norm(_xant - _xact)
            _xant = _xact
            _i += 1
            #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))

            _auxRes = [_i,_E]
            #_aux = _xant.reshape(1,self.matrix.size)
            #print(_aux)
            for _val in _xant.reshape(1,self.matrix.size)[0]:
                _auxRes.append(_val)
            resul.append(_auxRes)
            #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))

        table = pd.DataFrame(resul,columns= enc)
        #print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))
        
        print("\n",table.to_string(index=False), file = self.output)
        self.content = self.output.getvalue()
        self.output.close()

            
        
            
