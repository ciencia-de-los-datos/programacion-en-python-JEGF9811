
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
    print(dicc)

        
            


        
       


    
    



    
    

    


    



    

