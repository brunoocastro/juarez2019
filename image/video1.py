import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils




#importing the packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time



#constructing the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())



# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()

# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])

# allow the camera or video file to warm up
time.sleep(1.0)


# keep looping
while True:

	# allow the camera or video file to warm up
	time.sleep(0.2)

	# grab the current frame
	frame = vs.read()

	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
	frame = imutils.resize(frame, width=600)

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break

	greenLower = (35, 70, 46)
	greenUpper = (84, 194, 203)

	radius,x,y = color_radius(frame, greenLower, greenUpper)

	if radius:
		#diameter of the real object
		R = 6.7
		#pixels read diameter object
		P = radius*2

		F = 538

		distance = (R*F)/P
		distance = round(distance, 2)
		print("Distance: "+str(distance)+"cm")

		# draw the circle and centroid on the frame,
		cv2.circle(frame, (int(x), int(y)), int(radius),
			(0, 203, 0), 2)

		font = cv2.FONT_HERSHEY_SIMPLEX
		text = str(distance)+"cm"
		cv2.putText(frame,text, 
		    (int(x),int(y)), 
		    font, 
		    1,
		    (100,255,100),
		    2)

		

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF


	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break



cap.release()
cv2.destroyAllWindows()





captura = cv2.VideoCapture(0)

while(1):
	#Importando imagem
	oriimg = captura.read()
	#Resize da imagem pra 300x300
	img = cv2.resize(np.float32(oriimg),(300, 300))
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
			print('Vai pra esquerda fiadaputa')

		# Pegando a linha da Esquerda
		if pos[0][0] < 150:
			print('Direita VOLVER #B17')


	titles = ['Original Image','Resized Image','Res. and Cropped Image','Threshold']
	images = [oriimg, img, img2, mask]

	for i in range(4):
	    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
	    plt.title(titles[i])
	    plt.xticks([]),plt.yticks([])

	plt.show()

	cv2.imshow("Video", oriimg)

captura.release()
cv2.destroyAllWindows()