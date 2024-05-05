from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup  # Import Popup
import qrcode
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC8f97a5a3bdb043ccc31df68a2eef3b51'
auth_token = '306b3fd4f0641627ea119130910c2a73'
client = Client(account_sid, auth_token)

class QRCodeGenerator(App):
    def generate_qr(self, instance):
        name = self.name_input.text
        client_number = self.client_input.text

        # Validate inputs
        if not name or not client_number:
            self.show_error("Error", "Please enter both name and client number.")
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
        img_path = "qrcode.png"
        img.save(img_path)

        # Send the image via WhatsApp using Twilio
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='hello man , test from code',
            # media_url='Your appointment is coming up on July 21 at 3PM',  # Replace 'yourdomain.com' with your actual domain
            to='whatsapp:+212626651561'
        )

        self.show_info("Success", "QR code generated and sent successfully!")

    def show_error(self, title, message):
        popup = MessageBox(title=title, message=message)
        popup.open()

    def show_info(self, title, message):
        popup = MessageBox(title=title, message=message)
        popup.open()

    def build(self):
        layout = BoxLayout(orientation='vertical')

        name_label = Label(text="Name:")
        self.name_input = TextInput()
        client_label = Label(text="Client Number:")
        self.client_input = TextInput()
        generate_button = Button(text="Generate QR Code")
        generate_button.bind(on_press=self.generate_qr)

        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(client_label)
        layout.add_widget(self.client_input)
        layout.add_widget(generate_button)

        return layout

class MessageBox(Popup):  # Ensure MessageBox is a subclass of Popup
    def __init__(self, title, message, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.content = Label(text=message)
        self.size_hint = (None, None)
        self.size = (400, 200)
        self.auto_dismiss = True  # Automatically dismiss the popup when clicking outside of it

if __name__ == '__main__':
    QRCodeGenerator().run()
