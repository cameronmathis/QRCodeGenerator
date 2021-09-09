# QRCodeGenerator.py
import sys
import qrcode

# Read in URL
if len(sys.argv) == 2:
    input_url = sys.argv[1]
    print('Generating QR Code for: ' + input_url )
else:
    print('Error: No URL entered.')
    quit()

# Generate QR Code
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_url)
qr.make(fit=True)

# Save QR Code Image
img = qr.make_image(fill='black', back_color='white')
img.save('QRCode.png')
print('QR Code saved as: QRCode.png')
