import qrcode
from PIL import Image

def qrcode_generator(dataInput, nameOutput):
    qr = qrcode.QRCode(
        version=1,  # Adjust version for data complexity
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Adjust box size for QR code dimensions
        border=4  # Optional border for visual clarity
    )
    qr.add_data(dataInput)
    qr.make(fit=True)

    qr.make(fit=True)  # Ensure data fits within the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save(nameOutput + ".png")


link = input('Qual o texto que vai ser linkado?\n')
nameImage = input('Qual o nome que devo dar a imagem?\n')

qrcode_generator(link, nameImage)