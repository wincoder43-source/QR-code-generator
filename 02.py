import qrcode
from PIL import Image

DATE = "https://play.google.com/store/apps/details?id=com.google.android.youtube"
logo_path = r"D:\PROJECTS\logo.png.png"
qr = qrcode. QRCode(error_correction= qrcode.constants.ERROR_CORRECT_H)
qr.add_data(DATE)
qr.make(fit = True)
img =qr.make_image(fill_color ="#0A0C14FF", back_color ="white").convert('RGB')
logo =Image.open(logo_path)
logo =logo.resize((60,60))
pos = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2
)
img.paste(logo, pos)
img.save("coder.png")
print("success")