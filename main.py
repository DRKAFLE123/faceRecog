
from PIL import Image, ImageTk
import tkinter as tk

# Load image file
img = Image.open("C:\Users\Damodar Kafle\Pictures.jpg")

# Create Tkinter window
root = tk.Tk()

# Create ImageTk object
img_tk = ImageTk.PhotoImage(img)

# Create label with ImageTk object
label = tk.Label(root, image=img_tk)

# Show label in window
label.pack()

# Start main loop
root.mainloop()
