from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from screeninfo import get_monitors


class Window(QMainWindow):

    def __init__(self, memory_handler):
        super().__init__()
        
        self.memory_handler = memory_handler
        self.title = "UberPlanner"

        #TODO: 
        # 1. trzeba zrobić żeby po lewej była tabela z samochodami i ich obłożeniem (czyli reprezentująca timetable samochodu)
        # 2. po prawej trzeba dodać listę kierowców z opcjami edycji ich atrybutów
        # 3. dodać przycisk tworzący grafik
        # 4. dodać możliwość eksportowania grafiku
        # 5. ewentualnie dodać zczytywanie z pola tekstowego dyspozycji na kolejny tydzień
        
        monitors = get_monitors()
        self.width, self.height = monitors[0].width, monitors[0].height

        self.initUI()


    def initUI(self):
        self.setGeometry(30, 30, self.width - 60, self.height - 60)
        self.create_menu_bar()

        self.create_timetable()

        self.workspace = QWidget()
        self.workspace_layout = QHBoxLayout()
        self.workspace_layout.addWidget(self.timetable)
        self.workspace.setLayout(self.workspace_layout)

        self.setCentralWidget(self.workspace)

        self.show()


    def create_menu_bar(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('Aplikacja')

        exit_button = QAction(QIcon('exit24.png'), 'Wyjdż', self)
        exit_button.setStatusTip('Wyjście z aplikacji')
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(self.close)

        file_menu.addAction(exit_button)


    def create_timetable(self):
        self.timetable = QTableWidget()
        self.timetable.setRowCount(176)
        self.timetable.setColumnCount(len(self.memory_handler.get_cars()) + 1)

        days_of_the_week = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        hours_of_the_day = [str(h) + ":" + 2 * "0" for h in range(24)] 
        
        for i, car in enumerate(self.memory_handler.get_cars()):
            self.timetable.setItem(0, i + 1, QTableWidgetItem(car.plate))

            for d, day in enumerate(car.timetable.dispositions):
                self.timetable.setItem(d * 25 + 1, i + 1, QTableWidgetItem(days_of_the_week[d]))

                if i == 0:
                    self.timetable.setItem(d * 25 + 1, i, QTableWidgetItem(days_of_the_week[d]))

                for h, hour in enumerate(day):
                    self.timetable.setItem((d * 25) + h + 2, i + 1, QTableWidgetItem(hour if hour else ''))

                    if i == 0:
                        self.timetable.setItem((d * 25) + h + 2, i, QTableWidgetItem(hours_of_the_day[h]))
