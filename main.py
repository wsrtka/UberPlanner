import sys

from Parser import Parser
from MemoryHandler import MemoryHandler
from Window import Window


if __name__ == '__main__':

    memory_handler = MemoryHandler()
# this code is used to run the CLI of the app
    # input_parser = Parser(memory_handler)

    # input_parser.parse('help')

    # while True:

    #     action = input('Select action\n')

    #     input_parser.parse(action)

    app = Window()
    sys.exit(app.exec_())