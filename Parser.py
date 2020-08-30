import os
import signal


class Parser:
    """
    List of available commands:
        help            shows a list of available commands
        exit            closes the program
    """

    def __init__(self):
        
        pass


    def parse(self, input):

        words = input.split(' ')

        if words[0] == 'help':
            print(self.__doc__)

        elif words[0] == 'exit':
            os.kill(os.getpid(), signal.SIGINT)

        else:
            print('Could not understand input')
        