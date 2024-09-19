from tkinter import Tk,filedialog,Label,Button
from PIL import Image,ImageTk
import tkinter as tk 

def imageUploader():
    filename = [("Image Files","*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=filename)

    if path:
        img = Image.open(path)
        pic = ImageTk.PhotoImage(img)

        imgLabel.config(image=pic)
        imgLabel.image = pic

        another = logoadd()

        if another:
            
            img = img.convert('RGBA')
            another = another.convert('RGBA')
            logo_width, logo_height = another.size
            main_width, main_height = img.size  

            x_position = main_width - logo_width
            y_position = main_height - logo_height

            img.paste(im=another, box=(x_position, y_position), mask=another)
            img.convert('RGB')
            img.save(path)

def logoadd():

    filename = [("Image Files","*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=filename)

    if path:
        img = Image.open(path)
        img = img.resize((20,20))
        return img

if __name__ == "__main__":

    app = Tk()
    app.title("WaterMark")
    app.geometry("560x500")

    img = ImageTk.PhotoImage(file='E:/portfolio_project/watermark/mbatman.png')
    imgLabel = Label(app,image=img)
    imgLabel.place(x= 1,y=1)

    label = Label(app)
    label.pack(pady=10)

    upload = Button(app,text = "Locate Image",command=imageUploader)
    upload.pack(side=tk.BOTTOM,pady=20)

    app.mainloop()

