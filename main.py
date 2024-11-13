import qrcode
from PIL import Image


# Create a QRCode object with your desired data
qr = qrcode.QRCode(
    version=1,  # Adjust version for data complexity
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Adjust box size for QR code dimensions
    border=4  # Optional border for visual clarity
)
qr.add_data("https://dayvidsantana.netlify.app/")
qr.make(fit=True)

# Load your image
img = Image.open("image.png").convert("RGBA")

# Resize image to fit QR code center area, considering border
img = img.resize((qr.modules_count - 2 * qr.border, qr.modules_count - 2 * qr.border), resample=Image.LANCZOS)



# Combinando QRcode com imagem
# Generate the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white")

# Paste the image onto the QR code
qr_img.paste(img, (qr.border, qr.border))
# Save the combined QR code image
qr_img.save("qrcode_with_image.png")
