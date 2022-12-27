


import cv2
import numpy as np
import matplotlib.pyplot as plt


resim=cv2.imread("kedi.jpg",0)
uzunluk=resim.shape[0]
genislik=resim.shape[1]
max=0
for i in range(uzunluk):
    for j in range(genislik):
        if resim[i][j]>max:
            max=resim[i][j]

ters_resim=max-resim
cv2.imshow("kedi",ters_resim)
cv2.waitKey(0)





