#importing the packages
#from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time

# if a video path was not supplied, grab the reference
# to the webcam
vs = VideoStream(src=0).start()

# allow the camera or video file to warm up
time.sleep(1.0)


# keep looping
while True:

	# allow the camera or video file to warm up
	time.sleep(1.2)

	# grab the current frame
	frame = vs.read()

	#Resize da imagem pra 300x300
	img = cv2.resize(frame,(300, 300))
	#Criando uma outra imagem de 10x300 para diminuir o tempo de processamento
	img2 = img[180:190,0:300]

	#Definindo os parâmetos para identificação do branco (Cor em HSV)
	low = (0,0,200)
	up = (150,150,255)
	#Convertendo de BGR para HSV
	hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
	#Aplica a mascara
	# Acho que: Num range da imagem, quando for maior q o minimo e menor que o maximo
	# itera o valor definido como branco
	mask = cv2.inRange(hsv, low, up)
	mask = cv2.erode(mask, None, iterations=1)
	mask = cv2.dilate(mask, None, iterations=6)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_SIMPLE)

	cnts = imutils.grab_contours(cnts)
	pos = []

	for c in cnts:
	    M = cv2.moments(c)
	    if (M["m00"] != 0):
	        p = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	        pos.append(p)

	print('Numero de pontos: ' + str(len(pos)))
	print('Pontos: ' + str(pos))


	# Pegando as duas linhas
	if(len(pos)>1 and len(pos)<=2):
			print(' - Primeiro Ponto = [' + str(pos[0][0]) + ']')
			print(' - Segundo Ponto = [' + str(pos[1][0]) + ']')
			print('Segue o baile')

	if len(pos) == 1 :
		# Pegando a linha da Direita
		if pos[0][0] > 150:
			print('Vai pra esquerda fiadaputa #PT13')

		# Pegando a linha da Esquerda
		if pos[0][0] < 150:
			print('Direita VOLVER #B17')


	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break

		

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF


	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break


cap.release()
cv2.destroyAllWindows()