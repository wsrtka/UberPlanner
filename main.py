import sys, os

from Parser import Parser
from MemoryHandler import MemoryHandler
from Window import Window
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    os.putenv('DISPLAY', ':0.0')

    memory_handler = MemoryHandler()
# this code is used to run the CLI of the app
    # input_parser = Parser(memory_handler)

    # input_parser.parse('help')

    # while True:

    #     action = input('Select action\n')

    #     input_parser.parse(action)

    app = QApplication(sys.argv)
    window = Window(memory_handler)
    sys.exit(app.exec_())