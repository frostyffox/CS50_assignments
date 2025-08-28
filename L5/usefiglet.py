#*****OK********
import sys
from pyfiglet import Figlet, FigletFont
import random

def fontPick():
    if len(sys.argv) == 1:
        #user wants to output in random font
        fonts = FigletFont.getFonts()
        myfont = random.choice(fonts)

    elif len(sys.argv)==3:
        #user wants to output in specific form
        #sys.argv[1] must be == -f or == "--font"
        if sys.argv[1] not in ("-f","--font"):
            sys.exit("Invalid usage")

        #sys.argv[2] must be == name of a font
        if sys.argv[2] not in FigletFont.getFonts():
            sys.exit("Not a font")
        
        myfont = sys.argv[2]
    else:
        sys.exit()
    
    return myfont
    

def main():
    text = input("Text: ")
    myfont = fontPick()
    f = Figlet(font=myfont)
    print(f.renderText(text))


if __name__ == "__main__":
    main()

