"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        suma = 0
        for linea in lineas:
            num = linea.split('\t')[1]
            suma += int(num)

    return suma
    

    
    


def pregunta_02():
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        dicc = []
        count_A:int = 0
        count_B:int = 0
        count_C:int = 0
        count_D:int = 0
        count_E:int = 0
        for linea in lineas:
            letra = linea.split('\t')[0]
            if letra=='A':
                count_A +=1
            elif letra=='B':
                count_B +=1
            elif letra=='C':
                count_C +=1
            elif letra=='D':
                count_D +=1
            else:
                count_E +=1
        dicc = [('A',count_A),('B',count_B),('C',count_C),('D',count_D),('E',count_E)]
    return dicc


def pregunta_03():
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        dicc = []
        count_A:int = 0
        count_B:int = 0
        count_C:int = 0
        count_D:int = 0
        count_E:int = 0
        for linea in lineas:
            letra = linea.split('\t')[0]
            num = linea.split('\t')[1]
            if letra=='A':
                count_A +=int(num)
            elif letra=='B':
                count_B +=int(num)
            elif letra=='C':
                count_C +=int(num)
            elif letra=='D':
                count_D +=int(num)
            else:
                count_E +=int(num)
    dicc = [('A',count_A),('B',count_B),('C',count_C),('D',count_D),('E',count_E)]
    return dicc


def pregunta_04():
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
    
        dicc={}
        lista=[]
        for i in range(1,13):
            clave = f'count_{i:02}'
            dicc[clave]=0
        for cuenta in dicc: #cuenta es count_01, count_02...
            for linea in lineas:
                mes = linea.split('\t')[2][5:7]
                if str(cuenta)[6::]==str(mes):
                    dicc[f'{cuenta}']+=1
            tupla=(f'{str(cuenta)[6::]}',dicc[cuenta])
            lista.append(tupla)
    return lista


def pregunta_05():
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
    
        letras=['A','B','C','D','E']
        dicc_tuplas={}
        dicc={}
        lista=[]
        for i in letras:
            clave = i
            dicc[clave]=[]
        for letra in dicc: #cuenta es count_01, count_02...
            for linea in lineas:
                num = int(linea.split('\t')[1])
                if str(letra)==str(linea.split('\t')[0]):
                    dicc[f'{letra}'].append(num)
        
            clave = letra
            dicc_tuplas[clave]=(str(letra),max(dicc[letra]),min(dicc[letra]))
            lista.append(dicc_tuplas[letra])
            
    return lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        
        letras=['a','b','c','d','e','f','g','h','i','j']
        dicc_tuplas={}
        dicc={}
        lista=[]
        dicc_local={}
        for i in letras:
            clave = i*3
            dicc[clave]=[]
        #print(dicc)
        for linea in lineas:
            dicc_local={}
            texto=(linea.split('\t')[4]).split(',')   
            i=0         
            for par in texto:
                i+=1
                claves=list(dicc_local.keys())
                clave,valor=par.split(':')
                dicc_local[clave]=int(valor)
                for key in dicc_local.keys():
                    if str(clave)==str(key):
                        dicc[f'{clave}'].append(int(valor))
        for key in dicc.keys():
            for j in range(len(dicc[key])):
                int(dicc[key][j])

            dicc_tuplas[key]=(str(key),min(dicc[key]),max(dicc[key]))
            lista.append(dicc_tuplas[key])
    return lista


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        lista_tuplas=[]
        for i in range(0,10,1):
            tupla=(i,[])
            for linea in lineas:
                letra=str(linea.split('\t')[0])
                num=int(linea.split('\t')[1])
                if num==i:
                    tupla[1].append(letra)
            lista_tuplas.append(tupla)
    return lista_tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        lista_tuplas=[]
        for i in range(0,10,1):
            lista_letras=[]
            for linea in lineas:
                letra=str(linea.split('\t')[0])
                num=int(linea.split('\t')[1])
                if num==i:
                    lista_letras.append(letra)
            c_unicos=set(lista_letras)  
            lista_letras=list(c_unicos)
            lista_letras.sort()  
            tupla=(i,lista_letras)   
            lista_tuplas.append(tupla)
    return lista_tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        letras=['a','b','c','d','e','f','g','h','i','j']
        dicc={}
        for letra in letras:
            cuenta=0
            for linea in lineas:
                pares=linea.split('\t')[4].split(',')
                for par in pares:
                    
                    clave,valor= par.split(':')
                    if str(clave)==str(letra*3):
                        cuenta+=1
                n_valor=int(cuenta)
                dicc[letra*3]=n_valor
    return dicc


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        lista=[]

        for linea in lineas:
            letra=str(linea.split('\t')[0])
            col4=len(linea.split('\t')[3].split(','))
            col5=len(linea.split('\t')[4].split(','))
            tupla=(letra,col4,col5)      
            lista.append(tupla)
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        letras=['a','b','c','d','e','f','g']
        dicc={}
        for letra in letras:
            suma=0
            for linea in lineas:
                num=int(linea.split('\t')[1])
                lista_letras=list(str(linea.split('\t')[3].split(',')))
                if str(letra) in lista_letras:
                    suma+=num
            dicc[letra]=suma
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    with open('data.csv',newline='') as cvsfile:
        spamreader =csv.reader(cvsfile,delimiter = ' ')
        info_csv = '\n'.join('\t'.join(row) for row in spamreader)
        lineas = info_csv.split('\n')
        letras=['A','B','C','D','E']
        dicc={}
        for letra in letras:
            suma_acum=0
            for linea in lineas:
                suma=0
                letra_mayus=str(linea.split('\t')[0])
                pares=linea.split('\t')[4].split(',')
                for par in pares:
                    clave,valor=par.split(':')
                    suma+=int(valor)
                if str(letra) == letra_mayus:
                    suma_acum+=suma
            dicc[letra]=suma_acum
    return dicc
