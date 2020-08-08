import cv2
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
filename="/zdata_uji/sertifikatuji"
str=filename+"/*.jpg"
mat=io.ImageCollection(str)
img=mat[0]
 ##Create an MSER detector and detect the MSER area of ​​the image
 ##kpkp save the detected keypoint
mser=cv2.MSER_create()
regions,boxes=mser.detectRegions(img)
kpkp=mser.detect(img)
print (len(mser.detect(img)))
 ##Use the red box to frame the detected MSER areas, boxes save the coordinates of the upper left corner of these areas and the width and height of the area
for i in range(len(boxes)):
    x,y,w,h=boxes[i]
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 #Create a SIFT feature extractor
siftt=cv2.xfeatures2d.SIFT_create()
 
print(len(regions))
print(len(boxes))
kp=siftt.detect(img,None)
 ##Calculate the local descriptor of kpkp
des=siftt.compute(img,kpkp)
print(len(des[0]))
 ##Draw these keypoints on the image
cv2.drawKeypoints(img,kpkp,mat[0])
plt.imshow(mat[0])