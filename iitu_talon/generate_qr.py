import qrcode

# Define the URL you want to encode in the QR code
url = "https://iitu.edu.kz/ru/"  # Update this with your desired URL

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
img.save('qr_code.png')

print("QR code saved as qr_code.png")
