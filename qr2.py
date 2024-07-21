import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=7)
qr.add_data("https://github.com/RadhaIlmulwar/Python-Projects")
qr.make(fit=True)
img=qr.make_image(fill_color="pink",back_color="black")
img.save("Githubprofile_radha.png")
