# **Gestión de inventario de una tienda**

El objetivo principal de este reto es implementar funciones. 

El inventario inicial de la tienda está contenido en el siguiente diccionario:

```
inventario_inicial = {   
    '1':    ['Manzanas',    5000,   25],
    '2':	['Limones',	    2300,   15],
    '3':	['Peras',	    2700,	33],
    '4':	['Arandanos',	9300,	5],
    '5':	['Tomates',	    2100,	42],
    '6':	['Fresas',	    4100,	3],
    '7':	['Helado',	    4500,	41],
    '8':	['Galletas',	500,	8],
    '9':	['Chocolates',	3500,	80],
    '10':	['Jamon',    	15000,  10]}
```
El inventario inicial sufrirá modificaciones de acuerdo al ingreso de datos.

- Si se ingresa AGREGAR, la función `agregar()` debe agregar un producto que no exista en el inventario con sus respectivos valores (Nombre, Precio, Cantidad), los cuales se ingresan en la segunda línea.
- Si se ingresa BORRAR, la función `borrar()` debe eliminar un producto existente en el inventario y sus respectivos valores.
- Si se ingresa ACTUALIZAR, la función `actualizar()` debe actualizar el Precio y la Cantidad de un producto existente en el inventario.

Se debe imprimir 'ERROR' `print('ERROR')` en los siguientes casos:
* Si se ingresa BORRAR o ACTUALIZAR un producto inexistente en el inventario
* Si se ingresa AGREGAR un producto existente en el inventario.

El `print()` de salida debe contener los siguientes cuatro datos:
1. Nombre del producto con el precio mayor
2. Nombre del producto con el precio menor
3. Promedio de precios
4. Total del inventario que equivale a la suma de los precios de cada producto por su cantidad

Los valores numéricos deben contener un número decimal.
___
## **Casos de prueba**
### **Caso 1**
*Entrada de datos*

* `input()` = ACTUALIZAR

* `input().split()` = 7 Helado 65000 11

*Salida de datos*
* Helado Galletas 10950.0 1544600.0
___

### **Caso 2**
*Entrada de datos*

* `input()` = BORRAR

* `input().split()` = 3 Peras 2700 33 

*Salida de datos*
* Jamon Galletas 5144.4 925000.0
___
### Casos en los que la salida debe ser **ERROR**

#### Caso A

* `input()` = BORRAR

* `input().split()` = 15 Papa 1500 10
 33 

#### Caso B
* `input()` = BORRAR

* `input().split()` = 14 Maiz 45000 12 

#### Caso C
* `input()` = ACTUALIZAR

* `input().split()` = 15 Papa 1500 10 

#### Caso D
* `input()` = AGREGAR

* `input().split()` = 3 Peras 2700 33 

___
Las funciones `quit()` y `exit()` generaron fallas en las plataformas MasterTech y Colab. 
Sin embargo, en Visual Studio Code no ocasionaron ningún problema.
