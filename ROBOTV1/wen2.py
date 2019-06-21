import serial #cargamos la libreria serial
import numpy as np
import cv2
#import robopy as rob

#Iniciamos la comunicacion serial
ser = serial.Serial('com3', 9600)


cap = cv2.VideoCapture(0)
col = int(cap.get(3))
fil = int(cap.get(4))
Objetos = (np.zeros((fil,col),np.uint8))+255
while(cap.isOpened()):
     ret, frame1 = cap.read()
     gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

     gauss = cv2.GaussianBlur(gray1,(3,3),0)
     bordes = cv2.Canny(gauss,150,255)
     kernel = np.ones((10,10),np.uint8)
     mask1 = cv2.morphologyEx(bordes,cv2.MORPH_OPEN,kernel)
     mask2 = cv2.morphologyEx(mask1,cv2.MORPH_CLOSE,kernel)
     mask2 = mask2.astype('uint8')

     (_, contornos,_) = cv2.findContours(bordes.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

     lines = cv2.HoughLinesP(bordes, 1, np.pi/180, 100, minLineLength=10, maxLineGap=10)

     for c in contornos:
        M = cv2.moments(c)

        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*perimeter,True)
        if area > 1000 and area < 5000:
            cx = int(M['m10']/M['m00']) #Coordenada en X
            cy = int(M['m01']/M['m00']) #Coordenadas en Y

            #print("Area {} ".format([c]),"Contorno {} ".format(M),"Cx {}".format(cx),"Cy{}".format(cy))
            print("Cx = {}".format(cx),"Cy = {}".format(cy))
            #print("Area {} ".format([c]),"Contorno {} ".format(M))
            cv2.drawContours(frame1, [c], 0, (0, 255, 0), 1, cv2.LINE_AA)

            Ro = 0
            Az = 255
            Ve = 255
            cv2.rectangle(frame1, (cx,cy), (cx+2,cy+2),(Ro,Az,Ve), 2)
            cv2.drawContours(Objetos, [c], 0, (0, 255, 0), 1, cv2.LINE_AA)

     #for line in lines:
      #  x1, y1, x2, y2 = line[0]
      #  cv2.line(frame1, (x1,y1), (x2,y2), (0,0,255), 1, cv2.LINE_AA)
        #Objetos = (np.zeros((fil,col),np.uint8))+255

     #print("Introduzca Un comando = :")
     #comando = input()
     #print("Comando{}",format(comando))
     #if(col/2 > Cy):
         #cm
      #  ser.write('I')
       # print("Mayor")

     #elsif(col/2<Cy)
      #  ser.write('D')

       # print("Menor")
       #else
         #ser.write(A)
     cv2.imshow('Imagen Bordes',bordes)
     cv2.imshow('Imagen Original',frame1)
     cv2.imshow('Imagen Mascara',Objetos)


     if cv2.waitKey(50) & 0xFF == ord('q'):
        break
colm = cap.get(3)
film = cap.get(4)
print(film)
print(colm)
#print(ret)

cap.release()
cv2.destroyAllWindows()