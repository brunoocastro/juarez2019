import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/campo1.jpeg', cv2.IMREAD_GRAYSCALE)

##cv2.imshow('Imagem', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100],[80,100], 'r',linewidth=5)
plt.show()
