import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("안녕 친구야!\n네 이름이 뭐야?")
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("확인")
        self.layout().addWidget(my_button)

        def press_it():
            print(my_entry.text())
            my_entry.setText("")
        my_button.clicked.connect(press_it)

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
