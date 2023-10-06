import pytesseract
import  matplotlib.pyplot as plt
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread("test.png")

string = pytesseract.image_to_string(image)

image_copy = image.copy()

target_word = 'dog'

data = pytesseract.image_to_data(image , output_type = pytesseract.Output.DICT)

word_occurences = [i for i, word in enumerate(data['text']) if word.lower() == target_word]

for occ in word_occurences:
    w = data['width'][occ]
    h = data['height'][occ]
    l = data['left'][occ]
    t = data['top'][occ]

    p1 = (l,t)
    p2 = (l+w , t)
    p4 = (l,h+t)
    p3 = (l+w , t+h)

    image_copy = cv2.line(image_copy , p1 , p2 , color = (255,0,0) , thickness = 3)
    image_copy = cv2.line(image_copy, p2, p3, color=(255,0,0), thickness=3)
    image_copy = cv2.line(image_copy, p3, p4, color=(255,0,0), thickness=3)
    image_copy = cv2.line(image_copy, p4, p1, color=(255,0,0), thickness=3)


plt.imshow(image_copy)
plt.show()
