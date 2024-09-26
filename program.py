
import numpy as np
import cv2


def import_image(path):
    image = cv2.imread(path)
    return image
     

def process_image(image, x):
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if(x == 1):
        (thresh_value, thresh) = cv2.threshold(gray_image, 160, 255, cv2.THRESH_BINARY)
        
    else:
        ddepth = cv2.CV_32F 
        gradX = cv2.Sobel(gray_image, ddepth=ddepth, dx=1, dy=0, ksize=-1)
        gradY = cv2.Sobel(gray_image, ddepth=ddepth, dx=0, dy=1, ksize=-1)
        edges = cv2.subtract(gradX, gradY)
        edges =  cv2.convertScaleAbs(edges)
        blurred = cv2.blur(edges, (3, 3))
        (thresh_value, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
        

    
                                                                                                                                                                                     
    (conturs, thresh_value) = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    largest = max(conturs, key = cv2.contourArea)  
    rectangle = cv2.minAreaRect(largest)
    box = cv2.boxPoints(rectangle)
    box_int = np.int0(box)
    cv2.drawContours(image, [box_int], -1, (255, 0, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

