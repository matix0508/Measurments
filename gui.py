import sys
from Measurement import Measurement
from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    QApplication,
    qApp,
    QPushButton,
    QLabel,
    QInputDialog
)
from PyQt5.QtGui import QIcon, QKeySequence


class Lab(QMainWindow):
    def __init__(self):
        super().__init__()

        self.measurements = []
        self.labels = []

        self.initMenu()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Add', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.updateLabels()



        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Lab')
        self.show()

    def updateLabels(self):
        l1 = QLabel("Siema", self)
        l1.move(100, 100)
        if self.measurements:
            lbl = QLabel(str(self.measurements[0].value), self)
            l1 = QLabel("Siema", self)
            l1.move(100, 100)
            lbl.move(100, 120)
        for i, m in enumerate(self.measurements):
            lbl = QLabel(str(m.value), self)
            lbl.move(60, 120+40*i)
            l1 = QLabel("Siema", self)
            l1.move(100, 100)
            self.labels.append(lbl)
            print("sth")

    def initMenu(self):
        exitAct = QAction(QIcon('assets/exit.png'), '&Exit', self)
        exitAct.setShortcut(QKeySequence.Quit)
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        actions = [exitAct]
        for action in actions:
            fileMenu.addAction(exitAct)

        actions = []

    def doAction(self):
        text, ok = QInputDialog.getText(self, 'New Measurement', 'Enter Measurement: ')

        if ok:
            m = Measurement()
            m.value = (float(text))
            print(m)
            self.measurements.append(m)
            self.updateLabels()

def main():
    app = QApplication(sys.argv)
    lab = Lab()
    sys.exit(app.exec_())

main()
