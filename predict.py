from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pandas as pd
import string
import matplotlib.pyplot as plt
import sys

with open('stylesheet_compare.txt','r') as f:
    sheet=f.read()

class predictWindow(QWidget):
    def __init__(self,products,years,parent=None):
        super(predictWindow,self).__init__(parent)
        self.setMinimumHeight(400)
        self.setMinimumWidth(200)
        self.list_products=products
        self.list_years=years
        self.list_quartile=['q1','q2','q3','q4']
        self.setStyleSheet(sheet)
        self.pred_wind_list=[]
        self.layout_pred=QVBoxLayout()
        self.setupUI()
        self.setLayout(self.layout_pred)

    def setupUI(self):
        self.cb_product=QComboBox()
        self.cb_product.addItems(self.list_products)
        self.cb_years=QComboBox()
        self.cb_years.addItems(self.list_years)
        self.cb_quartile=QComboBox()
        self.cb_quartile.addItems(self.list_quartile)
        self.button_predict=QPushButton("Predict")
        self.layout_pred.addWidget(self.cb_product)
        self.layout_pred.addWidget(self.cb_years)
        self.layout_pred.addWidget(self.cb_quartile)
        self.layout_pred.addWidget(self.button_predict)