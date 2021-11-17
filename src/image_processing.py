import cv2


def show(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
