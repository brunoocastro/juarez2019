import cv2
import numpy as np
import matplotlib.pyplot as plt

oriimg = cv2.imread('images/campo2.jpeg', cv2.IMREAD_GRAYSCALE)

img = cv2.resize(oriimg,(300, 300))
img2 = img[150:300,0:300]

ret,img3 = cv2.threshold(img2,230,255,cv2.THRESH_BINARY)

tam = img.shape
tam2 = img2.shape
print(tam, '-', tam2)

titles = ['Original Image','Resized Image','Res. and Cropped Image','Threshold']
images = [oriimg, img, img2, img3]

for j in range(0,149,1):
	for i in range(0,149,1):
		#print('{ i = [' + str(i) + "] - " + 'j = [' + str(j) + '] }'),
		if(img3[i][j]>230):
			#cv2.circle(img3, (i,j), 1, (200,200,200))
			#print('{ i = [' + str(i) + "] - " + 'j = [' + str(j) + '] ' + 'Valor Local = [' + str(img[i][j]) + '] }'),
			print('\n[Pintou]')
			#cv2.circle(img2, img2[i,j], 1, 85, thickness=1, lineType=8, shift=0)

for i in range(4):
    plt.subplot(1,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()