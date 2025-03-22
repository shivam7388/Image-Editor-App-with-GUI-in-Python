from tkinter import *
from tkinter import ttk, IntVar
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps,ImageDraw, ImageFont
import os
import tkinter as tk
import cv2

import tkinter.filedialog as tk_file


root = Tk()
root.title("Image Editor App")
root.iconbitmap('download.ico')
root.geometry("640x640")
#.config(bg="blue")
opened_image = ""
image_height=0
image_width=0
img18=""
img19=""
bg=PhotoImage(file="back.png")
background_label= Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def select():
    global img_path, img, image_height, image_width
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1
    if img:
        opened_image = ImageTk.PhotoImage(Image.open(img_path))
        image_width = opened_image.width()
        image_height = opened_image.height()


def blur(event):
    global img_path, img1, imgg,img
    for m in range(0, v1.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1


def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 210, image=img3)
        canvas2.image = img3


def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 210, image=img5)
        canvas2.image = img5


def rotate(event):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas2.create_image(300, 210, image=img7)
    canvas2.image = img7


def flip(event):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
       img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
         img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    canvas2.create_image(300, 210, image=img9)
    canvas2.image = img9


def border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill='black')
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image = img11

def flip8(event):
    global img_path, img14, img15
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo5.get() == "COUNTER":
       img14 = img.filter(ImageFilter.CONTOUR)
    elif flip_combo5.get() == "SMOOTH_MORE":
        img14 = img.filter(ImageFilter.SMOOTH_MORE)
    elif flip_combo5.get() == "EMBOSS":
        img14 = img.filter(ImageFilter.EMBOSS)
    elif flip_combo5.get() == "EDGE_ENHANCE":
        img14 = img.filter(ImageFilter.EDGE_ENHANCE)
    elif flip_combo5.get() == "SHARPEN":
        img14 = img.filter(ImageFilter.SHARPEN)
    elif flip_combo5.get() == "DETAIL":
        img14 = img.filter(ImageFilter.DETAIL)
    img15 = ImageTk.PhotoImage(img14)
    canvas2.create_image(300, 210, image=img15)
    canvas2.image = img15

def onButton(e):
     btn1['bg']='blue'
def onButton1(e):
     btn2['bg']='blue'
def onButton2(e):
     btn3['bg']='blue'
def onButton3(e):
    btn4['bg'] = 'blue'
def leaveButton(e):
     btn1['bg']='black'
def leaveButton1(e):
     btn2['bg']='black'
def leaveButton2(e):
     btn3['bg']='black'
def leaveButton3(e):
    btn4['bg'] = 'black'


def colors(event):
    global img_path, img16, img17
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if color_combo8.get() == "DARK":
       for x in range(img.size[0]):
          for y in range(img.size[1]):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (r//2, g//2, b//2))
    elif color_combo8.get() == "LIGHT BLUE":
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                r, g, b = img.getpixel((x, y))
                img.putpixel((x, y), (0, g, b))
    elif color_combo8.get() == "PINK":
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        r, g, b = img.getpixel((x, y))
                        img.putpixel((x,y),(r,0,b))
    elif color_combo8.get() == "YELLOW":
                for x in range(img.size[0]):
                    for y in range(img.size[1]):
                        r, g, b = img.getpixel((x, y))
                        img.putpixel((x,y),(r,g,0))
    img16 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img16)
    canvas2.image = img16

def crop_image(left,top,right,bottom):
    global opened_image,edited_image,img21
    img= Image.open(img_path)
    edited_image = img.crop((left,top,image_width-right,image_height-bottom))
    img21 = ImageTk.PhotoImage(edited_image)
    #image_lb.config(image=img18)
    canvas2.create_image(300, 210, image=img21)
    canvas2.image = img21

def controls_window(w, h):
    #global img_path,image_height,image_width
    controls = tk.Toplevel(root)
    controls.geometry("350x350")
    left_lb = tk.Label(controls, text="left")
    left_lb.pack(anchor=tk.W, pady=5)
    left_scale = tk.Scale(controls, from_=0, to=w, orient=tk.HORIZONTAL,
                          command=lambda x:crop_image(left_scale.get(), top_scale.get(),
                                                       right_scale.get(), bottom_scale.get())
                          )
    left_scale.pack(anchor=tk.W, fill=tk.X)

    right_lb = tk.Label(controls, text="right")
    right_lb.pack(anchor=tk.W, pady=5)
    right_scale = tk.Scale(controls, from_=0, to=w, orient=tk.HORIZONTAL,
                           command=lambda x:crop_image(left_scale.get(),top_scale.get(),
                                                        right_scale.get(),bottom_scale.get()))
    right_scale.pack(anchor=tk.W, fill=tk.X)

    top_to = tk.Label(controls, text="top")
    top_to.pack(anchor=tk.W, pady=5)
    top_scale = tk.Scale(controls, from_=0, to=w, orient=tk.HORIZONTAL,
                         command=lambda x:crop_image(left_scale.get(), top_scale.get(),
                                                      right_scale.get(), bottom_scale.get())
                         )
    top_scale.pack(anchor=tk.W, fill=tk.X)

    bottom_to = tk.Label(controls, text="bottom")
    bottom_to.pack(anchor=tk.W, pady=5)
    bottom_scale = tk.Scale(controls, from_=0, to=w, orient=tk.HORIZONTAL,
                            command=lambda x:crop_image(left_scale.get(), top_scale.get(),
                                                         right_scale.get(), bottom_scale.get())
                            )
    bottom_scale.pack(anchor=tk.W, fill=tk.X)



img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img15 = None
img16 = None
img21 = None

def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[(
        "All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            imgg.save(file)
        elif canvas2.image == img3:
            img2.save(file)
        elif canvas2.image == img5:
            img4.save(file)
        elif canvas2.image == img7:
            img6.save(file)
        elif canvas2.image == img9:
            img8.save(file)
        elif canvas2.image == img11:
            img10.save(file)
        elif canvas2.image == img15:
            img14.save(file)
        elif canvas2.image == img16:
            img.save(file)
        elif canvas2.image == img21:
            edited_image.save(file)

blurr =ttk.Label(root, text="Blur:", font=("TIMES-ROMAN 12 bold"))
blurr.place(x=11, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1,
                   orient=HORIZONTAL, command=blur)
scale1.place(x=125, y=10, height=23, width=100)
bright = ttk.Label(root, text="Brightness:", font=("TIMES-ROMAN 12 bold"))
bright.place(x=11, y=50)
v2 = IntVar()
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2,
                   orient=HORIZONTAL, command=brightness)
scale2.place(x=125, y=50, height=23, width=100)

contrast1 = ttk.Label(root, text="Contrast:", font=("TIMES-ROMAN 12 bold"),)
contrast1.place(x=11, y=92)
v3 = IntVar()
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3,
                   orient=HORIZONTAL, command=contrast)
scale3.place(x=125, y=92, height=23, width=100)

rotate1 = ttk.Label(root, text="Rotate:",font=("TIMES-ROMAN 12 bold"))
rotate1.place(x=250, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, value=values, font=('TIMES-ROMAN 10 bold'))
rotate_combo.place(x=330, y=10,width=100, height=23)
rotate_combo.bind("<<ComboboxSelected>>", rotate)


flip1 = ttk.Label(root, text="Flip:", font=("TIMES-ROMAN 12 bold"))
flip1.place(x=250, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('TIMES-ROMAN 10 bold'))
flip_combo.place(x=330, y=50,width=100,height=23)
flip_combo.bind("<<ComboboxSelected>>", flip)

flip5 = ttk.Label(root, text="Filter:", font=("TIMES-ROMAN 12 bold"))
flip5.place(x=250, y=92)
values5 = ["COUNTER", "SMOOTH_MORE", "EMBOSS" , "EDGE_ENHANCE", "SHARPEN", "DETAIL" ]
flip_combo5 = ttk.Combobox(root, values=values5, font=('TIMES-ROMAN 10 bold'))
flip_combo5.place(x=330, y=92,width=100,height=23)
flip_combo5.bind("<<ComboboxSelected>>", flip8)


border1 = ttk.Label(root, text="Border:", font=("TIMES-ROMAN 12 bold"))
border1.place(x=450, y=8)
values2 = [i for i in range(0, 45, 5)]
border_combo = ttk.Combobox(root, values=values2, font=("TIMES-ROMAN 10 bold"))
border_combo.place(x=530, y=10,width=100,height=23)
border_combo.bind("<<ComboboxSelected>>", border)

color9 = ttk.Label(root, text="Colors:", font=("TIMES-ROMAN 12 bold"))
color9.place(x=450, y=50)
values8 = ["DARK", "LIGHT BLUE","PINK","YELLOW"]
color_combo8 =ttk.Combobox(root, values=values8, font=('TIMES-ROMAN 10 bold'))
color_combo8.place(x=530, y=50,width=100,height=23)
color_combo8.bind("<<ComboboxSelected>>", colors)

# create canvas to display image
canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

# create buttons
btn1 = Button(root, text="Select Image", width=11, bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=select)
btn1.place(x=12, y=595,)
btn1.bind('<Enter>', onButton)
btn1.bind('<Leave>', leaveButton)

btn2 = Button(root, text="Save", width=10, bg='black', fg='gold',
             font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=341, y=595)
btn2.bind('<Enter>', onButton1)
btn2.bind('<Leave>', leaveButton1)


btn3 = Button(root,text="Exit", width=10, bg='black', fg='gold',
              font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=492, y=595)
btn3.bind('<Enter>', onButton2)
btn3.bind('<Leave>', leaveButton2)

btn4 = Button(root, text="Crop", width=12, bg='black', fg='gold',
            font=('ariel 15 bold'), relief=GROOVE, command=lambda:controls_window(w=image_width, h=image_height))
btn4.place(x=168, y=595)
btn4.bind('<Enter>', onButton3)
btn4.bind('<Leave>', leaveButton3)

root.resizable(False, False)
root.mainloop()