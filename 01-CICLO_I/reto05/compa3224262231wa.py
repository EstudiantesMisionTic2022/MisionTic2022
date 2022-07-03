database = {  
    1: ["manzanas", 5000.0, 25,],
    2: ["limones", 2300.0, 15,],
    3: ["peras", 2700.0, 33,],
    4: ["arandanos", 9300.0, 5,],
    5: ["tomates", 2100.0, 42,],
    6: ["fresas", 4100.0, 3,],
    7: ["helado", 4500.0, 41,],
    8: ["galletas", 500.0, 8,],
    9: ["chocolates", 3500.0, 80,],
    10: ["jamon", 15000.0, 10,],
}



def leer_datos():
    operacion = input()
    producto = input().split()
    producto[0] = int(producto[0])
    producto[2] = float(producto[2])
    producto[3] = int(producto[3])

def agregar (database, producto):
    if producto [0] in database:
        return False
    index = producto[0] 
    producto.pop(0)
    database [index] = producto
    return True
    
def actualizar (database, producto):
    if producto [0] in database:
        index = producto[0] 
        producto.pop(0)
        database [index] = producto
        return True
    return False


def borrar ( database, producto):
    if producto in database:
        database.pop(producto[0])
        return True
    return True

def precio_mayor(database):
    mayor = 0
    for i in database:
        if database[i][1] > mayor:
            mayor = database[i][1]
            nombre = database[mayor][0]
            return nombre


def precio_menor(database):
    menor = list(database.keys())(0)
    for i in database:
        if database [i][1] < database[menor][1]:
            menor = i
            return database[menor][0]     


def promedio_precios(database):
    promedio = 0
    for i in database:
        promedio += database [i][1]
        promedio = promedio/len(database)
        return promedio


def valor_inventario(database):
    valor_inventario == 0.0
    for i in database:
        valor_inventario += database[i][1] * database[i][2]
        return valor_inventario 

        
operacion, producto = leer_datos()
if operacion == "AGREGAR":
    flags = agregar(database, producto)
elif operacion == "BORRAR":
    flags = borrar(database, producto)
elif operacion == "ACTUALIZAR":
    flags = actualizar(database, producto)


print(precio_mayor(database)), (precio_menor(database)), round(promedio_precios(database), 1), round(valor_inventario(database), 1)
