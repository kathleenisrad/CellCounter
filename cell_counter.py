# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#importing things 
import os 
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import imutils
import cv2

#define image paths
infile = 'file path of original image' 
outfile = 'file path of where you want to save the result'

#load image
image = cv2.imread(infile)

#convert to greyscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#thresholding
ret, thresh = cv2.threshold(grey, 49, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#watershed algorithm
D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=20,
	labels=thresh)

markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)

for label in np.unique(labels):
	if label == 0:
		continue
	mask = np.zeros(grey.shape, dtype="uint8")
	mask[labels == label] = 255
	contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)

# draw contours
	drawn = cv2.drawContours(grey, contours, -1, (255,255,255), 1)

#drawing a rectangle in which text will live
x,y,w,h = 0,0,375,75
cv2.rectangle(drawn, (x,x), (x + w, y + h), (0,0,0), -1)

#displaying number of cells in picture    
font                   = cv2.FONT_HERSHEY_DUPLEX
TopLeftCornerOfText = (10,10)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

t = len(np.unique(labels))-1
s = 'number of cells: {0}'.format(t)

cv2.putText(drawn, s, 
    (x + int(w/10), y + int(h/2)), 
    font, 
    fontScale,
    fontColor,
    lineType)

# show the output image
cv2.imshow("result", drawn)

#save the output image
directory = outfile
os.chdir(directory) 
filename = 'output.jpg'
cv2.imwrite(filename, drawn) 
cv2.waitKey(0)