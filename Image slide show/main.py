import tkinter as tk
from tkinter import filedialog
from itertools import cycle
from PIL import Image, ImageTk

class ImageSlideShow:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Slide Show")

        self.label = tk.Label(root)
        self.label.pack()

        # Ask user to select multiple image files
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images for Slide Show",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )

        if not self.image_paths:
            print("No Images Selected")
            root.destroy()
            return

        self.image_cycle = cycle(self.image_paths)
        self.delay = 2000  # 2 seconds
        self.show_next_image()

    def show_next_image(self):
        img_path = next(self.image_cycle)
        image = Image.open(img_path)
        image = image.resize((800, 600))
        photo = ImageTk.PhotoImage(image)

        self.label.config(image=photo)
        self.label.image = photo  # Keep reference to prevent garbage collection

        self.root.after(self.delay, self.show_next_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSlideShow(root)
    root.mainloop()