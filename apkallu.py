"""
Author: Henry Keena
Date: 12/28/2022
Description: Main File for Apkallu Translation System
Version: 0.1
"""

from PIL import Image
import cv2
import pytesseract


def main():
    # Simple image to string
    #print(pytesseract.image_to_boxes(Image.open('img/test1.jpg')))
    print(pytesseract.image_to_string(Image.open('img/sampletext.png')))
    

main()
