# coding: utf-8
import pilasengine
import random
#Integrantes: Genesis, Loana, Dalila, Nicolas
pilas = pilasengine.iniciar()

lista_jugador = []

def generar_boton(): #Funcion que crea un actor boton y lo devuelve como resultado
    boton = pilas.actores.Boton()
    boton.texto = "verificar"
    boton.y = -200
    return boton

def generar_lista_inicial(): #Funcion que genera una lista de 10 numeros aleatorio y la devuelve
    lista_numeros = []
    for i in range (0,10):
        numero_aleatorio = random.randint(1,10)
        lista_numeros.append(numero_aleatorio)  
    return lista_numeros
    
def ubicar_elementos_numero(lista):
    #Esta funcion toma la lista de numeros como parametro
    #para crear los objetos texto y ubicarlos en la pantalla
    grupo = pilas.actores.Grupo()
    i = -250
    for numero in lista:
        nro = pilas.actores.Texto(str(numero))
        nro.x = i
        grupo.append(nro)
        i= i+50
    grupo.aprender(pilas.habilidades.Arrastrable)
    grupo.radio_de_colision = 10
    return grupo

def ubicar_elementos_manzana():
    #Funcion que muestra las manzanas por pantalla
    manzanas = pilas.actores.Manzana()*10 
    manzanas.escala = 0.5
    manzanas.y= -100
    i = -270
    for manzana in manzanas:
        manzana.x = i
        i= i+60
    manzanas.radio_de_colision = 5
    return manzanas

def obtener_lista_jugador(texto, manzana):
   #crea una lista con valores que ordeno el jugador
    numero = int(texto.texto) 
    lista_jugador.append(numero)
    pilas.avisar(str(numero))
    return lista_jugador
    
def ordenar_menor_mayor(lista_numeros, tam):
   for i in range(0,len(lista_numeros)-1):#i recorre del 0 hasta la longuitud de los num aleatorios
        min = i
        for j in range(i+1,len(lista_numeros)):#J recorre lo mismo pero en una posicion mas
            if lista_numeros [min]>lista_numeros[j]:
                min = j
        aux= lista_numeros[min]
        lista_numeros[min] = lista_numeros[i]
        lista_numeros[i] = aux
   return lista_numeros
    
def ordenar_mayor_menor(lista_numeros, tam):
    pass
    
def comprobar_respuestas():
    #Funcion que compara cada elemento de la lista_numeros con lista_jugador
    #para saber si ordeno correctamente
    pilas.avisar("Verificando...")
    i=0
    estado = True
    for x in range (0,len(lista_jugador)):
         if lista_numeros[i] != lista_jugador[i]:
            estado=False
         i=i+1
    if estado:
        pilas.avisar("Muy bien!!")
    else:
        pilas.avisar("volve a intentarlo!")
        
verificar = generar_boton()
manzana = ubicar_elementos_manzana()
lista_numeros = generar_lista_inicial()
numeros = ubicar_elementos_numero(lista_numeros)
ordenar_menor_mayor(lista_numeros,len(lista_numeros))
pilas.colisiones.agregar(numeros, manzana, obtener_lista_jugador)

verificar.conectar_presionado(comprobar_respuestas)



pilas.ejecutar()