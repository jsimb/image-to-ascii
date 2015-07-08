# Image to ASCII Art
# Created on 7 Jul 2015
# Author: jsimb
#
# Writes a .txt file containing ascii art corresponding to an arbitrary image.
# Tested with python3.

from PIL import Image
import sys

greyscale = list(" -.':rLIVRQ")#11 tonal ranges of 24 pixels each
#greyscale = list(" -.':rLIVXRMWQ@")#15 tonal ranges of 18 pixels each
#greyscale = list(" .,~:;irsXA253hMHGS#9B&@")#24 tonal ranges of ~11 pixels each

if len(sys.argv) != 4:
    print("Usage: ./image-to-ascii.py <image_file> <max_height> <character_height_to_width_ratio>")
    sys.exit()
f, h, r = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])

img = Image.open(f)
img = img.convert("L") #convert to greyscale

(x,y) = img.size
newsize = (int(x/y*h*r), h) #width is r*height, image aspect-ratio is kept
img = img.resize(newsize, Image.ANTIALIAS)

str = ""
for y in range(img.size[1]):
    for x in range(img.size[0]):
        lum = 255-img.getpixel((x,y))
        str += greyscale[(lum//24)]
    str += "\n"

f = open((f.split(".")[0] + ".txt"), "w")
f.write(str)
f.close()
