#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://razonartificial.com/2010/08/arboles-e-inteligencia-artificial-ii/
#-------------------------------------
#https://iartificial.net/arboles-de-decision-con-ejemplos-en-python/
#http://www.aprendemachinelearning.com/arbol-de-decision-en-python-clasificacion-y-prediccion/
# Clases
# -----------------------------------------------------------

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return str(self.carga)

# -----------------------------------------------------------
# Funciones
# -----------------------------------------------------------

def si(preg):
    from string import lower
    resp = lower(raw_input(preg))
    return (resp[0] == 's')

# -----------------------------------------------------------

def main():
    bucle = True
    raiz = Arbol("pajaro")#crea un arbol
    while bucle:
        if not si("Estas pensando en un animal? "): break

        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        #adivinar
        animal = arbol.carga
        if si("Es un " + animal + "? "):
            print "Soy el más grande!"
            continue

        #obtener informacion
        nuevo = raw_input("Qué animal era? ")
        info = raw_input("Qué diferencia a un " + animal + " de un " + nuevo + "? ")
        indicador = "Si el animal fuera un " + animal + " cual seria la respuesta? "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)

    return 0

if __name__ == '__main__':
    main()