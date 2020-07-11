import cv2
import numpy as np 
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize
from skimage.filters import (threshold_sauvola)


image = cv2.imread('zdata_latih/alansky.png')

#fungsi grayscale
def grayscale(image):
    grayValue = 0.1140 * image[:,:,2] + 0.5870 * image[:,:,1] + 0.2989 * image[:,:,0]
    gray_img = grayValue.astype(np.uint8)
    return gray_img

#fungsi untuk sauvola thresholding
def thresholding(grayImage): 
    window_size = 25
    thresh_sauvola = threshold_sauvola(grayImage, window_size=window_size)
    binary_sauvola = grayImage < thresh_sauvola
    bool_val = np.array(binary_sauvola)
    bool_val_to_binary = np.multiply(bool_val,1)        
    
    return bool_val_to_binary

#thinning zhang suen

#pemberian jumlah tetangga 
def neighbours(x,y,image):
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1
    return [ img[x_1][y],img[x_1][y1],img[x][y1],img[x1][y1],         # P2,P3,P4,P5
            img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]    # P6,P7,P8,P9
 
# hitung transisi dari 0 ke 1
def transitions(neighbours):
    n = neighbours + neighbours[0:1]      # P2,P3,...,P8,P9,P2
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )  # (P2,P3),(P3,P4),...,(P8,P9),(P9,P2)
 
# proses thinning Zhang-Suen
def zhangSuen(image):
    Image_Thinned = image.copy()  # Making copy to protect original image
    changing1 = changing2 = 1
    while changing1 or changing2:   # Iterates until no further changes occur in the image
        # Step 1
        changing1 = []
        rows, columns = Image_Thinned.shape
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1     and    # Condition 0: Point P1 in the object regions 
                    2 <= sum(n) <= 6   and    # Condition 1: 2<= N(P1) <= 6
                    transitions(n) == 1 and    # Condition 2: S(P1)=1  
                    P2 * P4 * P6 == 0  and    # Condition 3   
                    P4 * P6 * P8 == 0):         # Condition 4
                    changing1.append((x,y))
        for x, y in changing1: 
            Image_Thinned[x][y] = 0
        # Step 2
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 6  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P2 * P4 * P8 == 0 and       # Condition 3
                    P2 * P6 * P8 == 0):            # Condition 4
                    changing2.append((x,y))    
        for x, y in changing2: 
            Image_Thinned[x][y] = 0
    return Image_Thinned

# fungsi untuk segmentasi MSER
def segmentasi(thinnImg,grayImg):
    mser = cv2.MSER_create()
    vis = thinnImg.copy()
    #detect regions in gray scale image
    regions, _ = mser.detectRegions(grayImg)
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    # mask = np.zeros((thinnImg.shape[0], thinnImg.shape[1], 1), dtype=np.uint8)
    i=0 
    for contour in hulls:
        x,y,w,h = cv2.boundingRect(contour)
        if h<120 and (8<w<150):
                cv2.imwrite("data_hasil/"+str(i)+".jpg", grayImg[y:y+h, x:x+w])
                tempImage = cv2.imread("data_hasil/"+str(i)+".jpg")
                resizeImg = cv2.resize(tempImage, (30, 30))                
                cv2.imwrite("data_hasil/"+str(i)+".jpg", resizeImg)
                i=i+1
        cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
    segmen_result_textonly = cv2.bitwise_and(thinnImg, thinnImg, mask=mask)
    return segmen_result_textonly


grayImage       = grayscale(image)
thresImge        = thresholding(grayImage)
# zero            = padding_zeros(thresImge)
thinnImg        = zhangSuen(thresImge)
segmnImg        = segmentasi(thinnImg,grayImage) 

      
# mt = np.savetxt('matrix/matriks thinning 2',np.array(thinnImg),fmt="%s")
# print(thresImge)

plt.figure()
plt.imshow(thresImge, cmap=plt.cm.gray)
plt.title('deteksi MSER')
plt.axis('off')
plt.show()