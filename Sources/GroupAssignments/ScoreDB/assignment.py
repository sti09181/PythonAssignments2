#########################
##### Assignment.py #####
#########################

import sys
import pickle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.dbfilename = "assignment6.dat"
        self.scoredb = []

        self.nameLabel = QLabel("Name:")
        self.nameLineEdit = QLineEdit()

        self.ageLabel = QLabel("Age:")
        self.ageLineEdit = QLineEdit()

        self.scoreLabel = QLabel("Score:")
        self.scoreLineEdit = QLineEdit()

        self.amountLabel = QLabel("Amount:")
        self.amountLineEdit = QLineEdit()

        self.keyLabel = QLabel("Key:")
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItem("Name")
        self.keyComboBox.addItem("Age")
        self.keyComboBox.addItem("Score")

        self.addPushButton = QPushButton("Add")
        self.delPushButton = QPushButton("Del")
        self.findPushButton = QPushButton("Find")
        self.incPushButton = QPushButton("Inc")
        self.showPushButton = QPushButton("Show")

        self.resultLabel = QLabel("Result:")
        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.setReadOnly(True)
        self.resultTextEdit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.resultTextEdit.viewport().setCursor(Qt.ArrowCursor)
        self.resultTextEdit.setFocusPolicy(Qt.NoFocus)

        self.initUI()
        self.readScoreDB()
        self.showScoreDB()
        self.configureEvent()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("Assignment6")

        hbox = [QHBoxLayout()]
        hbox[0].addWidget(self.nameLabel)
        hbox[0].addWidget(self.nameLineEdit)
        hbox[0].addWidget(self.ageLabel)
        hbox[0].addWidget(self.ageLineEdit)
        hbox[0].addWidget(self.scoreLabel)
        hbox[0].addWidget(self.scoreLineEdit)

        hbox.append(QHBoxLayout())
        hbox[1].addStretch()
        hbox[1].addWidget(self.amountLabel)
        hbox[1].addWidget(self.amountLineEdit)
        hbox[1].addWidget(self.keyLabel)
        hbox[1].addWidget(self.keyComboBox)

        hbox.append(QHBoxLayout())
        hbox[2].addStretch()
        hbox[2].addWidget(self.addPushButton)
        hbox[2].addWidget(self.delPushButton)
        hbox[2].addWidget(self.findPushButton)
        hbox[2].addWidget(self.incPushButton)
        hbox[2].addWidget(self.showPushButton)

        hbox.append(QHBoxLayout())
        hbox[3].addWidget(self.resultLabel)
        hbox[3].addStretch()

        hbox.append(QHBoxLayout())
        hbox[4].addWidget(self.resultTextEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox[0])
        vbox.addLayout(hbox[1])
        vbox.addLayout(hbox[2])
        vbox.addLayout(hbox[3])
        vbox.addLayout(hbox[4])

        self.setLayout(vbox)
        self.show()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, "rb")
        except FileNotFoundError:
            self.scoredb = []
            return

        self.scoredb = pickle.load(fH)

        fH.close()

    def addScoreDB(self):
        if self.nameLineEdit.text() == "" or self.ageLineEdit.text() == "" or self.scoreLineEdit.text() == "":
            return

        try:
            if int(float(self.nameLineEdit.text())):
                return
        except ValueError:
            pass

        try:
            record = {"Name": self.nameLineEdit.text()[0].upper() + self.nameLineEdit.text()[1:], "Age": int(self.ageLineEdit.text()), "Score": int(self.scoreLineEdit.text())}
        except ValueError:
            return

        self.scoredb += [record]

        self.scoredb.sort(key=lambda person: person[self.keyComboBox.currentText()])

        self.showScoreDB()
        self.writeScoreDB()

    def delScoreDB(self):
        if self.nameLineEdit.text() == "":
            return

        try:
            if int(float(self.nameLineEdit.text())):
                return
        except ValueError:
            pass

        self.scoredb.sort(key=lambda person: person[self.keyComboBox.currentText()])

        counter = 0

        for dataInScoredb in self.scoredb:
            if dataInScoredb["Name"].lower() == self.nameLineEdit.text().lower():
                counter += 1

        for dummy in range(counter):
            for dataInScoredb in self.scoredb:
                if dataInScoredb["Name"].lower() == self.nameLineEdit.text().lower():
                    self.scoredb.remove(dataInScoredb)
                    break

        self.showScoreDB()
        self.writeScoreDB()

    def findScoreDB(self):
        if self.nameLineEdit.text() == "":
            return

        try:
            if int(float(self.nameLineEdit.text())):
                return
        except ValueError:
            pass

        self.scoredb.sort(key=lambda person: person[self.keyComboBox.currentText()])

        self.resultTextEdit.clear()

        for dataInScoredb in self.scoredb:
            if dataInScoredb["Name"].lower() == self.nameLineEdit.text().lower():
                for attributesInData in sorted(dataInScoredb):
                    self.resultTextEdit.insertPlainText(f"{attributesInData}={dataInScoredb[attributesInData]}\t\t")
                self.resultTextEdit.insertPlainText("\n")

    def incScoreDB(self):
        if self.nameLineEdit.text() == "" or self.amountLineEdit.text() == "":
            return

        try:
            if int(float(self.nameLineEdit.text())):
                return
        except ValueError:
            pass

        self.scoredb.sort(key=lambda person: person[self.keyComboBox.currentText()])

        for dataInScoredb in self.scoredb:
            if dataInScoredb["Name"].lower() == self.nameLineEdit.text().lower():
                try:
                    dataInScoredb["Score"] = int(dataInScoredb["Score"]) + int(self.amountLineEdit.text())
                except ValueError:
                    return

        self.showScoreDB()
        self.writeScoreDB()

    def showScoreDB(self):
        self.scoredb.sort(key=lambda person: person[self.keyComboBox.currentText()])

        self.resultTextEdit.clear()

        for dataInScoredb in self.scoredb:
            for attributesInData in sorted(dataInScoredb):
                self.resultTextEdit.insertPlainText(f"{attributesInData}={dataInScoredb[attributesInData]}\t\t")
            self.resultTextEdit.insertPlainText("\n")

    def configureEvent(self):
        self.addPushButton.clicked.connect(self.addScoreDB)
        self.delPushButton.clicked.connect(self.delScoreDB)
        self.findPushButton.clicked.connect(self.findScoreDB)
        self.incPushButton.clicked.connect(self.incScoreDB)
        self.showPushButton.clicked.connect(self.showScoreDB)

    def writeScoreDB(self):
        fH = open(self.dbfilename, "wb")
        pickle.dump(self.scoredb, fH)
        fH.close()

    def closeEvent(self, event):
        self.writeScoreDB()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
