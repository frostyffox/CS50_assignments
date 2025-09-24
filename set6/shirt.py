#arg 1 = image in
#arg 2 = image out
import sys
import os
from PIL import Image, ImageOps

def main():
    #check cmd
    if len(sys.argv) != 3:
        sys.exit("Too few or too many arguments!")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    extensions = (".jpg",".png",".jpeg")
    in_ext = os.path.splitext(in_file)[1].lower()
    out_ext = os.path.splitext(out_file)[1].lower()

    if in_ext not in extensions or out_ext not in extensions:
        sys.exit("invalid img format")
    if in_ext != out_ext:
        sys.exit("formats not matching")

    #open input img
    try:
        pic = Image.open(in_file)
    except FileNotFoundError:
        sys.exit("file not found")

    #open shirt img
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    #resize and crop
    pic = ImageOps.fit(pic, shirt.size)

    #overlay
    pic.paste(shirt, shirt)

    #save out img
    pic.save(out_file)

if __name__ == "__main__":
    main()
