from pyfiglet import Figlet
# don't forget to install the package on your machine
import sys
import random

# use the module
figlet = Figlet()
# get the list of the fonts
figlets = figlet.getFonts()

if len(sys.argv) == 3:  # check if there are 2 word in the command line
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':  # the first must be -f or --font
        if sys.argv[2] in figlets:  # the 2 must be font name
            font = str(sys.argv[2])  # get the font from the list of fonts
            figlet.setFont(font = font)
            print(figlet.renderText(input('Text: ')))

    sys.exit('Invalid usage')

elif len(sys.argv)==1:  # if no font is provided
    font = random.choice(figlets)  # get a random font from the list of fonts
    figlet.setFont(font = font)
    print(figlet.renderText(input('Text: ')))

sys.exit("Invalid usage")
