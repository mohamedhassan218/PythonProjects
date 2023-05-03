"""
    - Create QRCode object and sets its parameters.
    - Specify the image name and the link of information passed from argv.
    - Create the QR Code and save it in the current directory.
"""
import qrcode
from sys import argv

def qr_generator():
    link = argv[1]    
    img_name = argv[2]
    qr = qrcode.QRCode(version=1, box_size=10, border=7)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(img_name + '.png')
    
qr_generator()
    