import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import psutil

def show_cpu_stats():
    usage = psutil.cpu_percent(interval=1)
    label.config(text=f"CPU Usage: {usage}%")

# Create the main window
root = tk.Tk()
root.title("Nikola Tesla and CPU monitors")

# Load and display the image
image_path = "patent 511915.png"  # Replace with your .png file
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Button to check CPU stats
button = tk.Button(root, text="Check CPU", command=show_cpu_stats, bg="black", fg="white")
button_window = canvas.create_window(410, 460, anchor=tk.NW, window=button)

# Label to display CPU usage
label = Label(root, text="CPU Usage: --%", bg="black", fg="white")
label_window = canvas.create_window(460, 510, anchor=tk.NW, window=label)

root.mainloop()
