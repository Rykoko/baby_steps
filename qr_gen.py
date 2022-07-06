import qrcode
from PIL import Image

# im1 = Image.open(r'Cucu.JPG')
# im1.save(r'Cucu.png')


img = qrcode.make('Hey what\'s up!?')

img.save("sample.png")
