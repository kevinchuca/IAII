#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    raiz = Arbol("Estudiante")#crea un arbol
    while bucle:
        if not si("¿Esta pensando en una persona de la EMI? "): break
        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha
        #adivinar
        persona = arbol.carga
        if si("¿Esa persona es " + persona + "? "):
            print "Soy el más grande!"
            continue

        #obtener informacion
        nuevo = raw_input("¿Qué cargo tiene esa persona? ")
        info = raw_input("¿Que pregunta distinguiría " + persona + " de un " + nuevo + " ? ")
        indicador = "¿Si la persona fuera un " + persona + " cual seria la respuesta? "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(persona)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(persona)
            arbol.izquierda = Arbol(nuevo)
    return 0

if __name__ == '__main__':
    main()