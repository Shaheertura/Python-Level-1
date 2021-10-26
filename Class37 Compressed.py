import PIL
from PIL import Image
from tkinter.filedialog import *

openfile = askopenfilename()
img = PIL.Image.open(openfile)
myheight,mywidth = img.size
img = img.resize((myheight,mywidth),Image.ANTIALIAS)
save = asksaveasfilename()
img.save(save+"Compressed.jpg")
