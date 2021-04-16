import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from indeed.indeed_job_list import main as IndeedJobsSearch

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Indeed job list'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.b = QPushButton(self)
        self.b.setText("search")
        self.b.move(50, 50)
        self.b.clicked.connect(self.printJobs)
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(280,40)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def printJobs(self):
        jobs = IndeedJobsSearch(self.textbox.text(),"Île-de-France",0)
        for i in jobs:
            print(i["title"])
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
