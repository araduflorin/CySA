import pytesseract
import PIL.Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

myconfig = r"--psm 12 --oem 3"


text=pytesseract.image_to_string(PIL.Image.open("vremea.png"), config=myconfig)

print(text)



