#Codigo de interaccion entre Arduino y OpenCV
#Por Glar3

import cv2
import numpy as np
import serial #cargamos la libreria serial
#Iniciamos la camara
captura = cv2.VideoCapture(2)

#Iniciamos la camara
#Iniciamos la comunicacion serial
ser = serial.Serial('com3', 9600)

while(1):

   #Capturamos una imagen y la convertimos de RGB -> HSV
   _, imagen = captura.read()
   hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

   #Establecemos el rango de colores que vamos a detectar
   #En este caso de verde oscuro a verde-azulado claro
   verde_bajos = np.array([49,50,50], dtype=np.uint8)
   verde_altos = np.array([80, 255, 255], dtype=np.uint8)

   #Crear una mascara con solo los pixeles dentro del rango de verdes
   mask = cv2.inRange(hsv, verde_bajos, verde_altos)

   #Encontrar el area de los objetos que detecta la camara
   moments = cv2.moments(mask)
   area = moments['m00']

   #Descomentar para ver el area por pantalla
   #print area

   #Si el objeto tiene un area determinada, escribimos 'h'
   #Si no, escribimos un caracter erroneo
   print area
   limsup=9537000
   liminf=6554265
   if(area<limsup and area>liminf):
       ser.write('r')
       print ("Recto")
   elif(area > limsup):
      ser.write('h')
      print("Mayor")
   elif(area < liminf):
      ser.write('n')
      print("Menor")

   #Mostramos la imagen original y
   #la mascara
   cv2.imshow('mask', mask)
   cv2.imshow('Camara', imagen)
   tecla = cv2.waitKey(5) & 0xFF
   if tecla == 27:
      break

cv2.destroyAllWindows()
