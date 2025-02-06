import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import pygame  # Importing the pygame library for sound

class CoinTossApp:
    def __init__(self, root):
        self.root = root
        self.root.title("50/50 Coin Toss")
        self.root.geometry("1020x720")

        # Initialize count for Heads and Tails
        self.heads_count = 0
        self.tails_count = 0

        # Light mode flag
        self.light_mode = True

        # Initialize Pygame for sound
        pygame.mixer.init()
        self.toss_sound = pygame.mixer.Sound("coin_flip.wav")  # Load your sound file here

        # Set up the result label
        self.result_label = tk.Label(root, text="Click the button to toss the coin!", font=("Arial", 16))
        self.result_label.pack(pady=10)

        # Load images and resize them
        heads_image = Image.open("heads.png")
        tails_image = Image.open("tails.png")

        self.image_width, self.image_height = 200, 200  # Set desired image size
        self.heads_resized = ImageTk.PhotoImage(heads_image.resize((self.image_width, self.image_height), Image.LANCZOS))
        self.tails_resized = ImageTk.PhotoImage(tails_image.resize((self.image_width, self.image_height), Image.LANCZOS))

        # Set up a label to display the coin image (initially with Heads)
        self.coin_image_label = tk.Label(root, image=self.heads_resized)
        self.coin_image_label.pack(pady=20)

        # Set up buttons
        self.toss_button = tk.Button(root, text="Toss the Coin", font=("Arial", 14), command=self.animate_coin_toss)
        self.toss_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=self.reset_toss)
        self.reset_button.pack(pady=10)

        # Display toss history
        self.history_label = tk.Label(root, text=f"Heads: {self.heads_count} | Tails: {self.tails_count}", font=("Arial", 12))
        self.history_label.pack(pady=10)

        # Light mode toggle button
        self.toggle_button = tk.Button(root, text="Toggle Light Mode", font=("Arial", 12), command=self.toggle_light_mode)
        self.toggle_button.pack(side=tk.TOP, anchor=tk.N, padx=10, pady=10)  # Position it at the top right corner

        # Initial UI update
        self.update_ui()

    def animate_coin_toss(self):
        # Play the coin toss sound
        self.toss_sound.play()
        
        # Simulate a brief spinning animation (flicking between heads and tails quickly)
        for _ in range(4):
            self.coin_image_label.config(image=self.heads_resized if random.choice([True, False]) else self.tails_resized)
            self.root.update()
            time.sleep(0.05)  # Small delay to simulate animation

        self.coin_toss()  # Perform the actual toss

    def coin_toss(self):
        # Randomly decide the toss outcome
        result = random.choice(['Heads', 'Tails'])
        
        # Update image and count based on result
        if result == 'Heads':
            self.coin_image_label.config(image=self.heads_resized)
            self.heads_count += 1
        else:
            self.coin_image_label.config(image=self.tails_resized)
            self.tails_count += 1

        # Update labels to reflect the result and history
        self.result_label.config(text=f"The coin landed on: {result}")
        self.history_label.config(text=f"Heads: {self.heads_count} | Tails: {self.tails_count}")

    def reset_toss(self):
        # Reset the toss result and counts
        self.heads_count = 0
        self.tails_count = 0
        self.result_label.config(text="Click the button to toss the coin!")
        self.history_label.config(text=f"Heads: {self.heads_count} | Tails: {self.tails_count}")
        self.coin_image_label.config(image=self.heads_resized)  # Reset image to heads

    def toggle_light_mode(self):
        # Toggle the light mode flag
        self.light_mode = not self.light_mode
        self.update_ui()

    def update_ui(self):
        # Update the UI based on the light mode flag
        if self.light_mode:
            self.root.configure(bg='black')
            self.result_label.configure(bg='black', fg='white')
            self.history_label.configure(bg='black', fg='white')
            self.toss_button.configure(bg='gray', fg='white')
            self.reset_button.configure(bg='gray', fg='white')
            self.toggle_button.configure(bg='gray', fg='white')
        else:
            self.root.configure(bg='white')
            self.result_label.configure(bg='white', fg='black')
            self.history_label.configure(bg='white', fg='black')
            self.toss_button.configure(bg='lightgray', fg='black')
            self.reset_button.configure(bg='lightgray', fg='black')
            self.toggle_button.configure(bg='lightgray', fg='black')

# Set up the main application window
root = tk.Tk()
app = CoinTossApp(root)

# Start the GUI event loop
root.mainloop()
