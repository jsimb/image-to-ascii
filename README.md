# image-to-ascii
A simple python script to turn images into ASCII art.


### Usage:
```bash
$ python3 image-to-ascii.py <image_file> <max_height> <character_height_to_width_ratio>
```
**image_file:** An arbitrary image file, ideally of .jpg or .png format.

**max_height:** The desired height of the ASCII art, expressed in characters.

**character_height_to_width_ratio:** The ratio of height/width of the characters that will compose the ASCII art. The font used should be a *monospace* (fixed-width) font. Usually a value of 2 is fine. In order to determine this ratio, you can proceed as follows:
```
A *square* is created with a few characters, as shown here:
0000000000
0000000000
0000000000
0000000000
0000000000
As you can observe, this *square* is composed of 10 character in width and of only
5 characters in height. The ratio in this case would be 10/5 = **2**.
```

### Example:
```bash
$ python3 image-to-ascii.py image.jpg 30 2
```
This will output a file named *image.txt* containing ASCII art 30 characters tall. It was previously determined that the monospace font used to display the ASCII art allowed twice as much characters in width as it did in height, hence the ratio of 2.
