from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = Image.open("blackSquare.jpg")
photo = ImageTk.PhotoImage(img)

label = Label(image=photo, width=100,height=100)
label.pack()

root.mainloop()
