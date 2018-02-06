import pytesseract
from PIL import Image

im = Image.open(r'C:\Users\鹏COMPUTER\Desktop\cc.png')
print(im.format,im.size,im.mode)
text = pytesseract.image_to_string(im)
print("Using image_to_string(): ")
print(text)