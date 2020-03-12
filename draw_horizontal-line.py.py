#import Pillow (fork of PIL - python image library) to do image stuff
from PIL import Image


#stuff
#x_dimention = 100
#y_dimention = 100

#Function that creates a canvas
#def create_canvas(x_dimention, y_dimention):


    #img = Image.new("1",[x_dimention,y_dimention])


def draw_horizontal_line(start, finish, height):

    x_dimention = 100
    y_dimention = 100
    img = Image.new("1",[x_dimention,y_dimention])
    
    #load the image into memory to make changes to it
    pixels = img.load()

    length = finish - start
    x = start

    pixels[start,height] = (1)
    for i in range(length):
        x = x + 1
        pixels[x,height] = (1)



#create_canvas(100,100)
draw_horizontal_line(10, 90, 50)

#saven the image as a .png file and then close the image
img.save('line.png')
img.close()
