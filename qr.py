import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def generate_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showerror("Error", "Please enter some data!")
        return

    # Generate QR code
    qr = qrcode.make(data)
    qr.save("qr_code.png")

    # Show QR code
    img = Image.open("qr_code.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x400")
root.resizable(False, False)

tk.Label(root, text="Enter text or URL", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()