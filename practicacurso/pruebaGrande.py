# -*- coding: utf-8 -*-
from scipy.io import loadmat
import matplotlib.image as img
import numpy
import scipy.misc
import matplotlib.pyplot as pl
from PIL import Image

r=loadmat ("modeloDig")
#print "la tabla contiene:"
#print r.keys()
#print "thetha 1 es: "
#print r['Theta1'].shape
#print "thetha 2 es: "
#print r['Theta2'].shape
#print "la imagen mide: "
image = img.imread("IMG_20190620_212744.png")


image= image.transpose()
#print image.shape
#print "imagen convertida: "
key = scipy.misc.imread("D:\Unidad D\EMI\8vo semestre\INTELIGENCIA ARTIIFICIAL II\RECONOCIMIENTO\IAII\practicacurso\IMG_20190620_212744.png")
#No da esta parte de la imagen pa cambiar el tamaño
#ext = key.resize((20, 20), img.ANTIALIAS)
#key.save("BICUBIC" + ext)


print "imagen a colors"
imagen = Image.open("IMG_20190620_212744.png")
imagen.show()
print imagen.size
print "imagen reducida"
ext = imagen.resize((20, 20), Image.BICUBIC)
#key.save("BICUBIC" + ext)
ext.show()
print ext.size
ext.save("mini.png")
key = scipy.misc.imread("D:\Unidad D\EMI\8vo semestre\INTELIGENCIA ARTIIFICIAL II\RECONOCIMIENTO\IAII\practicacurso\mini.png")
print "imagen reducida colores"


#lx, ly, lz = key.shape
#crop_lena = key[lx/3:-lx/3, ly/3:-ly/3]
pl.imshow(key)
pl.show()
print key.shape
key2= key.transpose().flatten()
print "el aplanado es: ",key2.shape
vec=numpy.ones((1))
X=numpy.append(vec,key2)

def verDigito(image):
    fila=image
    fila=fila.reshape(20,20)
    print fila.shape
    pl.imshow(fila.transpose(),cmap="Greys_r")
    pl.show()
print "imagen sinnnnn colors"

verDigito(key2)

#print "x vale: ",X.shape
def algoritmoFP( a):
# for i in range(1, 4):
    z=r['Theta1'].dot(a)
    #print "z vale: ",z.shape
    a=sigmoide(z)
    a=numpy.append(numpy.ones((1)),a)
    #print "a vale: ",a.shape
    z2=r['Theta2'].dot(a)
    #print "z2 vale: ",z2.shape
    a=sigmoide(z2)
    #print "a vale: ",a.shape
    return a
def sigmoide(h):
    return 1. / (1 + numpy.e ** (-h))
#print "aplicacion del algoritmo FP, nos da a: "
 #a[1]=x
aa= algoritmoFP( X)
#print numpy.argmax(aa)+1

def aplanar(t1,t2):
    c=numpy.append(t1.flatten(),t2.flatten())
    return c
print "el titha aplanado es: ",aplanar(r['Theta1'],r['Theta2'])

def armar(p):
    n=25*401
    t1=p[0:n]
    t1=t1.reshape(25,401)
    t2=p[n+1:]
    t2=t2.reshape(10,26)
    return t1,t2
    #ahora puedo calcular h, aplico propagacion asia adelante de una fila para la y y calculo la funcion costooo

Theta = numpy.ones(401)
def funcionCosto(theta,etiqueta):
    aux=(aa==etiqueta)
    m=X.shape[0]#numero de filas
    theta=theta.reshape(401,1)
    h= sigmoide(X.dot(theta))
    regularizacionn=1 /(2.*m)*(theta**2)
    #print aux.transpose().shape
    #print numpy.log(h).shape
    j = -(1. / m) * (aux.transpose().dot(numpy.log(h)) + ( aux-1).transpose().dot(numpy.log(1 - h)))
    j=j.sum()+regularizacionn
    return j.sum()

funcionCosto(Theta,6)



#edificio tecnico, segundo piso, se entra de la puerta de la la paz, ingeniero zeballos a las 3:30