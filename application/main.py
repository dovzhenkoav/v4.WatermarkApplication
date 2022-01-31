import tkinter as tk
from tkinter import filedialog, StringVar, messagebox
from brain import Brain


YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
ICON = r".\img\ICON.png"


root = tk.Tk()
root.title("Get Watermark")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=ICON))
root.minsize(width=600, height=400)
root.maxsize(width=600, height=400)
root.config(padx=1, pady=1, bg=YELLOW)

logo = tk.Label(text="Get Watermark", fg=GREEN, font=("Gabriola", 60), bg=YELLOW)
logo.grid(column=0, row=0, columnspan=2)

ent1 = tk.Entry(root, font=40, width=66)
ent1.grid(column=0, row=1, columnspan=2)

def browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("PNG", "*.png"), ("JPEG", "*.jpg"), ("All Files", "*.*")))
    ent1.insert(tk.END, filename)

def get_preview():
    brain = Brain(main_image=ent1.get(), watermark_type=switch_variable.get(), watermark_text=text_ent.get(), watermark_image=img_ent.get(), position=img_variable.get())
    brain.get_preview()

def save_image():
    brain = Brain(main_image=ent1.get(), watermark_type=switch_variable.get(), watermark_text=text_ent.get(), watermark_image=img_ent.get(), position=img_variable.get())
    brain.save_image()
    messagebox.showinfo(title='Picture Saved', message='Picture saved in output directory')



b1 = tk.Button(root, text="Find File", font=40, command=browsefunc, height=2, width=15)
b1.grid(column=0, row=2, pady=(30, 10), padx=30, sticky="W")

b2 = tk.Button(root, text="Get Preview", font=40,command=get_preview, height=2, width=15)
b2.grid(column=0, row=3, pady=3, padx=30, sticky="W")

b3 = tk.Button(root, text="Save Ass", font=40, command=save_image, height=2, width=15)
b3.grid(column=0, row=4, pady=3, padx=30, sticky="W")


img_options = tk.Frame(root)
text_options = tk.Frame(root)

def change_to_greet():
   img_options.grid(column=1, row=3)
   text_options.grid_forget()

def change_to_order():
   text_options.grid(column=1, row=3)
   img_options.grid_forget()

change_to_order()

def img_browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("PNG", "*.png"), ("JPEG", "*.jpg"), ("All Files", "*.*")))
    img_ent.insert(tk.END, filename)

img_ent = tk.Entry(img_options, font=40, width=15)
img_ent.grid()

img_btn = tk.Button(img_options, text="Find Image", font=20, command=img_browsefunc, height=1, width=15)
img_btn.grid(column=0, row=2, sticky="ew")

img_variable = StringVar(root)
img_variable.set("Center")

w = tk.OptionMenu(img_options, img_variable, 'Center', 'Top', 'Bottom', 'Left', 'Right', 'Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right')
w.grid(sticky="ew")

text_ent = tk.Entry(text_options, font=40, width=15)
text_ent.insert(tk.END, 'Your Text')
text_ent.grid(sticky="n")

w = tk.OptionMenu(text_options, img_variable, 'Center', 'Top', 'Bottom', 'Left', 'Right', 'Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right')
w.grid(sticky="ew")

switch_frame = tk.Frame(root)
switch_frame.grid(column=1, row=2)
switch_variable = tk.StringVar(value="text")
text_button = tk.Radiobutton(switch_frame, text="Text", variable=switch_variable,
                            indicatoron=False, value="text", width=8, command=change_to_order)
image_button = tk.Radiobutton(switch_frame, text="Image", variable=switch_variable,
                            indicatoron=False, value="image", width=8, command=change_to_greet)

text_button.pack(side="left")
image_button.pack(side="right")


root.mainloop()
