SIMPLE

import qrcode as qr
image = qr.make("https://www.spacex.com/")
# image.save("qr_code.png")
image



CUSTOMIZED

import qrcode 
import PIL as Image
qr = qrcode.QRCode(version= 1,
                   error_correction= qrcode.constants.ERROR_CORRECT_H,
                   box_size = 5,
                   border = 1)

qr.add_data("https://www.spacex.com/")

qr.make(fit = True)
image = qr.make_image(fill_color = "yellow", 
                      back_color = "black")
image.save("image.png")
image
