from PIL import Image
import sys

greyscale = list(" .,~:;irsXA253hMHGS#9B&@")#24 ranges of 11 pixels each

if len(sys.argv) != 2:
    print("Usage: ./jpg2ascii.py <image.jpg>")
    sys.exit()
f = sys.argv[1]

img = Image.open(f)
img = img.convert("L") #convert to greyscale

(x,y) = img.size
newsize = (int(x/y*50), 30)
img = img.resize(newsize, Image.ANTIALIAS)

str = ""
for y in range(img.size[1]):
    for x in range(img.size[0]):
        lum = 255-img.getpixel((x,y))
        str += greyscale[(lum//11)]
    str += "\n"

f = open((f.split(".")[0] + ".txt"), "w")
f.write(str)
f.close()