from pyqrcode import *
from pyzbar import *
from PIL import *

qr= pyqrcode.create("Coding with Himavanth")
qr.png("mycode.png", scale=10)

d=decode(Image.open("mycode.png"))
print(d[0].data.decode("ascii"))