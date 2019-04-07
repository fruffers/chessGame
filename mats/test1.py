import tkinter as tkin    
root = tkin.Tk()      
canvas = tkin.Canvas(root, width = 200, height = 200)      
canvas.pack()      
img = tkin.PhotoImage(file="blackSquare.jpg")      
canvas.tkin.create_image(20,20, anchor=NW, image=img)      
mainloop()    
