# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras (texto):
    """
    Función para calcular la frecuencia de cada letra en  un texto

    Args:
    texto: cadena de texto en la que se contaràn las letras (str)
    
    Returns:
    diccionario con las letras como claves y las frecuencias como valores (dict [str, int])
    """
    frecuencias = {}
    for letra in texto:
        letra = letra.lower()  #convertimos en minuscula todas lasletras
        if  not letra.isalpha(): #verificamos si la letra es alfabética
            continue 

        frecuencias [letra] = frecuencias.get (letra, 0) +1
    return frecuencias


texto = "Hola, Marina Gallus"
output = frecuencia_letras (texto)
print (f"El resultado de la función es: {output}")

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros =  [2, 3, 4, 5, 6]
doble_numeros = list (map(lambda x: x*2, numeros))
print (f"La lista que muestra el doble de cada numero es {doble_numeros}")

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def lista_objetivo (lista_palabras, palabra_objetivo):
    """
    Función para filtrar las palabras que contienen una palabra objetivo.
    
    Args:
    lista_palabras: lista de palabras (list)
    palabra_objetivo: palabra a buscar dentro de las palabras de la lista (str)

    Returns:
    Lista con las palabras que contienen la palabra objetivo (list)
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]


lista_nombres = ["Marina", "Caterina", "Adriana", "Karina", "Valentina", "Paola", "Silvia"]
output = lista_objetivo (lista_nombres, "ina")
print (f"El resultado de la función es: {output}")


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas (lista1, lista2):
    """
    Una función que calcula la diferencia entre los valores de dos listas
    
    Args: 
    lista1: primera  lista de valores (list[float])
    lista2: segudna lista de valores (list[float])

    Returns:
    lista con la diferencia de los valores de las listas dadas (list[float])
   """
    return list(map(lambda x, y : x - y, lista1, lista2))


lista_numeros1 = [18, 24, 33, 67, 89]
lista_numeros2 = [17, 31, 33, 56, 57]
output = diferencia_listas (lista_numeros1, lista_numeros2)
print (f"El resultado de la función es: {output}")

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_estado (lista_numeros, valor_objetivo):
    """
    Una función para calcular la media de una lista de numeros y comprobar si es mayor, igual o menos a un valor objetivo

    Args:
    lista_numero: lista de numeros de numeros (list[int, float])
    valor_objetivo: valor de corte para aprobar o menos (int, float)

    Return:
    Una tupla con media y estado (tuple[float, str])
    """
    media = sum(lista_numeros) / len(lista_numeros) # calculamos la media
    estado = "aprobado" if media >=  valor_objetivo else "suspenso" # determinamos el estado
    return (media, estado)
        

notas_examenes =  [4, 5, 6, 5, 7, 10]
nota_corte = 5
output = media_estado (notas_examenes, nota_corte)
print (f"El resultado de la función es: {output}")

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial (n):
    """
    Una función para calcular el factorial de un numero

    Args:
    n: numero del que vamos a calcular el factrorial (int, float)

    Return:
    Caso recursivo: si n es mayor que 1, calculamos n * factorial(n - 1)
    """
    
    if n == 0 or n == 1:  # Caso base: si n es 0 o 1, el factorial es 1 y se detiene la recursión
        return 1
    else:  # La función se llama a sí misma con n-1, repitiendo este proceso hasta llegar al caso base
         return n * factorial (n - 1)


n = 8
output = factorial (n)
print (f"El resultado de la función es: {output}")

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuple_to_string (lista_tuplas):
    """
    Una función que convierte una lista de tuplas a una lista de cadenas de texto.

    Args:
    lista_tuplas: una lista de tuplas que se van a convertir a cadenas de texto

    Return:
    list: Una lista de cadenas de texto, donde cada tupla se convierte en  string.  
     """
    return list (map(lambda tupla: str (tupla), lista_tuplas))

lista_tuplas = [(1, 1),(2, 3), (5, 8, 13, 21)]
output = tuple_to_string (lista_tuplas)
print (f"El resultado de la función es: {output}")

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

numero1 = input ("inserta un numero")
numero2 = input ("inserta otro numero")

try:
    numero1 = int (numero1)
    numero2 = int (numero2)
    
    if numero2 == 0:
        print ("numero2 tiene que ser distinto de cero")
    
    else:
        división_numeros = numero1 / numero2
        print (f"El resultado de la división es: {división_numeros}")

except ValueError:
    print ("Por favor, inserta solo números")


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

mascotas = ["Perro", "Gato", "Rata", "Oso", "Conejo", "Tigre", "Cocodrilo"]
mascotas_excluir = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

output =  list(filter (lambda mascota: mascota not in mascotas_excluir, mascotas))
print (f"El resultado de la función filter es : {output}")

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

lista_numeros = [2, 4, 6, 7, 89, 34, 8]

try:
     promedio = sum  (lista_numeros) / len (lista_numeros)
     print (f"El promedio es: {promedio}")

except ZeroDivisionError:
    print ("La lista no puede estar vacía")

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try: 
    edad_usuario = int(input ("por favor, inserte su edad"))
    if edad_usuario <= 0:
        print ("la edad no puede tener un valor negativo")
    
    elif edad_usuario >120:
        print ("Eres muy longevo, que suerte. ¿Seguro que has introducido bien tu edad?")
    
    else: 
        print (f"Tu edad es {edad_usuario}")

except ValueError:
    print ("por favor, ingrese un valor numerico")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras (frase):

 # Se usa el metodo split  para separar la frase en palabras. Usamos  map para obtener la longitud de cada una

      return list(map (len, frase.split() ))


frase = "Me llamo Marina"
output = longitud_palabras (frase)
print (f"El resultado de la función es: {output}")

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def generar_tuplas (caracteres):
   # Elimina duplicados usando un set y luego usa map para generar las tuplas
    return list(map (lambda c: (c.upper(), c.lower()), set(caracteres)))

caracteres = ["e", "s","t","u", "d", "i", "a", "n", "t", "e"]
caracteres = set (caracteres)
output = generar_tuplas (caracteres)
print (f"El resultado de la función es: {output}")


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()

def letra1_palabra(lista_palabras, letra):
    """
    Una función que retorna las palabras de una lista que comienzan con una letra específica.

    Args:
    lista_palabras: una lista de palabras (str).
    letra: una letra con la cual deben comenzar las palabras (str)

    Return:
    list: Una lista de palabras que comienzan con la letra especificada.
    """
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))


lista_de_palabras = ["Maria", "David", "Clara", "Micheal", "Marta"]
letra = "m"
output = letra1_palabra (lista_de_palabras, letra)
print (f"El resultado de la función es: {output}")


# 15.Crea una función lambda que sume 3 a cada número de una lista dada.

def suma_tres (lista_numeros):
    """
    Una función que suma 3 a cada número de una lista dada.

    Args:
    lista: una lista de números.

    Return:
    list: una nueva lista con 3 sumado a cada número de la lista original.
    """

    return list (map (lambda x: x+3, lista_numeros))

numeros = [2, 4, 5, 6, 9]
output = suma_tres (numeros)
print (f"El resultado de la función es: {output}")

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas (texto, n):

    """
    Esta función toma una cadena de texto y un número entero `n`, y devuelve una lista de todas las palabras 
    que tienen una longitud mayor a `n`.

    Args:
    texto (str): La cadena de texto que se desea procesar.
    n (int): El número entero que se utiliza como referencia para la longitud de las palabras.

    Returns:
    list: Una lista con todas las palabras que tienen una longitud mayor a `n`.
    """
    palabras = texto.split ()
    return list(filter(lambda palabra: len(palabra) > n, palabras ))

frase = "este es un texto de prueba para mi función"
output = palabras_largas (frase, 4)
print (f"El resultado de la función es: {output}")

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce
def juntar_numeros (digitos):
    """
    Convierte una lista de dígitos en el número correspondiente.

    Args:
    digitos (list): Una lista de números enteros que representan los dígitos de un número.

    Returns:
    int: El número entero correspondiente a los dígitos de la lista.
    """
    return reduce (lambda x, y: x*10 + y, digitos )

lista_de_numeros = [2, 3, 4, 5]
output = juntar_numeros (lista_de_numeros)
print (f"El resultado de la función es: {output}")

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def filtro_calificacion(lista_diccionario):
    """
    Filtra una lista de diccionarios de estudiantes para devolver aquellos cuya calificación 
    sea mayor o igual a 90.

    Args:
    lista_diccionario (list): Una lista de diccionarios, donde cada diccionario contiene la información 
     de un estudiante. Cada diccionario debe tener las claves 'nombre', 'edad', y 'calificacion'.

    Returns:
    list: Una lista de diccionarios que contiene solo a los estudiantes cuya calificación es mayor o igual a 90.
"""
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_diccionario))

estudiantes = [
    {'nombre': 'Juan', 'edad': 20, 'calificacion': 95},
    {'nombre': 'Ana', 'edad': 22, 'calificacion': 85},
    {'nombre': 'Pedro', 'edad': 21, 'calificacion': 92},
    {'nombre': 'Maria', 'edad': 23, 'calificacion': 88}
]

estudiantes_aptos = filtro_calificacion(estudiantes)
print (f"Los estudiantes con calificacion por encima del limite definido son: {estudiantes_aptos}")

# 19. Crea una función lambda que filtre los números impares de una lista dada.

def numeros_imapres (lista_numeros):
    """
    Esta función toma una lista de números y devuelve una nueva lista que contiene solo los números 
    impares 

    Args:
    lista_numeros (list): Una lista de números enteros.

    Returns:
    list: Una lista que contiene solo los números impares de la lista original.
    """
    return list (filter (lambda n: n % 2 != 0, lista_numeros))

lista_numeros = [2, 4, 5, 6, 7, 8, 9]
output = numeros_imapres (lista_numeros)
print (f"Los numeros impares son: {output}")

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

def lista_int (lista_mixta):

    """
    Esta función toma una lista que puede contener elementos de diferentes tipos y devuelve 
    una nueva lista que contiene solo los elementos que son numericos enteros.

    Args:
    lista_mixta (list): Una lista que puede contener elementos de cualquier tipo.

    Returns:
    list: Una lista que contiene solo los elementos de tipo numerico entero (int) de la lista original.
    """
    return list (filter (lambda x: type (x) == int, lista_mixta))

lista_mixta = [2, 3, 4, 5, "lunes", "martes", "miercoles"]
output = lista_int (lista_mixta)
print (f"La lista que incluye solo los valores de tipo integer contenidos en lista_mixta es: {output}")

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcula_cubo (numero):
    """
    Esta función toma un número como argumento y devuelve su cubo. El cálculo se realiza 
    mediante una función lambda que eleva el número a la potencia de 3.

    Args:
    numero (int/float): El número al que se le calculará el cubo. Puede ser un número entero o flotante.

    Returns:
    int/float: El cubo del número dado. El tipo de retorno depende del tipo de `numero`.
    """
    cubo = lambda n : n**3
    return cubo (numero)

numero = 54
output = calcula_cubo (numero)
print (f"El cubo del numero dado es: {output}")

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_numeros (lista_numeros):
     """
    Esta función toma una lista de números y utiliza la función `reduce()` para calcular 
    el producto de todos los números de la lista. Aplica la operación de multiplicación de manera acumulativa
    sobre los elementos de la lista.

    Args:
    lista_numeros (list): Una lista de números (enteros o flotantes) sobre los que se calculará el producto.

    Returns:
    int/float: El producto total de los números de la lista. El tipo de retorno depende de los valores en la lista.
    """
    
     return reduce (lambda x, y : x*y , lista_numeros)


lista_numeros = [2, 3, 4, 5]
output = producto_numeros (lista_numeros)
print (f"El producto del los numeros de la lista dada es: {output}")

# 23. Concatena una lista de palabras.Usa la función reduce() .

lista_palabras = ["El", "tiempo", "hoy", "es", "muy", "bonito"]
output = reduce (lambda x, y: x + " " + y, lista_palabras)
print (output)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

lista_numeros = [1, 2, 3, 25, 54, 32, 1,7, 8, 9]
diferencia_numeros = reduce (lambda x, y: x - y, lista_numeros)
print (f" La diferencia total en los valores de la lista dada es: {diferencia_numeros}")

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def cuenta_caracteres (texto):
     """
    Esta función toma una cadena de texto y devuelve la cantidad de caracteres 
    que contiene. 

    Args:
    texto (str): La cadena de texto cuya longitud se desea contar.

    Returns:
    int: El número de caracteres en la cadena de texto.
    """
     return len (texto)

texto = "hola, me llamo Marina"
output = cuenta_caracteres (texto)
print (f"El numero de caracteres del texto dado es: {output}")

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

calcula_resto = lambda x, y : x % y
numero1 = 25
numero2= 7
output = calcula_resto (numero1, numero2)
print (f"El resto de dividir los dos numeros dados es: {output}")

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio_numeros(lista_numeros):
    """
    Esta función toma una lista de números y devuelve su promedio, es decir, la suma 
    de todos los elementos dividida entre la cantidad de elementos de la lista.

    Args:
    lista_numeros (list): Una lista de números (enteros o flotantes) de los cuales se calculará el promedio.

    Returns:
    float: El promedio de los números en la lista. Si la lista está vacía, devuelve 0.
    """
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


lista_numeros = [10, 20, 30, 40]
output = promedio_numeros (lista_numeros)
print (output)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado en una lista dada.

    Args:
    lista (list): Una lista de elementos (pueden ser de cualquier tipo).

    Returns:
    El primer elemento duplicado si se encuentra, o None si no hay duplicados.
    """
    vistos = set()  # Conjunto para almacenar los elementos ya vistos
    for elemento in lista:
        if elemento in vistos:
            return elemento  # Devuelve el primer duplicado encontrado
        else:
             vistos.add(elemento)  # Agrega el elemento al conjunto de vistos
    return None  # Si no hay duplicados, devuelve None


lista = [2, 3, 4, 5, 6, 2, 4, 7, 8, 3, 7]
output = primer_duplicado (lista)
print (f"El primer elemento duplicado de la lista dada es: {output}")

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    """
    Convierte una variable en una cadena de texto y enmascara todos los caracteres con el carácter '#',
    excepto los últimos cuatro caracteres.

    Args:
    variable (int, float, str): La variable que se convertirá a cadena y enmascarará.

    Returns:
    str: La cadena resultante con los caracteres enmascarados, excepto los últimos cuatro.

    """
    # Convertir la variable a cadena
    cadena = str(variable)
    
    # Enmascarar los caracteres, excepto los últimos cuatro
    if len(cadena) > 4:
        return '#' * (len(cadena) - 4) + cadena[-4:]
    else: 
        return cadena  # Si la cadena tiene 4 caracteres o menos, se retorna tal cual


variable = 12345678
output = enmascarar_variable (variable)
print (f" La variable enmascarada queda así: { output}")

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas (palabra1, palabra2):
     """
    Determina si dos palabras son anagramas, es decir, si están formadas por las mismas letras
    pero en diferente orden.

    Args:
    palabra1 (str): La primera palabra.
    palabra2 (str): La segunda palabra.

    Returns:
    bool: True si las palabras son anagramas, False en caso contrario.
    """
     return sorted(palabra1.lower()) == sorted(palabra2.lower())

palabra1 = "japones"
palabra2 = "esponja"
output = son_anagramas (palabra1, palabra2)
if output == True:
    print (f"Si, las palabras dadas son anagramas")
else:
    print("No, las palabras dadas no son anagramas")

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def busca_nombre(lista_nombres, nombre_buscado):
    """
    Busca un nombre en una lista de nombres y muestra un mensaje indicando si fue encontrado.
    
    Si el nombre no está en la lista, se lanza una excepción que es capturada y mostrada 
    como un mensaje de error.

    Args:
    lista_nombres (list): Una lista de nombres en los que se realizará la búsqueda.
    nombre_buscado (str): El nombre que se buscará en la lista de nombres.

    Returns:
    None: La función no retorna ningún valor. Si el nombre se encuentra, imprime un mensaje, y si no se encuentra, lanza una excepción que también imprime un mensaje.

    Raises:
    ValueError: Si el nombre no se encuentra en la lista, se lanza una excepción con un mensaje de error.
    """
    try:
        # Comprobamos si el nombre está en la lista
        if nombre_buscado in lista_nombres:
            print(f"El nombre {nombre_buscado} fue encontrado en la lista de nombres dada.")
        else:
            # Lanzamos una excepción si el nombre no está en la lista
            raise ValueError(f"El nombre {nombre_buscado} no se encuentra en la lista dada.")
    except ValueError as e:
        print(e)



lista_nombres = input ("Por favor, introduzca una lista de nombres")
nombre_buscado = input ("Por favor, indica un nombre a buscar en la lista dada anteriormente")
output = busca_nombre(lista_nombres, nombre_buscado)

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre_completo, lista_empleados):
    """
    Busca un empleado en una lista de empleados y devuelve su puesto si se encuentra.

    Esta función recibe un nombre completo y una lista de diccionarios de empleados, donde cada
    diccionario contiene 'nombre' y 'puesto'. Si el nombre completo se encuentra en la lista,
    se devuelve el puesto del empleado. Si no se encuentra, se devuelve un mensaje indicando 
    que la persona no trabaja en la empresa.

    Args:
    nombre_completo (str): El nombre completo del empleado a buscar.
    lista_empleados (list): Una lista de diccionarios con los empleados, donde cada diccionario tiene las claves 'nombre' y 'puesto'.

    Returns:
    str: El puesto del empleado si se encuentra en la lista, o un mensaje indicando que no trabaja aquí si no está en la lista.
    """
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return print(f"El puesto de {nombre_completo} es {empleado['puesto']}")
    
    # Si no se encuentra el nombre, devolver el mensaje de error fuera del bucle
    return f"{nombre_completo} no trabaja aquí"



nombre_completo = input ("Indicame que empleado estás buscando")
lista_empleados = [
    {"nombre": "Mario Diaz", "puesto": "account manager"},
    {"nombre": "Roberto Garcia", "puesto": "business manager"},
    {"nombre": "Maria Gimenez", "puesto": "accountant"},
    {"nombre": "Sara Welsh", "puesto": "comercial"},
    {"nombre": "Jaime Foronda", "puesto": "analista de datos"}
    ]
output = buscar_empleado(nombre_completo, lista_empleados)

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

suma_elementos_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


lista_elementos1 = [1, 2, 3, 4, 5, 6]
lista_elementos2 = [7, 8, 9, 10, 1, 1]
output = suma_elementos_listas (lista_elementos1, lista_elementos2)
print (f"La suma de los elementos de las dos listas dadas es: {output}")

# 34.  Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos paranmanipular la estructura del árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []
        
    def crecer_tronco (self):
        self.tronco +=1
    
    def nueva_rama (self):
        self.ramas.append(1)

    def crecer_ramas (self):
        self.ramas = [longitud +1 for longitud in self.ramas]

    def quitar_rama (self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else: 
             print ("posición invalida")

    def info_arbol (self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


naranjo = Arbol()                            #1. Crear un arbol
naranjo.crecer_tronco()               #2. Hacer crecer el tronco una unidad
naranjo.nueva_rama()                  #3. Añadir una nueva rama
naranjo.crecer_ramas()                #4. Hacer crecer todas las ramas
naranjo.nueva_rama()                  #5. Añadir otra rama
naranjo.nueva_rama()                  #5.Añadir otra rama
naranjo.quitar_rama(2)                #6. Retirar la rama en la posición 2
info = naranjo.info_arbol()            #7. Obtener información

print (info)

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if self.saldo < cantidad:
            raise ValueError(f"No hay suficiente saldo para retirar {cantidad} €. Saldo actual: {self.saldo} €.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} €. Nuevo saldo: {self.saldo} €.")

    def transferir_dinero(self, otro_usuario, cantidad):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("El usuario origen debe ser una instancia de UsuarioBanco.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if otro_usuario.saldo < cantidad:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad} €.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} ha transferido {cantidad} € a {self.nombre}.")
        print(f"Saldo de {otro_usuario.nombre}: {otro_usuario.saldo} €, Saldo de {self.nombre}: {self.saldo} €.")

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad} €. Nuevo saldo: {self.saldo} €.")



# 36. Caso de Uso
# 1.Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2.Agregar 20 unidades de saldo de "Bob".
# 3.Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". 
# 4.Retirar 50 unidades de saldo a "Alicia".

# Paso 1: Crear usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# Paso 2: Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)  # Saldo de Bob: 70

# Paso 3: Transferir 80 unidades desde Bob a Alicia
# Esto lanzará error porque Bob solo tiene 70. Por lo tanto le agregamos 10.
bob.agregar_dinero(10)  # Saldo total ahora: 80

# Transferimos dinero de Bob a Alicia
alicia.transferir_dinero(bob, 80)  # Alicia recibirá 80

# Paso 4: Retirar 50 unidades de saldo de Alicia
alicia.retirar_dinero(50)  # Nuevo saldo de Alicia


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto . Código a seguir:
# 1.Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3.Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4.Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.strip(".,;:!?")  # Limpieza básica
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' necesitas palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' necesitas la palabra a eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'")


# 37. Caso de Uso
# Comprueba el funcionamiento completo de la función procesar_texto

texto = "hola gente, hola me llamo Marina me llamo"

resultado_contar = procesar_texto(texto, "contar")
print("Conteo de palabras:", resultado_contar)

resultado_reemplazo = procesar_texto(texto, "reemplazar", "llamo", "soy")
print("Texto tras reemplazo:", resultado_reemplazo)

resultado_eliminar = procesar_texto(texto, "eliminar", "me")
print("Texto tras eliminar:", resultado_eliminar)



# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    if hora < 0 or hora > 23:
        return "La hora introducida no es válida. Introduce un número entre 0 y 23."
    elif 6 <= hora < 12:
        return "Es de día (mañana)."
    elif 12 <= hora < 18:
        return "Es de tarde."
    else:
        return "Es de noche."


try:
    entrada = input("Introduce la hora actual (0-23): ")
    hora = int(entrada)
    resultado = momento_del_dia(hora)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")


# 39.  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# -  70 - 79 bien
# -  80 - 89 muy bien
# -  90 - 100 excelente

def calificacion_en_texto(nota):
    if nota < 0 or nota > 100:
        return "Calificación no válida. Debe estar entre 0 y 100."
    elif nota < 70:
        return "Insuficiente"
    elif nota < 80:
        return "Bien"
    elif nota < 90:
        return "Muy bien"
    else:
        return "Excelente"


try:
    entrada = input("Introduce la calificación numérica del alumno (0-100): ")
    nota = int(entrada)
    resultado = calificacion_en_texto(nota)
    print("Resultado:", resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    figura = figura.lower()  
    
    if figura == "rectangulo":
        if len(datos) != 2:
            return "Para un rectángulo se necesitan base y altura."
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            return "Para un círculo se necesita solo el radio."
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        if len(datos) != 2:
            return "Para un triángulo se necesitan base y altura."
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no reconocida. Usa 'rectangulo', 'circulo' o 'triangulo'."


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1.Solicita al usuario que ingrese el precio original de un artículo.
# 2.Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3.Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4.Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5.Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6.Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_precio_final():
    try:
        precio_original = float(input("Introduce el precio original del artículo: "))

        if precio_original < 0:
            print("El precio no puede ser negativo.")
            return

        tiene_cupon = input("Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Introduce el valor del cupón: "))
            
            if valor_cupon > 0:
                precio_final = max(precio_original - valor_cupon, 0)
                print(f" Cupón aplicado. Precio final: {precio_final:.2f} €")
            else:
                print("El cupón no es válido. Se usará el precio original.")
                print(f"Precio final: {precio_original:.2f} €")
        else:
            print(f"Sin cupón. Precio final: {precio_original:.2f} €")

    except ValueError:
        print("Entrada no válida. Asegúrate de introducir números correctamente.")


calcular_precio_final()



