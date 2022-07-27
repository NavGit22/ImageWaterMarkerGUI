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
label1.grid(column=0, row=0)

# Show image using label
label2 = tk.Label(window, image=folder_img)
label2.grid(column=0, row=1)

# Show Upload button
button_upload = tk.Button(window, text="Upload Images", bg=BLUE, fg=WHITE, highlightthickness=0, command=lambda:upload_file())
button_upload.grid(column=0, row=2, sticky='we')

# Show app name
label5 = tk.Label(window, text="", bg=WHITE)
label5.grid(column=2, row=0)

# Show Entry Box
my_entry = tk.Entry(window, font=("Helvetica", 14))

# Show Add Text Button
button_add = tk.Button(window, text="Add Text", bg=BLUE, fg=WHITE, highlightthickness=0,
                       command=lambda: edit_image())

# Show app name
label4 = tk.Label(window, text="", font=("Helvetica", 24), bg=WHITE, fg=GREEN)
label4.grid(column=4, row=2, columnspan=3)

upload_files = []


def upload_file():
    global img
    label4.config(text="")
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files','*.png')]
    filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
    col = 0  # start from column 3
    row = 4  # start from row 4
    for f in filename:
        upload_files.append(f)
        img = Image.open(f)  # read the image file
        img = img.resize((100, 100))  # new width & height
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(window)
        e1.grid(row=row, column=col)
        e1.image = img
        e1['image'] = img  # garbage collection
        if (col == 3):  # start new line after third column
            row = row + 1  # start with next row
            col = 0  # start with first column
        else:  # within the same row
            col = col + 1  # increase to next column
    label5.config(text="Type Watermarker")
    my_entry.grid(column=2, row=1, columnspan=2)
    button_add.grid(column=2, row=2, columnspan=2)


def edit_image():
    global my_img
    global new_filename

    for f in upload_files:
        # Open the image
        my_img = Image.open(f)

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
    label4.config(text="**File Saved**")


window.mainloop()