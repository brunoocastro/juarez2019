import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

#Importando imagem
oriimg = cv2.imread('images/campo1.jpeg', cv2.IMREAD_COLOR)
#Resize da imagem pra 300x300
img = cv2.resize(oriimg,(300, 300))
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