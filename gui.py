import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, qApp
from PyQt5.QtGui import QIcon, QKeySequence


class Lab(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

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

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Lab')
        self.show()

def main():
    app = QApplication(sys.argv)
    lab = Lab()
    sys.exit(app.exec_())

main()
