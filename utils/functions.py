import cv2
import numpy as np
from skimage.util import random_noise

def add_noise(image, option: int):
    if option == 1:
        return random_noise(image, mode ="gaussian")
    elif option == 2:
        return random_noise(image, mode ="s&p")
    elif option == 3:
        return random_noise(image, mode ="poisson")
    elif option == 4:
        return random_noise(image, mode ="speckle")

def remove_noise(image, mode):
    if mode == 1:
        return cv2.GaussianBlur(image, (5,5), 1,0)
    elif mode == 2:
        return cv2.medianBlur(image, 1)
    elif mode == 3:
        return cv2.blur(image, (5,5))
    else:
        print("Wrong choice")
        
def flip_image(image):
    return cv2.flip(image, 1)

def rotate_image(image, angle):
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 190:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    