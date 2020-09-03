from Parser import Parser
from MemoryHandler import MemoryHandler


if __name__ == '__main__':

    cars = []
    drivers = []

    memory_handler = MemoryHandler()
    input_parser = Parser(memory_handler)

    while True:

        action = input('Select action (type help for help)\n')

        input_parser.parse(action)