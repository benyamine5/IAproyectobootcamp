import cv2 #pip install opencv-contrib-python
import os
cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



Id=input('Ingresa tu id: ')
Datos = 'dataSet/User.'+Id
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)
sampleNum=0
muestra=int(input('Digite la cantidad de muestras que desea tomar: '))
print("Inicializando software por favor posa con tu rostro frente a tu camara y espera que finalice")
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #saving the captured face in the dataset folder
        cv2.imwrite(Datos+"/"+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        sampleNum=sampleNum+1
        cv2.imshow('frame',img)
    # break if the sample number is morethan 20
    if sampleNum>muestra:
        print("Correctamente guardado los datos del ID",Id)
        break
cam.release()
cv2.destroyAllWindows()
