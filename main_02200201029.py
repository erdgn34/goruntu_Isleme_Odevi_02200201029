# Goruntu_isleme_odevi1
# Mustafa Erdogan
# 02200201029



import numpy as np
import cv2
import matplotlib.pyplot as plt
img= cv2.imread("kedi.jpg",0)


hist=np.zeros(256)
(w,h)=img.shape

for v in range (w):
    for u in range (h):
        i =img[v,u]
        hist[i]=hist[i]+1

print(max(hist))

plt.hist(img.ravel(),256,[0,256])
plt.show()







