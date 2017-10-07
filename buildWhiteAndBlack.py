import cv2


def to_white_and_black1(img_url, output_url):
    img = cv2.imread(img_url, 0)
    ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(output_url, th3)

def to_white_and_black2(img_url,output_url):
    img = cv2.imread(img_url, 0)
    img = cv2.medianBlur(img, 5)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(output_url, th3)