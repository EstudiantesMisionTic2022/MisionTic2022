p = {   '1':	['Manzanas',    5000,	    25],
        '2':	['Limones',	    2300,	    15],
        '3':	['Peras',	    2700,	    33],
        '4':	['Arandanos',	9300,	    5],
        '5':	['Tomates',	    2100,	    42],
        '6':	['Fresas',	    4100,	    3],
        '7':	['Helado',	    4500,	    41],
        '8':	['Galletas',	500,	    8],
        '9':	['Chocolates',	3500,	    80],
        '10':	['Jamon',    	15000,      10]}

def borrar(cod):
    del p[cod]
    nbd = list(p.values())
    return nbd
def agregar(valoresP):
    p[cod] = valoresP
    nbd = list(p.values())
    return nbd
def actualizar(valoresP):
    p[cod] = valoresP
    nbd = list(p.values())
    return nbd
def mayorMenor(nBD, lnBD):
    colPrecios = []
    for i in range(lnBD):
        colPrecios.append(nBD[i][1])
    indiceMax = colPrecios.index(max(colPrecios))
    indiciMin = colPrecios.index(min(colPrecios))
    return nBD[indiceMax][0], nBD[indiciMin][0]
def promedio_precio(nBD, lnBD):
    s = 0
    for i in range(lnBD):
        s += nBD[i][1]
    return round(s / lnBD, 1)        
def total_inventario(nBD, lnBD):
    m = 0
    for i in range(lnBD):
        m += (nBD[i][1] * nBD[i][2])
    return round(m/1, 1)

o = input()
cod, *valoresP = input().split()
nBD = []
lnBD = 0

if (o == 'AGREGAR' and cod in p) or \
    (o == 'ACTUALIZAR' or o == 'BORRAR') and cod not in p:
    print('ERROR')
    exit()
elif o == 'BORRAR' and cod in p:
    nBD = borrar(cod)
    lnBD = len(nBD)
    print(mayorMenor(nBD, lnBD)[0], mayorMenor(nBD, lnBD)[1], 
          promedio_precio(nBD, lnBD), total_inventario(nBD, lnBD))
    exit()
else:
    valoresP[1], valoresP[2] = int(valoresP[1]), int(valoresP[2])
    if o == 'ACTUALIZAR':
        nBD = actualizar(valoresP)
        lnBD = len(nBD)
    elif o == 'AGREGAR':        
        nBD = agregar(valoresP)
        lnBD = len(nBD)
if lnBD > 9:
    print(mayorMenor(nBD, lnBD)[0], mayorMenor(nBD, lnBD)[1], 
          promedio_precio(nBD, lnBD), total_inventario(nBD, lnBD))