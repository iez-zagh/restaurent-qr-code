import tkinter as tk
from tkinter import messagebox
import qrcode
import re

def contains_only_numbers(input_string):
    numeric_pattern = re.compile(r'^\d+$')
    return bool(numeric_pattern.match(input_string))

def generate_qr():
    name = name_entry.get()
    client_number = client_entry.get()

    # Validate inputs
    if not name or not client_number:
        messagebox.showerror("Erreur", "Veuillez saisir votre nom et votre numéro de client.")
        return
    if not contains_only_numbers(client_number):
            messagebox.showerror("Erreur", "Le numéro du client ne contient que des chiffres.")
            return

    # Combine name and client number into a single string
    data = f"Name: {name}, Client Number: {client_number}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="black")

    # Save the image
    img.save("qrcode.png")
    messagebox.showinfo("Success", "QR code generated successfully!")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Create input fields
tk.Label(root, text="Nom et Prenom:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="N de client:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
client_entry = tk.Entry(root)
client_entry.grid(row=1, column=1, padx=5, pady=5)

# Create generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()


# auth_token = '306b3fd4f0641627ea119130910c2a73'