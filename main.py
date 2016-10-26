from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import sys
with open('stylesheet.txt','r') as f:
    sheet=f.read()



class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.topUI()
        self.mainUI()
        self.wrap_layout.addWidget(self.top_window)
        self.wrap_layout.addWidget(self.main_window)
        self.setLayout(self.wrap_layout)
        self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        # self.wrap_layout.addLayout(self.main_layout)

    def topUI(self):
        self.top_window = QWidget()
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(100)
        self.top_window.setMaximumHeight(200)
        self.top_window.setStyleSheet(
            "QWidget#topwindow{background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dce6dd, stop: 1 #c8cec8);;}")
        top_layout = QHBoxLayout()
        self.top_search = QLineEdit()
        self.top_search.setMaximumWidth(300)
        self.top_search_button = QPushButton("search")
        self.top_search_button.setCheckable(True)
        self.top_search_button.toggle()
        top_layout.addStretch()
        top_layout.addWidget(self.top_search)
        top_layout.addWidget(self.top_search_button)
        top_layout.addStretch()
        self.top_window.setLayout(top_layout)

    def mainUI(self):
        self.main_window = QWidget()
        self.main_window.setMinimumHeight(300)
        self.main_window.setMinimumWidth(1000)
        self.main_window_layout=QHBoxLayout()
        self.main_leftUI()
        self.main_rightUI()

        self.main_window.setLayout(self.main_window_layout)
        # self.main_window.setStyleSheet("*{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8bf192, stop: 1 #41c34a);}")

    def main_leftUI(self):
        scroll_left_main=QScrollArea()
        scroll_left_main.setWidgetResizable(True)
        self.list_widget=QListWidget()
        self.list_widget.addItem("Item1")
        self.list_widget.addItem("Item1")
        self.list_widget.addItem("Item1")
        self.list_widget.addItem("Item1")
        self.list_widget.addItem("Item1")
        self.list_widget.addItem("Item1")
        scroll_left_main.setMinimumHeight(250)
        scroll_left_main.setMaximumWidth(300)
        self.list_widget.setMinimumWidth(250)
        self.list_widget.setMaximumWidth(300)
        scroll_left_main.setWidget(self.list_widget)
        self.main_window_layout.addWidget(scroll_left_main)

    def main_rightUI(self):
        scroll_area_right=QScrollArea()
        scroll_area_right.setWidgetResizable(True)
        self.main_right=QWidget()
        self.main_right.setMinimumHeight(250)
        self.main_right.setMinimumWidth(600)
        scroll_area_right.setMinimumHeight(250)
        scroll_area_right.setMinimumWidth(600)
        scroll_area_right.setWidget(self.main_right)
        self.main_window_layout.addWidget(scroll_area_right)



app = QApplication(sys.argv)
wind = qWindow()
wind.show()
sys.exit(app.exec_())
