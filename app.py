# Import package PySide2 for UI of Application
from PySide2 import QtWidgets, QtCore
# Use this script for import the function get_movies to make it easier
from movie import get_movies
from movie import Movie
# Define the class for display the window
class App(QtWidgets.QWidget):
    # Class Initialization
    def __init__(self):
        # We recovers class parent initialization
        super().__init__()
        # This method define the window title
        self.setWindowTitle("Ciné Club")
        # Here, the method for initialize the widgets of the window
        self.setup_ui()
        # This method is initialize with instance
        self.populate_movie()
        # Method for connect the different actions on the widgets
        self.setup_connections()

    # This method defined the different widget
    def setup_ui(self):
        # this attribute centralizes all widgets for the instance
        self.layoutmain = QtWidgets.QVBoxLayout(self)
        # Widget for the title movie
        self.ln_MovieTitle = QtWidgets.QLineEdit()
        # Widget for the button add
        self.btn_Add = QtWidgets.QPushButton("Add movie")
        # Widget for the view all movies
        self.list_View = QtWidgets.QListWidget()
        # We configure the possibility of choice multiple movies
        self.list_View.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        # Widget for the button remove
        self.btn_Delete = QtWidgets.QPushButton("Remove movie(s)")
        self.date_Calendar = QtWidgets.QCalendarWidget()

        # This method add widget at the layout, one for widget
        self.layoutmain.addWidget(self.ln_MovieTitle)
        self.layoutmain.addWidget(self.date_Calendar)
        self.layoutmain.addWidget(self.btn_Add)
        self.layoutmain.addWidget(self.list_View)
        self.layoutmain.addWidget(self.btn_Delete)

    # This method permit view all movies in the file
    def populate_movie(self):
        # We recovers and register in the variable
        movies = get_movies()
        # Loop for recover the titles of the object
        for movie in movies:
            # We create a widget list item for configure a method for instance a object
            list_movies = QtWidgets.QListWidgetItem(movie.title)
            # Here, we instance object with data in the widget, it's most facility after for different request
            list_movies.setData(QtCore.Qt.UserRole, movie)
            # Add the titles in the widget list_View
            self.list_View.addItem(list_movies)

    # Method for the connections for different widgets
    def setup_connections(self):
        # Connection for add movie with widget
        self.btn_Add.clicked.connect(self.add_movie)
        # Connection for delete the movie(s) on the widget
        self.btn_Delete.clicked.connect(self.remove_movies)
        # Connection on the widget lineEdit when we press return on the keyboard
        self.ln_MovieTitle.returnPressed.connect(self.add_movie)
        # Connection for add the select choice in the list widget at the line edit
        self.list_View.clicked.connect(self.edit_movie)

    # Method for add movie with the widget lineEdit and pushButton add
    def add_movie(self):
        # Variable for the text in the widget for instantiate an object Movie
        movie = self.ln_MovieTitle.text()
        date = self.date_Calendar.selectedDate()
        print(date.getDate())
        # Here, condition for check if widget line edit not null
        if not movie:
            return False
        # Here, instance an object Movie with the widget
        m = Movie(movie)
        # Condition for add movie in the widget and check if it's True
        if m.add_to_movie():
            # If it's True about add movie title directly in the list widget
            # We create a widget list item for configure a method for instance a object
            list_movies = QtWidgets.QListWidgetItem(m.title)
            # Here, we instance object with data in the widget, it's most facility after for different request
            list_movies.setData(QtCore.Qt.UserRole, m)
            # Finally add the title of object
            self.list_View.addItem(list_movies)
            # And clear the widget line edit
            self.ln_MovieTitle.clear()
            return True
        # If no, about return False
        else:
            return False

    # Method for delete the movie(s) with the widget pushButton remove
    def remove_movies(self):
        # Loop for select item in the list widget
        for selected_ite in self.list_View.selectedItems():
            # We recover the item with data who has been discover grace at the methods before setData when add item
            movie = selected_ite.data(QtCore.Qt.UserRole)
            # Here method for remove movie with method of Object
            movie.remove_to_movie()
            # Method for remove the item in the list widget
            self.list_View.takeItem(self.list_View.row(selected_ite))

    # Method for edit movie who select in the list widget directly in line edit
    def edit_movie(self):
        # Loop for select item in the list widget
        for selected_item in self.list_View.selectedItems():
            # Select the title of the movie who has been define in the methods before
            movie = selected_item.data(QtCore.Qt.UserRole)
            # Define the line edit with the select of the list widget
            self.ln_MovieTitle.setText(movie.title)
            # If movie exist in the file
            if movie:
                # Return False for interrupt the process
                return False
            # Otherwise we do add movie grace the method add_movie of the instance
            else:
                self.add_movie()
                return True

# Variable for instantiate a application
app = QtWidgets.QApplication()
# Variable for instantiate a new window
win = App()
# Method for display the window
win.show()
# Method for execute the application
app.exec_()
