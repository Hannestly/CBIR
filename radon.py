import numpy as np 
import cv2
import matplotlib.pyplot as plt
import math
import os
import csv



def getIrmaCode(filename):
    name = filename.replace('.png','')
    irmaCode = ''
    with open('irmaSample/irmacode.csv','r') as f:
        reader = csv.reader(f,dialect='excel',delimiter=';')
        for row in reader:
            for column in row:
                if column == name:
                    print(column,row[1])
                    continue
    with open('irmaSample/irmacode2.csv','r') as f:
        reader = csv.reader(f,dialect='excel',delimiter=',')
        for row in reader:
            for column in row:
                if column == name:
                    print(column, row[5])
                    continue



def getRadonAtAngle(img,angle,size):
    radonVal = []
    radAngle = np.deg2rad(angle)
    maxSize = int(math.sqrt(size**2 + size**2))
    #If angle is below 0 or higher or equal to 180, sends an error
    assert(radAngle >= 0 and radAngle < np.pi), "invalid angle"
    #If angle is 0
    if radAngle == 0:
        for x in range(0, size):
            pVal = 0
            for y in range(0,size):
                pVal += img[y][x]
            radonVal.append(pVal)
    #if angle is 90
    elif radAngle == np.pi*0.5:
        for y in range(0, size):
            pVal = 0
            for x in range(0,size):
                pVal += img[y][x]
            radonVal.append(pVal)
    #angle is above 0 and below 90
    elif radAngle > 0 and radAngle < np.pi*0.5:
        p = 0
        while p < maxSize:
            pVal = 0
            for y in range(0,size):
                x = int( (p - (y*np.sin(radAngle)))/(np.cos(radAngle)))
                if x >= 0 and x < size:
                    pVal += img[y][x]
            radonVal.append(pVal)
            p += 1
    #angle is above 90 and below 180
    elif radAngle > np.pi*0.5 and radAngle < np.pi:
        p = int(size*np.cos(radAngle))
        pMax = int(size*np.sin(radAngle))
        while p < pMax:
            pVal = 0
            for y in range(0,size):
                x = int( (p - (y*np.sin(radAngle)))/(np.cos(radAngle)))
                if x>= 0 and x < size:
                    pVal += img[y][x]
            radonVal.append(pVal)
            p += 1        

    return radonVal

def displayRadon(img,segmentAngle,size):
    sumAngle = 0
    while sumAngle < 180:
        radonTrans = getRadonAtAngle(img,sumAngle,size)
        print(radonTrans)
        print(sumAngle)
        xaxis = []

        for xaxisVal in range(0,len(radonTrans)):
            xaxis.append(xaxisVal)
        plt.plot(xaxis,radonTrans,'go-',linewidth=1,markersize=1)
        plt.show()

        sumAngle += segmentAngle
        
if __name__ == '__main__':

    directory = 'irmaSample'
    filepath = 'irmaSample/'

    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            absPath = filepath + filename
            #print(absPath)
            img = cv2.imread(absPath,0)

            #'normalizing' image size
            resizeImg = cv2.resize(img,(512,512))
            resizeHeight,resizeWidth = resizeImg.shape
            
            #print(resizeHeight,resizeWidth)
            getIrmaCode(filename)
            cv2.imshow('image',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            displayRadon(resizeImg,22.5,resizeHeight)

            
        else:
            continue




