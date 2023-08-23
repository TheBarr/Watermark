import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

def load_image():
    global image
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.resize((800,600))
    img = ImageTk.PhotoImage(image)
    label.configure(image=img)
    label.image  = img

def add_text_to_image():
    global image_with_text
    image_with_text = image
    draw = ImageDraw.Draw(image_with_text)
    text = wm_input.get()
    font = ImageFont.truetype("arial.ttf", 36)
    text_position = (10, 10)
    text_color = (255, 0, 0) 
    draw.text(text_position, text, font=font, fill=text_color)
    update_display()

def update_display():
    global tk_image_with_text
    tk_image_with_text = ImageTk.PhotoImage(image_with_text)
    label.config(image=tk_image_with_text)

def save_image_with_text():
    if image_with_text:
        img_path = filedialog.asksaveasfilename(title="Select file", initialdir="./img_with_wm/", defaultextension=".png", filetypes=(('PNG', '*.png'),  ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
        image_with_text.save(img_path)    

root = tk.Tk()
root.title("WaterMarker")
root.config(bg='#3A3845')

image_with_text = None
img_path = "img\img_placeholder.png"
image = Image.open(img_path)
image = image.resize((800,600))
img = ImageTk.PhotoImage(image)

label = tk.Label(root, image=img)
label.grid(column=0, row=0, columnspan=3)


upload_img = tk.Button(root, text="Upload IMG", command=load_image)
upload_img.grid(column=0, row=1, sticky='nsew', rowspan=2, padx=10, pady=10)

wm_input = tk.Entry(root)
wm_input.grid(column=1, row=1, sticky='ew', padx=10, pady=10)

wm_button = tk.Button(root, text="Place Watermark", command=add_text_to_image)
wm_button.grid(column=1, row=2, sticky='ew', padx=10, pady=10)

save_button = tk.Button(root, text="Save", command=save_image_with_text)
save_button.grid(column=2, row=1, sticky='nsew', rowspan=2, padx=10, pady=10)


root.mainloop()