from Parser import Parser
from MemoryHandler import MemoryHandler


if __name__ == '__main__':

    memory_handler = MemoryHandler()
    input_parser = Parser(memory_handler)

    input_parser.parse('help')

    while True:

        action = input('Select action\n')

        input_parser.parse(action)