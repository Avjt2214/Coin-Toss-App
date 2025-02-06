import tkinter as tk
from PIL import Image, ImageTk
import random

# Function to simulate the coin toss
def coin_toss():
    result = random.choice(['Heads', 'Tails'])
    
    if result == 'Heads':
        coin_image_label.config(image=heads_resized)
    else:
        coin_image_label.config(image=tails_resized)

    result_label.config(text=f"The coin landed on: {result}")

# Set up the main window
root = tk.Tk()
root.title("50/50 Coin Toss©")

# Set up a label to display the result
result_label = tk.Label(root, text="Click the button to toss the coin!", font=("Arial", 16))
result_label.pack(pady=10)

# Load the images for Heads and Tails and resize them
heads_image = Image.open("heads.png")
tails_image = Image.open("tails.png")

# Resize images (adjust width and height as needed)
image_width, image_height = 200, 200  # Resize to 200x200 pixels

# Use LANCZOS (previously called ANTIALIAS) for high-quality image resizing
heads_resized = ImageTk.PhotoImage(heads_image.resize((image_width, image_height), Image.LANCZOS))
tails_resized = ImageTk.PhotoImage(tails_image.resize((image_width, image_height), Image.LANCZOS))

# Set up a label to display the coin image (starts with Heads)
coin_image_label = tk.Label(root, image=heads_resized)
coin_image_label.pack(pady=20)

# Set up a button to trigger the coin toss
toss_button = tk.Button(root, text="Toss the Coin", font=("Arial", 14), command=coin_toss)
toss_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
