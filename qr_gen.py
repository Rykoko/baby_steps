import qrcode
from PIL import Image

# im1 = Image.open(r'Cucu.JPG')
# im1.save(r'Cucu.png')


img = qrcode.make('VAL GIVE ME ATTENTION!!')

img.save("sample.png")
