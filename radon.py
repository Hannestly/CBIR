import numpy as np 
import cv2
import matplotlib.pyplot as plt
import math



def getRadon(img,angle,size):
    radonVal = []
    radAngle = np.deg2rad(angle)
    if radAngle == 0:
        for x in range(0, size):
            pVal = 0
            for y in range(0,size):
                pVal += img[y][x]
            radonVal.append(pVal)
    elif radAngle == np.pi*0.5:
        for y in range(0, size):
            pVal = 0
            for x in range(0,size):
                pVal += img[y][x]
            radonVal.append(pVal)
    else:
        p = 0
        maxSize = int(math.sqrt(size**2 + size**2))
        while p < maxSize:
            pVal = 0
            for y in range(0,size):
                x = int( (p - (y*np.sin(radAngle)))/(np.cos(radAngle)))
                if x >= 0 and x < size:
                    pVal += img[y][x]
            radonVal.append(pVal)
            p += 1

    return radonVal



        
if __name__ == '__main__':
    img = cv2.imread('imgforradon/circle.png',0)

    #invering image to focus on black (for demo only)
    imagem = cv2.bitwise_not(img)
    height,width = imagem.shape
    print(height)
    radonTrans = getRadon(imagem,34,height)
    print(radonTrans)
    xaxis = []
    for xaxisVal in range(0,len(radonTrans)):
        xaxis.append(xaxisVal)
    plt.plot(xaxis,radonTrans,'go-',linewidth=1,markersize=1)
    plt.show()

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
