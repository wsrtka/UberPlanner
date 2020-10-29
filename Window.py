from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QTabWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from screeninfo import get_monitors
from utils import ButtonFactory


class Window(QMainWindow):

    def __init__(self, memory_handler):
        super().__init__()
        
        self.memory_handler = memory_handler
        self.button_factory = ButtonFactory()
        self.title = "UberPlanner"
        
        monitors = get_monitors()
        self.width, self.height = monitors[0].width, monitors[0].height

        self.initUI()


    def initUI(self):
        self.setGeometry(30, 30, self.width - 60, self.height - 60)
        self.create_menu_bar()

        self.create_timetable_tab()
        self.create_drivers_tab()
        self.create_cars_tab()

        self.workspace = QTabWidget()
        self.workspace.addTab(self.timetable_tab, "Grafik")
        self.workspace.addTab(self.drivers_tab, "Kierowcy")
        self.workspace.addTab(self.cars_tab, "Samochody")

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


    def create_timetable_tab(self):
        
        self.timetable_tab = QWidget()
        timetable_tab_layout = QHBoxLayout()

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

        create_timetable_button = QPushButton("Ułóż grafik", self)
        create_timetable_button.clicked.connect(self.create_timetable)

        export_timetable_button = QPushButton("Eksportuj", self)
        export_timetable_button.clicked.connect(self.export_timetable)

        timetable_buttons = QWidget()
        timetable_buttons_layout = QVBoxLayout()

        timetable_buttons_layout.addWidget(create_timetable_button)
        timetable_buttons_layout.addWidget(export_timetable_button)

        timetable_buttons.setLayout(timetable_buttons_layout)

        timetable_tab_layout.addWidget(self.timetable)
        timetable_tab_layout.addWidget(timetable_buttons)

        self.timetable_tab.setLayout(timetable_tab_layout)


    @pyqtSlot()
    def create_timetable(self):
        pass


    @pyqtSlot()
    def export_timetable(self):
        pass

# TODO: add a drivers search field
    def create_drivers_tab(self):
        self.drivers_tab = QWidget()

        drivers_tab_layout = QVBoxLayout()

        create_driver_button = QPushButton('Dodaj kierowcę', self)
        create_driver_button.clicked.connect(self.create_driver)

        drivers_tab_layout.addWidget(create_driver_button)

        for d, driver in enumerate(self.memory_handler.get_drivers()):
            driver_menu = QWidget()
            driver_menu_layout = QHBoxLayout()

            label = QLabel()
            label.setText(str(d + 1) + " \t " + str(driver))
            driver_menu_layout.addWidget(label)

            # TODO: create a button factory

            add_driver_timetable_button = QPushButton('Dodaj grafik', self)
            add_driver_timetable_button.clicked.connect(self.add_driver_timetable)
            driver_menu_layout.addWidget(add_driver_timetable_button)

            change_driver_timetable_button = QPushButton('Edytuj grafik', self)
            change_driver_timetable_button.clicked.connect(self.change_driver_timetable)
            driver_menu_layout.addWidget(change_driver_timetable_button)

            remove_driver_button = QPushButton('Usuń', self)
            remove_driver_button.clicked.connect(self.remove_driver)
            driver_menu_layout.addWidget(remove_driver_button)

            driver_menu.setLayout(driver_menu_layout)

            drivers_tab_layout.addWidget(driver_menu)

        self.drivers_tab.setLayout(drivers_tab_layout)


    @pyqtSlot()
    def create_driver(self):
        pass

    @pyqtSlot()
    def add_driver_timetable(self):
        pass

    @pyqtSlot()
    def change_driver_timetable(self):
        pass

    @pyqtSlot()
    def remove_driver(self):
        pass


    def create_cars_tab(self):
        self.cars_tab = QWidget()

        cars_tab_layout = QVBoxLayout()

        add_car_button = self.button_factory.get_button('Dodaj samochód', self.add_car, parent=self)
        cars_tab_layout.addWidget(add_car_button)

        for c, car in enumerate(self.memory_handler.get_cars()):
            cars_menu = QWidget()
            cars_menu_layout = QHBoxLayout()

            label = QLabel()
            label.setText(str(c + 1) + " \t " + str(car))
            cars_menu_layout.addWidget(label)

            add_car_event_button = self.button_factory.get_button('Dodaj zdarzenie', self.add_car_event, parent=self)
            cars_menu_layout.addWidget(add_car_event_button)

            show_car_timetable_button = self.button_factory.get_button('Podglądnij grafik', self.show_car_timetable, parent=self)
            cars_menu_layout.addWidget(show_car_timetable_button)

            remove_car_button = self.button_factory.get_button('Usuń', self.remove_car, parent=self)
            cars_menu_layout.addWidget(remove_car_button)

            cars_menu.setLayout(cars_menu_layout)

            cars_tab_layout.addWidget(cars_menu)

        self.cars_tab.setLayout(cars_tab_layout)
        

    @pyqtSlot()
    def add_car(self):
        pass

    @pyqtSlot()
    def add_car_event(self):
        pass

    @pyqtSlot()
    def show_car_timetable(self):
        pass

    @pyqtSlot()
    def remove_car(self):
        pass