import numpy as np 
import matplotlib.pyplot as plt
import cv2 
import skimage as sk
from skimage.io import imread
from skimage.transform import radon, resize


def getBarcode(radonValue,height,width):
    #for row in range(0,width):
    barcode = [1,1]
    for row in range(0,width):
        radonAtRow = radonValue[:,row]
        nonZeroRadon = list(filter(lambda x: x != 0, radonAtRow))
        median = np.median(nonZeroRadon)
        for i in range(0,len(radonAtRow)):
            if radonAtRow[i] > median:
                radonAtRow[i] = 1
            else:
                radonAtRow[i] = 0
        radonAtRow = list(radonAtRow)
        barcode += radonAtRow
    return barcode
    
            
    

if __name__ == '__main__':

    projections = int(input('number of projections:     '))
    theta = np.linspace(0.,180.,projections+1)
    theta = theta[:len(theta)-1]
    
    image = imread('imgforradon/circle.png',as_gray = True)
    image = resize(image,(32,32))
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    radonValue = radon(image,theta=theta)
    print(radonValue)
    height, width = radonValue.shape
    getBarcode(radonValue,height,width)
    #barcode = getBarcode(radonValue, height, width)


#plt.imshow(image)
#plt.show()

''' CV2 version
image = cv2.imread('imgforradon/circle.png',0)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''