"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo=open("data.csv","r")
    list=[]
    suma=0
    for line in archivo:
        list.append(line[2])

    for i in list:
        suma+=int(i)

    return suma
    


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    archivo=open("data.csv","r")
    lista=[]
    conteo={}

    for line in archivo:
        lista.append(line[0])
    for letra in lista:
        if letra in conteo:
            conteo[letra]+=1
        else:
            conteo[letra]=1
    
    tuplas=sorted([(letra,cantidad) for letra,cantidad in conteo.items()])
    
    return tuplas



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    archivo=open("data.csv","r")
    lista_1=[]
    letra={}

    for line in archivo:
        lista_1.append([line[0],line[2]])

    for i in lista_1:
        if i[0] in letra:
            letra[i[0]]+=int(i[1])
        else:
            letra[i[0]] = int(i[1])
    
    tuplas=sorted([(letra,cantidad) for letra,cantidad in letra.items()])
    
    return tuplas
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    archivo=open("data.csv","r")
    lista_comp=[]
    lista_fechas=[]
    lista_fechas2=[]
    lista_meses=[]
    conteo_mes={}

    for line in archivo:
        lista_comp.append(line.split())
    for line in lista_comp:
        lista_fechas.append(line[2])
    for line in lista_fechas:
        lista_fechas2.append(line.split("-"))
    for line in lista_fechas2:
        lista_meses.append(line[1])
    for mes in lista_meses:
        if mes in conteo_mes:
            conteo_mes[mes]+=1
        else:
            conteo_mes[mes]=1
    
    tuplas=sorted([(mes,cantidad) for mes,cantidad in conteo_mes.items()])
    
    return tuplas
        
    




def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo=open("data.csv","r")
    letra={}

    for line in archivo:
        clave=line[0]
        valor=int(line[2])
        if clave in letra:
            letra[clave].append(valor)
        else:
            letra[clave]=[valor]

    tuplas=sorted([(letra,max(numeros),min(numeros)) for letra,numeros in letra.items()])
    

    return tuplas


        

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
    archivo=open("data.csv","r")
    lista_comp=[]
    lista_valores=[]
    lista_valores2=[]
    valores_min_max={}

    for line in archivo:
        lista_comp.append(line.split())
    for line in lista_comp:
        lista_valores.append(line[4])
    for line in lista_valores:
        lista_valores2.append(line.split(","))
    for sublista in lista_valores2:
        for item in sublista:
            clave, valor = item.split(":")
            valor=int(valor)
            if clave in valores_min_max:
                valores_min_max[clave] = (min(valores_min_max[clave][0], valor), max(valores_min_max[clave][1], valor))
            else:
                valores_min_max[clave] = (valor, valor)


    tuplas = sorted([(clave, valores[0], valores[1]) for clave, valores in valores_min_max.items()])

    return tuplas

    


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
    archivo=open("data.csv","r")
    numero={}

    for line in archivo:
        clave=int(line[2])
        valor=line[0]
        if clave in numero:
            numero[clave].append(valor)
        else:
            numero[clave]=[valor]


    tuplas=sorted([(numero,letras) for numero,letras in numero.items()])

    return tuplas
    



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
    archivo=open("data.csv","r")
    numero={}

    for line in archivo:
        clave=int(line[2])
        valor=line[0]
        if clave in numero:
            numero[clave].add(valor)
        else:
            numero[clave]={valor}

    numero={clave:sorted(list(valores)) for clave, valores in numero.items()}

    tuplas=sorted([(numero,letras) for numero,letras in numero.items()])

    return tuplas
    



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
    archivo=open("data.csv","r")
    lista_comp=[]
    lista_valores=[]
    lista_valores2=[]
    valores={}

    for line in archivo:
        lista_comp.append(line.split())
    for line in lista_comp:
        lista_valores.append(line[4])
    for line in lista_valores:
        lista_valores2.append(line.split(","))
    for sublista in lista_valores2:
        for item in sublista:
            clave, valor = item.split(":")
            if clave in valores:
                valores[clave] += 1
            else:
                valores[clave] = 1
    
    diccionario = dict(sorted(valores.items()))

    return diccionario


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
    archivo=open("data.csv","r")
    lista=[]
    tuplas=[]
    

    for line in archivo:
        lista.append(line.split())
        for item in lista:
            letra=item[0]
            valor1=len(item[3].split(","))
            valor2=len(item[4].split(","))
        tuplas.append((letra,valor1,valor2))

    return tuplas
            
    

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
    archivo=open("data.csv","r")
    letras={}
    lista=[]
    claves=[]
    valores=[]
    conteo={}

    for line in archivo:
        lista.append(line.split())
    for line in lista:
        claves.append(line[3].split(","))
        valores.append(int(line[1]))
    for clave, valor in zip(claves, valores):
        for letra in clave:
            if letra in letras:
                letras[letra].append(valor)
            else:
                letras[letra]=[valor]

    for letra,valores in letras.items():
        letras[letra]=sum(valores)

    letras_ordenadas=dict(sorted(letras.items()))
    
    return letras_ordenadas


    


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
    archivo=open("data.csv","r")
    suma_valores = {}

    for line in archivo:
        lista = line.split()
        clave = lista[0]  
        valores = lista[4]  

        
        for elemento in valores.split(","):
            _, valor = elemento.split(":")
            suma_valores[clave] = suma_valores.get(clave, 0) + int(valor)

    letras_ordenadas=dict(sorted(suma_valores.items()))
    
    return letras_ordenadas
    



pregunta_01()
pregunta_02()
pregunta_03()
pregunta_04()
pregunta_05()
pregunta_06()
pregunta_07()
pregunta_08()
pregunta_09()
pregunta_10()
pregunta_11()
pregunta_12()