from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, Tk, Button, Label
import cv2
import numpy as np
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
from deep_translator import (GoogleTranslator,
                             MyMemoryTranslator)

global path_image

image_display_size = 300, 300

def upload_gambar():
    # Step 1.5
    global path_image
    # use the tkinter filedialog library to open the file using a dialog box.
    # obtain the image of the path
    path_image = filedialog.askopenfilename()
    # load the image using the path
    load_image = Image.open(path_image)
    # set the image into the GUI using the thumbnail function from tkinter
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    # load the image as a numpy array for efficient computation and change the type to unsigned integer
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(left_frame, image=render).grid(row=1, column=0, padx=5, pady=5)
    img.place(height=100, width=100)


def detection():
    # Step 2
    global path_image
    global result2

    # load the image
    reader = easyocr.Reader(['en','ko'], gpu=False) 
    result = reader.readtext(path_image)
    result2 = reader.readtext(path_image,detail=0,paragraph=True)
    
    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    img = cv2.imread(path_image)
    spacer = 100
    
    for detection in result: 
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
        spacer+=15

    cv2.imwrite("detected_image.png", img)
    
    # Display the success label.
    Label(left_frame, text="Text Detection Completed!").grid(row=1, column=0, padx=5, pady=5)


def translation():
    # load the image and convert it into a numpy array and display on the GUI.
    load = Image.open("./detected_image.png")
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    
    def listToString(s): 
        str1 = "" 
        for ele in s: 
            str1 += ele  
            return str1 
    
    hasil = listToString(result2)
    txt.insert(1.0, hasil)
    translated = GoogleTranslator(source='ko', target='en').translate(hasil)
    translated2 = MyMemoryTranslator(source='ko', target='en').translate(hasil)
    
    txt2.insert(1.0, translated)
 
app = Tk() 
app.title("Simple Translation Application by Image") 
app.maxsize(900, 600) 
app.config(bg="skyblue") 
 

left_frame = Frame(app, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)
right_frame = Frame(app, width=50, height=50, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)
 

Button(left_frame, text="Choose a Picture", command=upload_gambar).grid(row=0, column=0, padx=5, pady=5)
 

Label(right_frame, text="Korean Version: ").grid(row=0, column=0, padx=5, pady=5)
txt = Text(right_frame, wrap=WORD, width=50, height = 10)
txt.grid(row=1,column=0, padx=5, pady=5)

Label(right_frame, text="English Version: ").grid(row=2, column=0, padx=5, pady=5)
txt2 = Text(right_frame, wrap=WORD, width=50, height = 10)
txt2.grid(row=3,column=0, padx=5, pady=5)

 

tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)
 

Button(tool_bar, text="Extract Text", command=detection).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
Button(tool_bar, text="Translate Text", command=translation).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

 
app.mainloop()