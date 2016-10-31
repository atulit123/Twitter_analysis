from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys
from compare_show import compareShow

sheet='''
QComboBox {
    border: 1px solid gray;
    border-radius: 3px;
    padding: 1px 18px 1px 3px;
    min-width: 200px;
    max-width:250px;
}

QComboBox:editable {
    background: blue;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}

QPushButton {

	box-shadow: 0px 10px 14px -7px #276873;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #599bb3, stop: 1 #408c99);
	background-color:#599bb3;
	border-radius:8px;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	padding:5px 20px;
	font-weight:bold;
	text-decoration:none;
	text-shadow:0px 1px 0px #3d768a;
	margin-top:20px;
}

QPushButton:hover {
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #408c99, stop: 1 #599bb3);
	background-color:#408c99;
}

QPushButton:pressed {
	top:1px;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #346e78, stop: 1 #22565f);
}

QLabel{
font-size:15px;
padding:5px;
background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ede5a5, stop: 1 #dbd283);
}

'''


class compareWindow(QWidget):
    def __init__(self,data_list,data_ob,parent=None):
        super(compareWindow,self).__init__(parent)
        self.setMinimumHeight(300)
        self.setMinimumWidth(600)
        self.setStyleSheet(sheet)
        self.items=data_list
        self.data_ob=data_ob
        self.comp_wind_list=[]
        self.layout_choose=QHBoxLayout()
        self.leftUI()
        self.rightUI()
        self.setLayout(self.layout_choose)
    def leftUI(self):
        self.left_wid=QWidget()
        self.left_wid.setMinimumWidth(300)
        self.left_layout=QVBoxLayout()
        self.left_layout_items=QVBoxLayout()
        self.left_items_list=[]
        self.left_layout.addLayout(self.left_layout_items)
        self.left_layout.addStretch()
        self.left_wid.setLayout(self.left_layout)
        scroll_area=QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.left_wid)
        self.layout_choose.addWidget(scroll_area)


    def rightUI(self):
        layout=QVBoxLayout()
        self.cb1=QComboBox()
        self.cb1_list=list(self.items)
        self.cb1.addItems(self.cb1_list)
        self.button_compare=QPushButton("Compare")
        self.button_compare.clicked.connect(self.compare_clicked)
        layout.addStretch()
        layout.addWidget(self.cb1)
        layout.addWidget(self.button_compare)
        layout.addStretch()
        self.cb1.activated.connect(self.select_cb1)
        self.layout_choose.addLayout(layout)
        self.lis_w=[]

    def select_cb1(self):
        ob=self.cb1.currentText()
        txt=self.cb1_list[self.cb1_list.index(ob)]
        self.cb1_list.remove(ob)
        self.left_items_list.append(txt)
        self.cb1.clear()
        self.cb1.addItems(self.cb1_list)
        label=QLabel()
        label.setText(ob)
        self.left_layout_items.addWidget(label)

    def compare_clicked(self):
        comp_wind=compareShow(self.left_items_list,self.data_ob)
        self.cb1_list=list(self.items)
        self.left_items_list=[]
        self.cb1.clear()
        self.cb1.addItems(self.cb1_list)
        for i in reversed(range(self.left_layout_items.count())):
            self.left_layout_items.itemAt(i).widget().setParent(None)
        self.comp_wind_list.append(comp_wind)
        comp_wind.show()