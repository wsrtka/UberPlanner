from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtGui import QIcon
from screeninfo import get_monitors

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "UberPlanner"
        
        monitors = get_monitors()
        self.width, self.height = monitors[0].width, monitors[0].height

        self.initUI()

    def initUI(self):
        self.setGeometry(30, 30, self.width - 60, self.height - 60)
        self.create_menu_bar()
        self.show()

    def create_menu_bar(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('Aplikacja')

        exit_button = QAction(QIcon('exit24.png'), 'Wyjdż', self)
        exit_button.setStatusTip('Wyjście z aplikacji')
        exit_button.triggered.connect(self.close)

        file_menu.addAction(exit_button)