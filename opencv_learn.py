import cv2
import numpy as np 
# import matplotlib.pyplot as plt 

# img = cv2.imread(r'C:\Users\99770\Desktop\1.jpg')
# cv2.imshwo('image', img)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([])
# plt.yticks([])
# plt.show()

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5) #起点，终点，颜色，宽度
cv2.rectangle(img, (150, 150), (300, 300), (255, 0, 0), 5)
cv2.circle(img, (150, 150), 50, (255, 0, 0), 5)
cv2.ellipse(img, (256, 256), (150, 50), 0, 0, 360, 255, -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv', (100, 80), font, 4, (255, 255, 255), 3)
cv2.imshow('image', img)
cv2.waitKey(0)

# img = np.zeros((512, 512, 3), np.uint8)
# cv2.imshow('image', img)
# cv2.waitKey(0)
