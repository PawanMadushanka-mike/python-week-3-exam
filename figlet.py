import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # Random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Set font
    figlet.setFont(font=font)

    # Prompt for input
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
