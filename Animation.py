from tkinter import *
import time

WIDTH=500
HEIGHT=500
xVelocity=1
yVelocity=1

window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background=PhotoImage(file="C:\\Users\\Sahib\\Desktop\\Coding\\Test\\index1.png")
my_image=canvas.create_image(0,0,image=background,anchor=NW)

photo=PhotoImage(file="C:\\Users\\Sahib\\Desktop\\Coding\\Test\\index.png")
my_image=canvas.create_image(0,0,image=photo,anchor=NW)

image_width=photo.width()  
image_height=photo.height()

while True:
    coordinates=canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):  #x ucundur
        xVelocity=-xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):  #y ucundur
        yVelocity=-yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()