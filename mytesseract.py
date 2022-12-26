import numpy as np
import cv2 as cv
import pytesseract as tesseract

def tesseract_detect(img):  
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    denoise = cv.fastNlMeansDenoising(gray, h=5) 
    blur = cv.GaussianBlur(denoise,(3,3),0)
    _,thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    text = tesseract.image_to_string(thresh, lang= 'eng', psm=7)
    return text
