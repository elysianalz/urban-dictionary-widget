import dictionary
import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel)

class Application(QDialog):
    def __init__(self, parent = None):
        super(Application, self).__init__(parent)
        self.setWindowTitle("Urban Widget")
        # widgets
        self.search = QLineEdit()
        self.submit = QPushButton("search")
        self.wordSearched = QLabel()
        self.definitions = QLabel()
        self.examples = QLabel()
        # layout config
        layout = QVBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.submit)
        layout.addWidget(self.wordSearched)
        layout.addWidget(self.definitions)
        layout.addWidget(self.examples)
        self.setLayout(layout)
        self.wordSearched.setWordWrap(True)
        self.definitions.setWordWrap(True)
        self.examples.setWordWrap(True)
        self.submit.clicked.connect(self.start_search)
        # dictionary
        self.d = dictionary.Dictionary

    def start_search(self):
        word = self.search.text()
        self.d.setWord(self,word)
        data = self.d.getDefinition(self)
        self.wordSearched.setText(data[0])
        self.definitions.setText(data[1][0].get_text())
        self.examples.setText(data[2][0].get_text())

def main():
    app = QApplication(sys.argv)
    application = Application()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
