import pyfiglet
from termcolor import colored

def wish_holi():

    message = pyfiglet.figlet_format("Happy Holi")
    color = colored(message, color='red')
    print(color)

wish_holi()