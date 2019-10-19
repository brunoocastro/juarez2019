#importing the packages
#from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time

import rospy
from std_msgs.msg import String

tw = 1.5 

#Responsável pela movimentação para a esquerda
def turn_left(perc):
    print('[Movendo para a esquerda com velocidade de {}%]'.format(perc))
    time.sleep(tw)

#Responsável pela movimentação para a direita
def turn_right(perc):
    print('[Movendo para a direita com velocidade de {}%]'.format(perc))
    time.sleep(tw)

def talker(vel):
    pub = rospy.Publisher('robotis/walking/set_params', String, queue_size=10)
    rospy.init_node('vision', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(str(vel))
        rate.sleep()

vs = VideoStream(src=1).start()

time.sleep(1.0)

# keep looping
while True:

    # allow the camera or video file to warm up
    time.sleep(0.1)

    # grab the current frame
    frame = vs.read()

    #Resize da imagem pra 300x300
    img = cv2.resize(frame,(300, 300))
    #Criando uma outra imagem de 10x300 para diminuir o tempo de processamento
    img2 = img[180:190,0:300]

    #Definindo os parâmetos para identificação do branco (Cor em HSV)
    low = (0,0,0)
    up = (110,110,110)

    #low = (0,0,200)
    #up = (150,150,255)

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


    if (len(pos)!=0):

        #pe = pos[(len(pos)-1)][0]
        #pe = pos[0][0]
        pd = np.amax(pos, axis=0)[0]
        #pd = pos[0][0]
        pe = np.amin(pos, axis=0)[0]
        cpd = 300-pd

        diste = 60
        distd = 60

        print('\nNumero de pontos: ' + str(len(pos)))
        print('Pontos: ' + str(pos))
        print('PE (Azul)     = [{}]\nPD (Vermelho) = [{}]\nPEF = [{}]\n'.format(pe,pd,cpd))

        cv2.rectangle(img,(0,150),(300,160),(0,255,0),1)
        cv2.circle(img, (pe, 155), 5, (255,0,0))
        cv2.circle(img, (pd, 155), 4, (0,0,255))

        #Se houver apenas 1 linha na pista
        if len(pos) == 1 :
            # Pegando a linha da Direita
            if pos[0][0] > 150:
                turn_left(60)

            # Pegando a linha da Esquerda
            if pos[0][0] < 150:
                turn_right(60)


        # Pegando as duas linhas
        if len(pos)>1:

            # Se a distância da direita for menor que 60px a partir a extrema direita
            if cpd < diste:
                turn_left(40)

            elif pe < distd:
                turn_right(40)

            else:
                print("Continuar andando")


            '''
                                                if len(pos)==2 :
                                                    print(' - Primeiro Ponto = [' + str(pos[0][0]) + ']')
                                                    print(' - Segundo Ponto = [' + str(pos[1][0]) + ']')
                                                    print('Segue o baile')
                                                if len(pos)>2 :
                                                    for n in range(0,len(pos)):
                                                        print(' - Ponto {} = ['.format(n) + str(pos[n][0]) + ']')
                                    '''

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        break

    # show the frame to our screen
    #cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("IMG", img)

    key = cv2.waitKey(1) & 0xFF


    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()