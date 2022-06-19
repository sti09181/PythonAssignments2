#########################
##### assignment.py #####
#########################

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QToolButton, QSizePolicy, QLayout, QGridLayout


class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        self.digitButton = [x for x in range(0, 10)]

        for i in range(0, 10):
            self.digitButton[i] = Button(f'{i}', self.buttonClicked)

        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        self.clearButton = Button('C', self.buttonClicked)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)

        digitButtonCoordinate = [0, 2]

        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], digitButtonCoordinate[1], digitButtonCoordinate[0])
            digitButtonCoordinate[0] += 1

            if i % 3 == 0:
                digitButtonCoordinate[1] -= 1
                digitButtonCoordinate[0] = 0

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Calculator')

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
