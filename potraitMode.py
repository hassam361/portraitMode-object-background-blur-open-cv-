# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:22:01 2019

@author: Hassam Asif
Pakistan, Fast Nuces, Isb 
"""


# Import the cv2 library
import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# Read the image you want connected components of
def show_img(img):
    cv2.imwrite('sds.jpg', img)
    img = cv2.imread('sds.jpg')
    cv2.imshow('sds', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def StichingFromMask(orig_img,masked_img,blurred_img,rects):
    xmin = rects[0]
    ymin = rects[1]
    b_width = rects[2]
    b_height = rects[3]
    xmax = xmin + b_width
    ymax = ymin + b_height
    temp_img=blurred_img.copy()
    
    for x in range(ymin, ymax):
        for y in range(xmin, xmax):
            if masked_img[x][y]==255:
                temp_img[x,y,:] = orig_img[x,y,:]
    return temp_img



# --------------------------------------------------------------------

fileName = 'Persian_155.jpg'
src = cv2.imread(fileName, 0)
col = cv2.imread(fileName, 1)
colorImage=col

show_img(col)
phase1=col
cv2.imwrite('phase1.jpg', col)
img = src

ret, thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# It is extracting the countours array of the largest object detected and then all the 
# calculations are performed over it.
show_img(thresh)
phase2=thresh
cv2.imwrite('phase2.jpg', thresh)
tuple_list=[]
for i in contours:
    tuple_list.append(i.shape[0])
lis=np.array(tuple_list)
max_con=np.argmax(lis)
# now draw the largest contour in white color
img = cv.drawContours(col, contours, max_con, (255, 255, 255), -1)
show_img(img)
phase3=img
cv2.imwrite('phase3.jpg', img)
c_0=contours[max_con]

x, y, w, h = cv2.boundingRect(c_0)
rects=list([x,y,w,h])
img_copy = colorImage.copy()
img_box = cv2.rectangle(img_copy, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 2)

colorImage = cv2.imread(fileName, 1)
blur_img = cv2.GaussianBlur(colorImage,(21,21),0)
gray_mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
col = cv2.imread(fileName, 1)
img_potrait=StichingFromMask(col,gray_mask,blur_img,rects)
show_img(img_potrait)
phase4=img_potrait
cv2.imwrite('phase4.jpg', img_potrait)
col=2
row=2
plt.figure(figsize=[12,12])
plt.subplot(col,row,1), plt.imshow(phase1)
plt.title("Orignal")
plt.subplot(col,row,2), plt.imshow(phase2)
plt.title("Thresholding")
plt.subplot(col,row,3), plt.imshow(phase3)
plt.title("Detecting the largest Contour and masking it")
plt.subplot(col,row,4), plt.imshow(phase4)
plt.title("Guassian blur and stiching the original on blurred image.")
