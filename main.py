#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy_dtype import *
from matplotlib import pyplot as plt
global rakam
rakam=0
def nothing(x):
    global rakam
    rakam=x
    print "rakam===>",rakam
    pass

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('sayi1', 'image',1,255,nothing)

baslangicy=20
baslangicx=20


kordinatlar = np.empty( 1, dtype=data_type_kordinatlar)

mesafeler=np.empty( 12, dtype=data_type_mesafeler)

path = np.empty( 1, dtype=data_type_kordinatlar)

tum_kordinatlar = np.empty( 1, dtype=data_type_kordinatlar)
tum_kordinatlar[0]=baslangicx,baslangicy

if __name__ == "__main__":
    print "Merhaba"
    maze=cv2.imread('path.png')
    #maze=cv2.resize(maze,None,fx=0.05, fy=0.05, interpolation = cv2.INTER_CUBIC)

    imgray = cv2.cvtColor(maze,cv2.COLOR_BGR2GRAY)

    binary_image=np.zeros((maze.shape[0],maze.shape[1]),np.uint8)

    demo=binary_image.copy()
    cv2.threshold(imgray,136,255,cv2.THRESH_BINARY_INV,binary_image)
    binary_image[baslangicy,baslangicx]=0
    path['x']=baslangicx
    path['y']=baslangicy

    mesafe=100


    while(mesafe>2):

        cv2.imshow('image',demo)
        k = cv2.waitKey(33)
        if k==1048689:    # 'q' tusu cikmak icin
            break

        kordinatlar= komsular(path[path.shape[0]-1])

        kordinatlar=path_eleme(kordinatlar,path)

        kordinatlar=pixel_eleme(kordinatlar,binary_image)


        for a in range(0,kordinatlar.shape[0]):
            tum_kordinatlar=nokta_ekle3(tum_kordinatlar,kordinatlar[a])

        tum_kordinatlar=path_eleme(tum_kordinatlar,path)



        mesafeler=mesafe_yaz(mesafeler,tum_kordinatlar)



        index= np.where((mesafeler[:]['toplam']==mesafeler[:]['toplam'].min())==True)



        path=nokta_ekle3(path,tum_kordinatlar[index[0][0]])

        print tum_kordinatlar[index[0][0]]

        mesafe= mesafeler[:]['mes_son'].min()

        demo[tum_kordinatlar[index[0][0]]['y'],tum_kordinatlar[index[0][0]]['x']]=255