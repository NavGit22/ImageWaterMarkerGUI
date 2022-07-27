import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageFont, ImageDraw
import random
import datetime

WHITE = "#FFFFFF"
BLUE = "#231955"
GREEN = "#7DCE13"

window = tk.Tk()
window.title("Image Watermarking App")
window.minsize(width=800, height=600)
window.config(padx=10, pady=10, bg=WHITE)


# Get the image
folder_img = tk.PhotoImage(file='FolderImage.png')

# Show app name
label1 = tk.Label(window, text="Image Watermarker App", bg=WHITE)
label1.pack()
label1.place(x=350, y=20)

# Show image using label
label2 = tk.Label(window, image=folder_img)
label2.pack()
label2.place(x=345, y=40)

# Show Upload button
button_upload = tk.Button(window, text="Upload Image", bg=BLUE, fg=WHITE, highlightthickness=0, command=lambda:upload_file())
button_upload.pack()
button_upload.place(x=375, y=190)

# Show Entry Box
my_entry = tk.Entry(window, font=("Helvetica", 14))

# Show Add Text Button
button_add = tk.Button(window, text="Add Text", bg=BLUE, fg=WHITE, highlightthickness=0,
                       command=lambda: edit_image())

# Show app name
label4 = tk.Label(window, text="", font=("Helvetica", 24) ,bg=WHITE, fg=GREEN)
label4.pack()
label4.place(x=450, y=300)

upload_files = []


def upload_file():
    global img
    label4.config(text="")
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    upload_files.append(filename)

    img = Image.open(filename)
    resize_image = img.resize((400, 300))
    img = ImageTk.PhotoImage(resize_image)

    label3 = tk.Label(window, image=img)
    label3.pack()
    label3.place(x=0, y=220)

    my_entry.pack()
    my_entry.place(x=450, y=220)

    button_add.pack()
    button_add.place(x=700, y=220)


def edit_image():
    global my_img
    global new_filename

    # Open the image
    my_img = Image.open(upload_files[0])

    # Define The Font
    text_font = ImageFont.truetype("arial.ttf", 8)

    # Get text to add to image
    text_to_add = my_entry.get()
    text_to_add = f"{text_to_add}_{datetime.datetime.now()}"

    # Edit the Image
    edit_images = ImageDraw.Draw(my_img)
    edit_images.text((0, 0), text_to_add, ("green"), font=text_font)

    # new filename
    new_filename = f"Pic_Marked_{random.randint(1,100)}.png"

    # Save The Image
    my_img.save(new_filename)

    # Clear the entry box
    my_entry.delete(0, tk.END)
    my_entry.insert(0, "Saving File...")

    my_entry.delete(0, tk.END)

    upload_files.clear()

    # Show Confirmation
    label4.config(text="**Image Watermarked**")


window.mainloop()