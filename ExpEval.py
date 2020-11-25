from fourFn import pyParsingEvaluate as pypEval
import numpy as np
import matplotlib.pyplot as plt
import re
import pyparsing

def rangeF(a,b):
    h=np.arange(a,b,0.1)
    return h

def graph(a,b,fn):
    FunctionEvaluate=rangeF(a,b)
    aux=FunctionEvaluate.copy()
    for i in range(0,len(FunctionEvaluate)):
        aux[i]=expEval(fn,FunctionEvaluate[i])   
    plt.xlabel(r"x")
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x)='+fn)
    plt.plot(FunctionEvaluate,aux)
    plt.grid(True)
    plt.show()

def graphP(a,b,fn,point):
    FunctionEvaluate=rangeF(a,b)
    aux=FunctionEvaluate.copy()
    for i in range(0,len(FunctionEvaluate)):
        aux[i]=expEval(fn,FunctionEvaluate[i])
    
    plt.xlabel(r"x")
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f(x)='+fn)
    plt.plot(FunctionEvaluate,aux)
          
    plt.plot(point,0, marker="o", color="red")
    
    plt.grid(True)
    plt.show()

def expEval(_function, *args):

    _function = str(_function)

    #print("\nf( g ) = ", _function)
    
    if(len(args) > 0):       
        _parsedFunction = re.sub(r"\b[x]", str(args[0]), _function)
        #print("f(", args[0] ,") = ", pypEval(_parsedFunction))
        return pypEval(_parsedFunction)
    else:
        #print("\nf( g ) = ", pypEval(_function))
        return pypEval(_function)

def parseMatrix(_rawData, _size):
    _parsedData = str(_rawData).replace(";",",")            #Remplazo de ;
    _parsedData = re.sub(r"\s","", _parsedData)             #Eliminamos espacios vacios
    _parsedData = list(map(float,str(_parsedData).split(",")))               #Listamos valores
    
    if (len(_parsedData) == _size**2):
        print("Bien")
    else:
        print("Exception")
        return ""

    _matrix = np.array(_parsedData).reshape(_size,_size)
    
    return _matrix

def parseArray(_rawData, _size):
    _parsedData = str(_rawData).replace(";",",")            #Remplazo de ;
    _parsedData = re.sub(r"\s","", _parsedData)             #Eliminamos espacios vacios
    _parsedData = list(map(float,str(_parsedData).split(",")))          #Listamos valores

    if (len(_parsedData) == _size):
        print("Bien")
    else:
        print("Exception")
        return ""

    _array = np.array(_parsedData)#.reshape(_size,1)

    return _array

def getWarType(_type):
    return {
        "Dominio": "Error al evaluar la funcion, verifique su dominio",
        "Funcion": "Error al parsear la funcion, verifique su sintaxis",
        "DivZero": "Error al intentar dividir por zero, verifique las entradas",
    }.get(_type, "Error desconocido, verifique las excepciones del metodo")

def handleError(e):
    print(e.__class__)
    if (isinstance(e, ValueError)):
        return getWarType("Dominio")

    if (isinstance(e, pyparsing.ParseSyntaxException)):
        return getWarType("Funcion")

    if (isinstance(e, ZeroDivisionError)):
        return getWarType("DivZero")
    
    return getWarType("Error")