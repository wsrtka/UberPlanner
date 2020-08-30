from Parser import Parser


if __name__ == '__main__':

    cars = []
    drivers = []

    input_parser = Parser()

    while True:

        action = input('Select action (type help for help)\n')

        input_parser.parse(action)