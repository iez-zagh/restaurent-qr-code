import zbar
from PIL import Image

def read_qr_code(image_path):
    scanner = zbar.Scanner()
    with open(image_path, 'rb') as image_file:
        image = Image.open(image_file)
        qr_codes = scanner.scan(image)
        for qr_code in qr_codes:
            return qr_code.data.decode('utf-8')

# Example usage
qr_code_data = read_qr_code("loyalty_card_CUSTOMER123.png")
print("QR Code Data:", qr_code_data)
