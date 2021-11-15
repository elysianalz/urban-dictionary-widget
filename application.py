import dictionary
import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)

class Application(QDialog):
    def __init__(self, parent = None):
        super(Application, self).__init__(parent)
        self.setWindowTitle("Urban Widget")
        self.search = QLineEdit("search word here")
        self.submit = QPushButton("search")
        layout = QVBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.submit)
        self.setLayout(layout)
        self.d = dictionary.Dictionary
        self.submit.clicked.connect(self.start_search)

    def start_search(self):
        word = self.search.text()
        self.d.setWord(self,word)
        self.d.getDefinition(self)

def main():
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
