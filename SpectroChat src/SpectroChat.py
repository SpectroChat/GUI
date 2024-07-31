# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:09:03 2023

@author: mtahmed3
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:10:30 2022

@author: mtahmed3
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GA_FS_REG.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
import random
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from math import *
from sklearn.linear_model import LinearRegression
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QMovie
from itertools import combinations
from sklearn import model_selection
from sklearn.cross_decomposition import PLSRegression, PLSSVD
from scipy.signal import savgol_filter #svg
#import xlsxwriter
from pathlib import Path
from scipy.spatial.distance import cdist





class Ui_About(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1221, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/about.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(1070, 630, 141, 141))
        self.home_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QtCore.QSize(200, 200))
        self.home_button.setObjectName("home_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About"))
        
        

class Ui_Instruction(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/instruction_window.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(1130, 600, 151, 121))
        self.home_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QtCore.QSize(200, 200))
        self.home_button.setObjectName("home_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instruction"))





class Ui_OutputWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1275, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/ga.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(0, 0, 1281, 61))
        self.output_label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);")
        self.output_label.setObjectName("output_label")
        self.sel_label = QtWidgets.QLabel(self.centralwidget)
        self.sel_label.setGeometry(QtCore.QRect(0, 60, 371, 91))
        self.sel_label.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label.setObjectName("sel_label")
        self.feat_label = QtWidgets.QListWidget(self.centralwidget)
        self.feat_label.setGeometry(QtCore.QRect(370, 60, 911, 91))
        self.feat_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.feat_label.setObjectName("feat_label")
        self.sel_label_13 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_13.setGeometry(QtCore.QRect(0, 710, 1281, 71))
        self.sel_label_13.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_13.setObjectName("sel_label_13")
        self.sel_label_11 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_11.setGeometry(QtCore.QRect(140, 620, 511, 91))
        self.sel_label_11.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_11.setObjectName("sel_label_11")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(650, 620, 451, 91))
        self.time_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.time_label.setObjectName("time_label")
        self.sel_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_3.setGeometry(QtCore.QRect(0, 360, 151, 91))
        self.sel_label_3.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_3.setObjectName("sel_label_3")
        self.rmsec_label = QtWidgets.QLabel(self.centralwidget)
        self.rmsec_label.setGeometry(QtCore.QRect(150, 360, 151, 91))
        self.rmsec_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rmsec_label.setObjectName("rmsec_label")
        self.sel_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_7.setGeometry(QtCore.QRect(340, 360, 151, 91))
        self.sel_label_7.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_7.setObjectName("sel_label_7")
        self.r2c_label = QtWidgets.QLabel(self.centralwidget)
        self.r2c_label.setGeometry(QtCore.QRect(480, 360, 151, 91))
        self.r2c_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.r2c_label.setObjectName("r2c_label")
        self.sel_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_8.setGeometry(QtCore.QRect(670, 360, 151, 91))
        self.sel_label_8.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_8.setObjectName("sel_label_8")
        self.rmsep_label = QtWidgets.QLabel(self.centralwidget)
        self.rmsep_label.setGeometry(QtCore.QRect(820, 360, 151, 91))
        self.rmsep_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rmsep_label.setObjectName("rmsep_label")
        self.sel_label_9 = QtWidgets.QLabel(self.centralwidget)
        self.sel_label_9.setGeometry(QtCore.QRect(990, 360, 151, 91))
        self.sel_label_9.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.sel_label_9.setObjectName("sel_label_9")
        self.r2p_label = QtWidgets.QLabel(self.centralwidget)
        self.r2p_label.setGeometry(QtCore.QRect(1130, 360, 151, 91))
        self.r2p_label.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.r2p_label.setObjectName("r2p_label")
        
        
        self.mlr_button = QtWidgets.QPushButton(self.centralwidget)
        self.mlr_button.setGeometry(QtCore.QRect(390, 200, 187, 57))
        self.mlr_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.mlr_button.setObjectName("mlr_button")
        
        self.pslr_button = QtWidgets.QPushButton(self.centralwidget)
        self.pslr_button.setGeometry(QtCore.QRect(790, 200, 187, 57))
        self.pslr_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.pslr_button.setObjectName("pslr_button")
        
        
        self.lv_label = QtWidgets.QLabel(self.centralwidget)
        self.lv_label.setGeometry(QtCore.QRect(720, 270, 100, 57))
        self.lv_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.lv_label.setObjectName("lv_label")
        
        
        self.lv_le = QtWidgets.QLineEdit(self.centralwidget)
        self.lv_le.setGeometry(QtCore.QRect(820, 270, 50, 57))
        self.lv_le.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        
        
        self.pslr_run_button = QtWidgets.QPushButton(self.centralwidget)
        self.pslr_run_button.setGeometry(QtCore.QRect(880, 270, 170, 57))
        self.pslr_run_button.setStyleSheet("font: 75 9pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.pslr_run_button.setObjectName("pslr_run_button")
        
        
        
        #Back button to mainpage
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(490, 500, 270, 57))
        self.reset_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb( 255, 174, 66);")
        self.reset_button.setObjectName("reset_button")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Output"))
        self.output_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">OUTPUT SCREEN</span></p></body></html>"))
        self.sel_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SELECTED FEATURES</span></p></body></html>"))
        self.sel_label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Detailed results generated in:</span><span style=\" font-family:\'Eras Bold ITC,sans-serif\'; font-size:9pt; color:#000000;\">“Predictive results_mm-dd-yy_HH-MM.xlsx” </span></p></body></html>"))
        self.sel_label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">EXECUTION TIME (HH:MM:SS)</span></p></body></html>"))
        self.time_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.sel_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">RMSEC</span></p></body></html>"))
        self.rmsec_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.sel_label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">R</span><span style=\" font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-size:12pt; font-weight:600;\">c</span></p></body></html>"))
        self.r2c_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.sel_label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">RMSEP</span></p></body></html>"))
        self.rmsep_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.sel_label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">R</span><span style=\" font-size:12pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-size:12pt; font-weight:600;\">p</span></p></body></html>"))
        self.r2p_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mlr_button.setText(_translate("MainWindow", "MLR"))
        self.pslr_button.setText(_translate("MainWindow", "PLSR"))
        self.pslr_run_button.setText(_translate("MainWindow", "RUN PLSR"))
        self.reset_button.setText(_translate("MainWindow", "RE-ANALYSIS"))
        self.lv_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">LV</span></p></body></html>"))
        self.lv_le.setText(_translate("MainWindow", ""))
        self.lv_label.hide()
        self.lv_le.hide()
        self.pslr_run_button.hide()





class Ui_MainWindow(object):
    
    #temp = now_2.strftime("Predictive results_%m-%d-%y_%H:%M_.xlsx")
    # dd/mm/YY H:M:S
    
    output_filename=""
    partition_file=""
    sample_procedure =""
    time_now = ""
    
    #output_filename=""
    pop=""
    gen=""
    mut=""
    feat=""
    ref="0.0000001"
    cal=""
    pred=""
    rmsec=""
    rmsep=""
    r2c=""
    r2p=""
    time_=""
    feat_list=""
    y=[]
    y_=[]
    yt=[]
    yt_=[]
    selected_list=[]
    cal_pd = None        
    val_pd = None
    total_feat = None
    prerocessing_type = ""
    results = {"Number":[],"Regression":[],"LV":[],"Preprocessing":[],"R2C":[],"RMSEC":[],"R2P":[],"RMSEP":[],"RPD":[],"Feats":[],"Selected feats":[]}
    count_row = 0
    lvs= None
    percent = ""
    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1268, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/genetics.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(1160, 0, 111, 101))
        self.about_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/about2.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.about_button.setIcon(icon)
        self.about_button.setIconSize(QtCore.QSize(300, 100))
        self.about_button.setObjectName("about_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 0, 311, 91))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/logo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.instruction_button = QtWidgets.QPushButton(self.centralwidget)
        self.instruction_button.setGeometry(QtCore.QRect(0, 0, 111, 101))
        self.instruction_button.setStyleSheet("background-image: url(:/icons/instructions.jpg);")
        self.instruction_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/instructions.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.instruction_button.setIcon(icon1)
        self.instruction_button.setIconSize(QtCore.QSize(150, 300))
        self.instruction_button.setObjectName("instruction_button")
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setGeometry(QtCore.QRect(390, 85, 451, 51))
        self.file_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.file_label.setObjectName("file_label")
        self.tr_button = QtWidgets.QPushButton(self.centralwidget)
        self.tr_button.setGeometry(QtCore.QRect(390, 150, 187, 57))
        self.tr_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.tr_button.setObjectName("tr_button")
        self.ts_button = QtWidgets.QPushButton(self.centralwidget)
        self.ts_button.setGeometry(QtCore.QRect(660, 150, 187, 57))
        self.ts_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.ts_button.setObjectName("ts_button")
        
        
        #preprocessing labels
        self.pre_label = QtWidgets.QLabel(self.centralwidget)
        self.pre_label.setGeometry(QtCore.QRect(390, 225, 451, 51))
        self.pre_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pre_label.setObjectName("pre_label")
        
        
        self.raw_button = QtWidgets.QPushButton(self.centralwidget)
        self.raw_button.setGeometry(QtCore.QRect(150, 295, 187, 57))
        self.raw_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.raw_button.setObjectName("raw_button")
        
        
        
        self.msc_button = QtWidgets.QPushButton(self.centralwidget)
        self.msc_button.setGeometry(QtCore.QRect(400, 295, 187, 57))
        self.msc_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.msc_button.setObjectName("msc_button")
        
        
        self.snv_button = QtWidgets.QPushButton(self.centralwidget)
        self.snv_button.setGeometry(QtCore.QRect(650, 295, 187, 57))
        self.snv_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.snv_button.setObjectName("snv_button")
        
        self.sg_button = QtWidgets.QPushButton(self.centralwidget)
        self.sg_button.setGeometry(QtCore.QRect(900, 295, 187, 57))
        self.sg_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.sg_button.setObjectName("sg_button")
        
        self.sgrun_button = QtWidgets.QPushButton(self.centralwidget)
        self.sgrun_button.setGeometry(QtCore.QRect(900, 295, 187, 57))
        self.sgrun_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.sgrun_button.setObjectName("sgrun_button")
        
        
        self.der_label = QtWidgets.QLabel(self.centralwidget)
        self.der_label.setGeometry(QtCore.QRect(1100, 250, 51, 31))
        self.der_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.der_label.setObjectName("der_label")
        self.der_le = QtWidgets.QLineEdit(self.centralwidget)
        self.der_le.setGeometry(QtCore.QRect(1150, 250, 51, 31))
        self.der_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.der_le.setObjectName("der_le")
        
        
        self.poly_label = QtWidgets.QLabel(self.centralwidget)
        self.poly_label.setGeometry(QtCore.QRect(1100, 300, 51, 31))
        self.poly_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.poly_label.setObjectName("poly_label")
        self.poly_le = QtWidgets.QLineEdit(self.centralwidget)
        self.poly_le.setGeometry(QtCore.QRect(1150, 300, 51, 31))
        self.poly_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.poly_le.setObjectName("poly_le")
        
        
        
        self.gap_label = QtWidgets.QLabel(self.centralwidget)
        self.gap_label.setGeometry(QtCore.QRect(1100, 350, 51, 31))
        self.gap_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.gap_label.setObjectName("gap_label")
        self.gap_le = QtWidgets.QLineEdit(self.centralwidget)
        self.gap_le.setGeometry(QtCore.QRect(1150, 350, 51, 31))
        self.gap_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.gap_le.setObjectName("gap_le")
        
        
        
        
        #Ga parameters
        self.files_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.files_label_2.setGeometry(QtCore.QRect(390, 375, 451, 51))
        self.files_label_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.files_label_2.setObjectName("files_label_2")
        self.pop_label = QtWidgets.QLabel(self.centralwidget)
        self.pop_label.setGeometry(QtCore.QRect(150, 440, 150, 51))
        self.pop_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pop_label.setObjectName("pop_label")
        self.pop_le = QtWidgets.QLineEdit(self.centralwidget)
        self.pop_le.setGeometry(QtCore.QRect(305, 440, 71, 51))
        self.pop_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.pop_le.setObjectName("pop_le")
        
        self.gen_label = QtWidgets.QLabel(self.centralwidget)
        self.gen_label.setGeometry(QtCore.QRect(400, 440, 150, 51))
        self.gen_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.gen_label.setObjectName("gen_label")
        self.gen_le = QtWidgets.QLineEdit(self.centralwidget)
        self.gen_le.setGeometry(QtCore.QRect(555, 440, 71, 51))
        self.gen_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.gen_le.setObjectName("gen_le")
        
        
        self.feat_label = QtWidgets.QLabel(self.centralwidget)
        self.feat_label.setGeometry(QtCore.QRect(650, 440, 150, 51))
        self.feat_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.feat_label.setObjectName("feat_label")
        self.feat_le = QtWidgets.QLineEdit(self.centralwidget)
        self.feat_le.setGeometry(QtCore.QRect(805, 440, 71, 51))
        self.feat_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.feat_le.setObjectName("feat_le")
        
        
        
        
        self.mut_label = QtWidgets.QLabel(self.centralwidget)
        self.mut_label.setGeometry(QtCore.QRect(900, 440, 150, 51))
        self.mut_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mut_label.setObjectName("mut_label")
        
     
        """
        self.ref_label = QtWidgets.QLabel(self.centralwidget)
        self.ref_label.setGeometry(QtCore.QRect(1020, 440, 150, 51))
        self.ref_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.ref_label.setObjectName("ref_label")
        self.ref_le = QtWidgets.QLineEdit(self.centralwidget)
        self.ref_le.setGeometry(QtCore.QRect(1178, 440, 90, 51))
        self.ref_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.ref_le.setObjectName("ref_le")
        """
        self.mut_le = QtWidgets.QLineEdit(self.centralwidget)
        self.mut_le.setGeometry(QtCore.QRect(1055, 440, 71, 51))
        self.mut_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.mut_le.setObjectName("mut_le")
        
        
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(580, 520, 100, 100))
        self.run_button.setStyleSheet("background-image: url(:/icons/instructions.jpg);")
        self.run_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/run.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.run_button.setIcon(icon2)
        self.run_button.setIconSize(QtCore.QSize(100, 150))
        self.run_button.setObjectName("run_button")
        self.tr_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tr_button_2.setGeometry(QtCore.QRect(420, 630, 431, 51))
        self.tr_button_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.tr_button_2.setObjectName("Analyze_button")
        #self.tr_button_2.setEnabled(False)
        """
        self.animate_label = QtWidgets.QLabel(self.centralwidget)
        self.animate_label.setGeometry(QtCore.QRect(1110, 610, 150, 101))
        self.animate_label.setStyleSheet("")
        self.animate_label.setText("")
        self.animate_label.setPixmap(QtGui.QPixmap(":/icons/loading2.gif"))
        self.animate_label.setScaledContents(True)
        self.animate_label.setObjectName("animate_label")
        
        """
        ###partitioning 
        self.partition_label = QtWidgets.QLabel(self.centralwidget)
        self.partition_label.setGeometry(QtCore.QRect(900, 150, 150, 57)) #150, 150, 150, 57
        self.partition_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.partition_label.setObjectName("partition_label")
        
        self.partitionbox = QtWidgets.QComboBox(self.centralwidget)
        self.partitionbox.setGeometry(QtCore.QRect(750, 150,177, 57))#300, 150,177, 57
        self.partitionbox.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.partitionbox.addItems(['Random', 'Systematic', 'KS', 'IRS'])
        
        self.partition_button = QtWidgets.QPushButton(self.centralwidget)
        self.partition_button.setGeometry(QtCore.QRect(290, 150, 307, 57))
        self.partition_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.partition_button.setObjectName("partition_button")
        
        self.ownfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.ownfile_button.setGeometry(QtCore.QRect(660, 150, 307, 57))
        self.ownfile_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.ownfile_button.setObjectName("ownfile_button")
        
        self.selectfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectfile_button.setGeometry(QtCore.QRect(150, 150, 250, 57))#500, 150, 177, 57
        self.selectfile_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.selectfile_button.setObjectName("selectfile_button")
        
        
        ###partitioning 
        self.percent_label = QtWidgets.QLabel(self.centralwidget)
        self.percent_label.setGeometry(QtCore.QRect(430, 150, 200, 57)) #700, 150, 120, 57
        self.percent_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.percent_label.setObjectName("percent_label")
        
        self.percent_le = QtWidgets.QLineEdit(self.centralwidget)
        self.percent_le.setGeometry(QtCore.QRect(630, 150, 91, 57))#820, 150, 61, 57
        self.percent_le.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.percent_le.setObjectName("percent_le")
        
        
        self.runsample_button = QtWidgets.QPushButton(self.centralwidget)
        self.runsample_button.setGeometry(QtCore.QRect(927, 150, 150, 57))
        self.runsample_button.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.runsample_button.setObjectName("runsample_button")
        
        
        self.sample_label = QtWidgets.QLabel(self.centralwidget)
        self.sample_label.setGeometry(QtCore.QRect(20, 650, 1280, 71))
        self.sample_label.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\"; align: center;")
        self.sample_label.setObjectName("sample_label")
        MainWindow.setCentralWidget(self.centralwidget)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpectroChat"))
        #self.file_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select Train &amp; Test Files</span></p></body></html>"))
        self.file_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Data partitioning & loading </span></p></body></html>"))
        self.tr_button.setText(_translate("MainWindow", "Train File"))
        self.ts_button.setText(_translate("MainWindow", "Test File"))
        self.selectfile_button.setText(_translate("MainWindow", "Select File"))
        self.partition_button.setText(_translate("MainWindow", "Data partitioning"))
        self.ownfile_button.setText(_translate("MainWindow", "Select partitioned files"))
        self.files_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Input GA Parameters</span></p></body></html>"))
        #preprocessing
        self.pre_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select Preprocessing Method</span></p></body></html>"))
        self.raw_button.setText(_translate("MainWindow", "RAW"))
        self.msc_button.setText(_translate("MainWindow", "MSC"))
        self.snv_button.setText(_translate("MainWindow", "SNV"))
        self.sg_button.setText(_translate("MainWindow", "SG"))
        self.sgrun_button.setText(_translate("MainWindow", "RUN SG"))
        
        self.sgrun_button.hide()
        self.der_label.setText(_translate("MainWindow", "Der"))
        self.poly_label.setText(_translate("MainWindow", "Poly"))
        self.gap_label.setText(_translate("MainWindow", "Gap"))
        self.der_le.setText(_translate("MainWindow", ""))
        self.gap_le.setText(_translate("MainWindow", ""))
        self.poly_le.setText(_translate("MainWindow", ""))
        self.percent_le.setText(_translate("MainWindow", ""))
        self.runsample_button.setText(_translate("MainWindow", "Split"))
        self.runsample_button.hide()
        
        self.der_label.hide()
        self.gap_label.hide()
        self.poly_label.hide()
        self.der_le.hide()
        self.gap_le.hide()
        self.poly_le.hide()
        self.sample_label.hide()
        
        self.percent_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Train#</span></p></body></html>"))
        
        self.pop_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Population</span></p></body></html>"))
        self.pop_le.setText(_translate("MainWindow", ""))
        self.mut_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Mutation</span></p></body></html>"))
        self.feat_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Feature#</span></p></body></html>"))
        self.gen_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Generations</span></p></body></html>"))
        #self.ref_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ref RMSEC</span></p></body></html>"))
        self.feat_le.setText(_translate("MainWindow", ""))
        self.gen_le.setText(_translate("MainWindow", ""))
        self.tr_button_2.setText(_translate("MainWindow", "Analyzing results please wait..."))
        self.tr_button_2.hide()
        self.tr_button_2.setEnabled(False)
        #self.animate_label.hide()
        self.run_button.setEnabled(False)
        self.partition_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Split</span></p></body></html>"))
        self.partitionbox.hide()
        self.partition_label.hide()
        
        
         #instruction page
        self.instruction_button.clicked.connect(self.instruction_window)
        
        #about page
        self.about_button.clicked.connect(self.about_window)
        
        
         #tr and ts file select
        self.ownfile_button.clicked.connect(self.train_test_enable)
        self.partition_button.clicked.connect(self.partition_enable)
        self.selectfile_button.clicked.connect(self.select_enable)
        self.runsample_button.clicked.connect(self.run_sample)
        self.selectfile_button.hide()
        self.tr_button.clicked.connect(self.tr_handler)
        self.ts_button.clicked.connect(self.ts_handler)
        self.tr_button.hide()
        self.ts_button.hide()
        self.percent_label.hide()
        self.percent_le.hide()
        
        ##### Line Edit Inputs ##########
        self.pop_le.editingFinished.connect(self.le_pop)
        self.gen_le.editingFinished.connect(self.le_gen)
        self.mut_le.editingFinished.connect(self.le_mut)
        self.feat_le.editingFinished.connect(self.le_feat)
        self.percent_le.editingFinished.connect(self.le_percent)
        
        
        
        #run button click
        self.raw_button.clicked.connect(self.raw_preprocessing)
        self.msc_button.clicked.connect(self.msc_preprocessing)
        self.snv_button.clicked.connect(self.snv_preprocessing)
        self.sg_button.clicked.connect(self.sg_show)
        self.sgrun_button.clicked.connect(self.sg_preprocessing)
        self.run_button.clicked.connect(self.ga)
        self.tr_button_2.clicked.connect(self.output_window)
        
        
    def le_percent(self):
        self.percent=self.percent_le.text()
        if(self.percent==""):
            self.percent="1"
            self.percent_le.setText(self.percent)
        #self.partition_label.show()
        self.runsample_button.show()
        self.partitionbox.show()
        self.file_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select data partitioning</span></p></body></html>")
    
    def run_sample(self):
        self.sample_procedure = self.partitionbox.currentText()
        self.partitionbox.setEnabled(False)
        self.run_sampling(self.sample_procedure)
        self.selectfile_button.hide()
        self.percent_label.hide()
        self.percent_le.hide()
        self.runsample_button.hide()
        self.partitionbox.hide()
        self.tr_button.show()
        self.ts_button.show()
        self.file_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select Train &amp; Test Files</span></p></body></html>")
        
        self.sample_label.setText(self.sample_procedure+" method performed. Partitioned files generated in Partitioned data folder")
        self.sample_label.show()
        
    def random_sampling(self):
        file=self.partition_file#".csv"
        data = pd.read_csv(file) 
        total_rows =data.shape[0]
        #print("total_rows=",total_rows)
        indices = list(range(0,total_rows))
        num_train_indices = int(self.percent) #int(total_rows*(float(self.percent)/100))
        #print(num_train_indices)
        num_test_indices=total_rows-num_train_indices
        test_indices= random.sample(indices,num_test_indices)
        #print(test_indices,len(test_indices))
        train_indices = list(set(indices)-set(test_indices))
        #print(train_indices,len(train_indices))
        train_data=data.iloc[train_indices,:]
        #print(train_data.shape)
        test_data=data.iloc[test_indices,:]
        
        filepath = Path("Partitioned data/Random_train.csv")  
        tr_ = pd.DataFrame(train_data)
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        tr_.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/Random_test.csv")  
        ts_ = pd.DataFrame(test_data)
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        ts_.to_csv(filepath2,index=False)
    
    def systematic_sampling(self):
        file=self.partition_file#".csv"
        data = pd.read_csv(file) 
        total_rows =data.shape[0]
        #print("total_rows=",total_rows)
        indices = list(range(0,total_rows))
        num_train_indices = int(self.percent) #int(total_rows*(float(self.percent)/100))
        #print(num_train_indices)
        num_test_indices=total_rows-num_train_indices
        #print(num_test_indices)
        step=total_rows//num_test_indices
        test_indices = np.arange(0, total_rows, step=step)
        #print(test_indices, len(test_indices))
        test_indices = test_indices[0:num_test_indices]
        train_indices = list(set(indices)-set(test_indices))
        train_data=data.iloc[train_indices,:]
        #print(train_data.shape)
        test_data=data.iloc[test_indices,:]
        #print(test_data.shape)
        filepath = Path("Partitioned data/Systematic_train.csv")  
        tr_ = pd.DataFrame(train_data)
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        tr_.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/Systematic_test.csv")  
        ts_ = pd.DataFrame(test_data)
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        ts_.to_csv(filepath2,index=False)
        
        
    def kennardstone(self,spectra, test_size=0.25, metric='euclidean', *args, **kwargs):
        """Kennard Stone Sample Split method
        Parameters
        ----------
        spectra: ndarray, shape of i x j
            i spectrums and j variables (wavelength/wavenumber/ramam shift and so on)
        test_size : float, int
            if float, then round(i x (1-test_size)) spectrums are selected as test data, by default 0.25
            if int, then test_size is directly used as test data size
        metric : str, optional
            The distance metric to use, by default 'euclidean'
            See scipy.spatial.distance.cdist for more infomation
        Returns
        -------
        select_pts: list
            index of selected spetrums as train data, index is zero based
        remaining_pts: list
            index of remaining spectrums as test data, index is zero based
        References
        --------
        Kennard, R. W., & Stone, L. A. (1969). Computer aided design of experiments.
        Technometrics, 11(1), 137-148. (https://www.jstor.org/stable/1266770)
        """

        if test_size < 1:
            train_size = round(spectra.shape[0] * (1 - test_size))
        else:
            train_size = spectra.shape[0] - round(test_size)

        if train_size > 2:
            distance = cdist(spectra, spectra, metric=metric, *args, **kwargs)
            select_pts, remaining_pts = self.max_min_distance_split(distance, train_size)
        else:
            raise ValueError("train sample size should be at least 2")

        return select_pts, remaining_pts
    
    def max_min_distance_split(self,distance, train_size):
        """sample set split method based on maximun minimun distance, which is the core of Kennard Stone
        method
        Parameters
        ----------
        distance : distance matrix
            semi-positive real symmetric matrix of a certain distance metric
        train_size : train data sample size
            should be greater than 2
        Returns
        -------
        select_pts: list
            index of selected spetrums as train data, index is zero-based
        remaining_pts: list
            index of remaining spectrums as test data, index is zero-based
        """

        select_pts = []
        remaining_pts = [x for x in range(distance.shape[0])]

        # first select 2 farthest points
        first_2pts = np.unravel_index(np.argmax(distance), distance.shape)
        select_pts.append(first_2pts[0])
        select_pts.append(first_2pts[1])

        # remove the first 2 points from the remaining list
        remaining_pts.remove(first_2pts[0])
        remaining_pts.remove(first_2pts[1])

        for i in range(train_size - 2):
            # find the maximum minimum distance
            select_distance = distance[select_pts, :]
            min_distance = select_distance[:, remaining_pts]
            min_distance = np.min(min_distance, axis=0)
            max_min_distance = np.max(min_distance)

            # select the first point (in case that several distances are the same, choose the first one)
            points = np.argwhere(select_distance == max_min_distance)[:, 1].tolist()
            for point in points:
                if point in select_pts:
                    pass
                else:
                    select_pts.append(point)
                    remaining_pts.remove(point)
                    break
        return select_pts, remaining_pts
        
    def ks_sampling(self):
        file=self.partition_file#".csv"
        data = pd.read_csv(file) 
        total_rows =data.shape[0]
        num_train_indices = int(self.percent)#int(total_rows*(float(self.percent)/100))
        num_test_indices=total_rows-num_train_indices
        test_size = num_test_indices/total_rows
        #print(test_size)
        train_indices,test_indices = self.kennardstone(data.iloc[:,1:], test_size=test_size)
        #print(test_indices)
        
        train_data=data.iloc[train_indices,:]
        #print(train_data.shape)
        test_data=data.iloc[test_indices,:]
        
        filepath = Path("Partitioned data/KS_train.csv")  
        tr_ = pd.DataFrame(train_data)
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        tr_.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/KS_test.csv")  
        ts_ = pd.DataFrame(test_data)
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        ts_.to_csv(filepath2,index=False)
    
    
    def IRS_sampling(self):
        file=self.partition_file#".csv"
        data = pd.read_csv(file) 
        total_rows =data.shape[0]
        #print("total_rows=",total_rows)
        indices = list(range(0,total_rows))
        num_train_indices = int(self.percent) #int(total_rows*(float(self.percent)/100))
        #print(num_train_indices)
        num_test_indices=total_rows-num_train_indices
        
        train_good_indices=[]
        test_good_indices=[]
        
        
    
        
        
        test_indices= random.sample(indices,num_test_indices)
        train_indices = list(set(indices)-set(test_indices))
        train_data=data.iloc[train_indices,:]
        test_data=data.iloc[test_indices,:]
        
        
        
        y1 = train_data['ref']
        X1 = train_data.drop(columns='ref')
        
        X=X1.to_numpy()
        y=y1.to_numpy()
        
        y1test = test_data['ref']
        X1test = test_data.drop(columns='ref')
        
        Xtest=X1test.to_numpy()
        ytest=y1test.to_numpy()
        
        clf_irs = LinearRegression()
        clf_irs.fit(X,y)
        y_=clf_irs.predict(X)
        y_test=clf_irs.predict(Xtest)
        
        msec = mean_squared_error(y, y_)
        msep = mean_squared_error(ytest, y_test)
        obj=(msec+2*msep)/3
     
        train_good_indices=train_indices[:]
        test_good_indices=test_indices[:]
        
        for i in range(0,100):
            test_indices= random.sample(indices,num_test_indices)
            train_indices = list(set(indices)-set(test_indices))
            train_data=data.iloc[train_indices,:]
            test_data=data.iloc[test_indices,:]
            
            
            
            y1 = train_data['ref']
            X1 = train_data.drop(columns='ref')
            
            X=X1.to_numpy()
            y=y1.to_numpy()
            
            y1test = test_data['ref']
            X1test = test_data.drop(columns='ref')
            
            Xtest=X1test.to_numpy()
            ytest=y1test.to_numpy()
            
            clf_irs = LinearRegression()
            clf_irs.fit(X,y)
            y_=clf_irs.predict(X)
            y_test=clf_irs.predict(Xtest)
            
            msec = mean_squared_error(y, y_)
            msep = mean_squared_error(ytest, y_test)
            obj_temp= (msec+2*msep)/3
            if(obj_temp<obj):
                
                obj=obj_temp
                #print(obj)
                train_good_indices=[]
                test_good_indices=[]
                train_good_indices=train_indices[:]
                test_good_indices=test_indices[:]
                #print(test_good_indices)
                
            
            
        
        
        train_good_data=data.iloc[train_good_indices,:]
        test_good_data=data.iloc[test_good_indices,:]
        #print("end",test_good_indices)
        
        filepath = Path("Partitioned data/IRS_train.csv")  
        tr_ = pd.DataFrame(train_good_data)
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        tr_.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/IRS_test.csv")  
        ts_ = pd.DataFrame(test_good_data)
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        ts_.to_csv(filepath2,index=False)
    
    
    def run_sampling(self,string):
        #print(string)
        if(string=="Random"):
            self.random_sampling()
            
        elif(string=="Systematic"):
            self.systematic_sampling()
        
        elif(string=="KS"):
            self.ks_sampling()
            
        elif(string=="IRS"):
            self.IRS_sampling()
        
    
    def train_test_enable(self):
        self.ownfile_button.hide()
        self.partition_button.hide()
        self.tr_button.show()
        self.ts_button.show()
        self.file_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select Train &amp; Test Files</span></p></body></html>")
        
        
    def partition_enable(self):
        self.ownfile_button.hide()
        self.partition_button.hide()
        self.selectfile_button.show()
        self.file_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select unpartitioned file</span></p></body></html>")
        
        
    def select_enable(self):
        
        self.file_label.setText( "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Input number & press enter</span></p></body></html>")
        self.open_dialog_box_select()
        self.percent_label.show()
        self.percent_le.show()
        
        
    def open_dialog_box_select(self):
        filename = QFileDialog.getOpenFileName()
        self.partition_file = filename[0]
         
    def raw_preprocessing(self):
        
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        data = pd.read_csv(cal_file)
        self.cal_pd = data
        X1 = data.drop(columns='ref')
       
        dataT2 = pd.read_csv(pred_file)
        self.val_pd = dataT2
        X1test = dataT2.drop(columns='ref')
        
        #X1 = X1.append(X1test) #whole spectra together
        wl = (X1.columns).astype(float)
        #print(wl)
    
        X = X1.to_numpy()
        Xt = X1test.to_numpy()
        #print(X.shape)
        
        
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        fig2, ax2 = plt.subplots(1)
        ax2.plot(wl, X.T, lw=4)
        ax2.set_xlabel('Wavenumber')
        ax2.set_ylabel('Absorbance/Reflectance')
        ax2.set_title("Original train spectra")
        
        #ax2.legend()
        ax2.grid()
        plt.tight_layout()
        
        fig3, ax3 = plt.subplots(1)
        ax3.plot(wl, Xt.T, lw=4)
        ax3.set_xlabel('Wavenumber')
        ax3.set_ylabel('Absorbance/Reflectance')
        ax3.set_title("Original test spectra")
        #ax2.legend()
        ax3.grid()
        plt.tight_layout()
        plt.show()
        
        
        self.raw_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
        #print(self.val_pd.columns)
        self.prerocessing_type = "RAW"
        
        self.disable_preprocessing()
        
    def msc(self,input_data, reference=None):
        """
            :msc: Scatter Correction technique performed with mean of the sample data as the reference.
            :param input_data: Array of spectral data
            :type input_data: DataFrame
            :returns: data_msc (ndarray): Scatter corrected spectra data
        """
        for i in range(input_data.shape[0]):
            input_data[i,:] -= input_data[i,:].mean()

        # Get the reference spectrum. If not given, estimate it from the mean    
        if reference is None:    
            # Calculate mean
            ref = np.mean(input_data, axis=0)
        else:
            ref = reference

        # Define a new array and populate it with the corrected data    
        data_msc = np.zeros_like(input_data)
        for i in range(input_data.shape[0]):
            # Run regression
            fit = np.polyfit(ref, input_data[i,:], 1, full=True)
            # Apply correction
            data_msc[i,:] = (input_data[i,:] - fit[0][1]) / fit[0][0] 

        return (data_msc)
    
    
    def msc_preprocessing(self):
        
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        data = pd.read_csv(cal_file)
        #self.cal_pd = data
        y = data['ref']
        X1 = data.drop(columns='ref')
        index_len = X1.shape[0]
        #Xm_c = self.msc(X1.to_numpy())
       
        dataT2 = pd.read_csv(pred_file)
        #self.val_pd = dataT2
        ytest = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        #Xm_t = self.msc(X1test.to_numpy())
        
        
        #X1 = X1.append(X1test)
        X1= pd.concat([X1, X1test], ignore_index=True)
        #y = y.append(ytest)
        y= pd.concat([y, ytest], ignore_index=True)
        col = X1.columns
        wl = (X1.columns).astype(float)
        #print(wl)
    
        X = X1.to_numpy()
        Xsnv=self.msc(X) #msc preprocessing
        Xm_c = Xsnv[:index_len]
        Xm_t = Xsnv[index_len:]
        
        
        data_snv = pd.DataFrame(Xsnv, columns = col)
        data_snv['ref'] = y.to_numpy()
        #print(data_snv.head(2))
        #print(data_snv.shape)
        
        
        self.cal_pd = data_snv.iloc[0:index_len,:]
        #print(self.cal_pd.shape)
        
        self.val_pd = data_snv.iloc[index_len:,:]
        #print(self.val_pd.shape)
        
        
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        fig2, ax2 = plt.subplots(1)
        #ax2.plot(wl, Xsnv.T, lw=4)
        ax2.plot(wl, Xm_c.T, lw=4)
        ax2.set_xlabel('Wavenumber')
        ax2.set_ylabel('Absorbance/Reflectance')
        ax2.set_title("MSC Preprocessed Train Spectra")
        #ax2.legend()
        ax2.grid()
        plt.tight_layout()
        
        fig3, ax3 = plt.subplots(1)
        #ax2.plot(wl, Xsnv.T, lw=4)
        ax3.plot(wl, Xm_t.T, lw=4)
        ax3.set_xlabel('Wavenumber')
        ax3.set_ylabel('Absorbance/Reflectance')
        ax3.set_title("MSC Preprocessed Test Spectra")
        #ax2.legend()
        ax3.grid()
        plt.tight_layout()
        plt.show()
        
        
        
        #new added to generate csv files
        
        filepath = Path("Partitioned data/msc_train.csv")  
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        self.cal_pd.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/msc_test.csv")  
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        self.val_pd.to_csv(filepath2,index=False)
        
        
        
        
        self.msc_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
        #print(self.val_pd.columns)
        
        self.disable_preprocessing()
        self.prerocessing_type = "MSC"
        
    
    def snv(self,input_data):
      
        # Define a new array and populate it with the corrected data  
        output_data = np.zeros_like(input_data)
        for i in range(input_data.shape[0]):
     
            # Apply correction
            output_data[i,:] = (input_data[i,:] - np.mean(input_data[i,:])) / np.std(input_data[i,:])
     
        return output_data
        
    def snv_preprocessing(self):
        
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        data = pd.read_csv(cal_file)
        #self.cal_pd = data
        y = data['ref']
        X1 = data.drop(columns='ref')
        index_len = X1.shape[0]
       
        dataT2 = pd.read_csv(pred_file)
        #self.val_pd = dataT2
        ytest = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        
        
        #X1 = X1.append(X1test)
        X1= pd.concat([X1, X1test], ignore_index=True)
        #y = y.append(ytest)
        y= pd.concat([y, ytest], ignore_index=True)
        col = X1.columns
        wl = (X1.columns).astype(float)
        #print(wl)
    
        X = X1.to_numpy()
        Xsnv=self.snv(X)
        Xm_c = Xsnv[:index_len]
        Xm_t = Xsnv[index_len:]
        
        data_snv = pd.DataFrame(Xsnv, columns = col)
        data_snv['ref'] = y.to_numpy()
        #print(data_snv.head(2))
        #print(data_snv.shape)
        
        
        self.cal_pd = data_snv.iloc[0:index_len,:]
        #print(self.cal_pd.shape)
        
        self.val_pd = data_snv.iloc[index_len:,:]
        #print(self.val_pd.shape)
        
        
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        
        
        fig2, ax2 = plt.subplots(1)
        #ax2.plot(wl, Xsnv.T, lw=4)
        ax2.plot(wl, Xm_c.T, lw=4)
        ax2.set_xlabel('Wavenumber')
        ax2.set_ylabel('Absorbance/Reflectance')
        ax2.set_title("SNV Preprocessed Train Spectra")
        #ax2.legend()
        ax2.grid()
        plt.tight_layout()
        
        fig3, ax3 = plt.subplots(1)
        #ax2.plot(wl, Xsnv.T, lw=4)
        ax3.plot(wl, Xm_t.T, lw=4)
        ax3.set_xlabel('Wavenumber')
        ax3.set_ylabel('Absorbance/Reflectance')
        ax3.set_title("SNV Preprocessed Test Spectra")
        #ax2.legend()
        ax3.grid()
        plt.tight_layout()
        plt.show()
        
        #new added to generate csv files
        
        filepath = Path("Partitioned data/snv_train.csv")  
        filepath.parent.mkdir(parents=True, exist_ok=True)  
        self.cal_pd.to_csv(filepath,index=False)
        
        filepath2 = Path("Partitioned data/snv_test.csv")  
        filepath2.parent.mkdir(parents=True, exist_ok=True)  
        self.val_pd.to_csv(filepath2,index=False)
        
        
        self.snv_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
        #print(self.val_pd.columns)
        self.prerocessing_type = "SNV"
        self.disable_preprocessing()
        
    def sg_show(self,X):
        self.der_label.show()
        self.gap_label.show()
        self.poly_label.show()
        self.der_le.show()
        self.gap_le.show()
        self.poly_le.show()
        self.sg_button.hide()
        self.sgrun_button.show()
        
    def sg_(self,X):
        gap = self.gap_le.text()
        poly = self.poly_le.text()
        der = self.der_le.text()
        
        if gap!="":
             gap = int(gap)
        else:
            gap = 9
            self.gap_le.setText("9")
            
        if poly!="":
            poly = int(poly)
        else:
           poly = 2
           self.poly_le.setText("2")
        
        if der!="":
            der = int(der)
        else:
           der = 1
           self.der_le.setText("1")
        
        Xsg=savgol_filter(X, gap, poly, der)
        return Xsg
    
    def sg_preprocessing(self):
         
         cal_file=self.cal#"Mois_Corn_Cal.csv"
         pred_file=self.pred#"Mois_Corn_Val.csv"
         data = pd.read_csv(cal_file)
         #self.cal_pd = data
         y = data['ref']
         X1 = data.drop(columns='ref')
         index_len = X1.shape[0]
        
         dataT2 = pd.read_csv(pred_file)
         #self.val_pd = dataT2
         ytest = dataT2['ref']
         X1test = dataT2.drop(columns='ref')
         
         
         #X1 = X1.append(X1test)
         X1= pd.concat([X1, X1test], ignore_index=True)
         #y = y.append(ytest)
         y= pd.concat([y, ytest], ignore_index=True)
         col = X1.columns
         wl = (X1.columns).astype(float)
         #print(wl)
         X = X1.to_numpy()
         
         Xsnv = self.sg_(X)
         Xm_c = Xsnv[:index_len]
         Xm_t = Xsnv[index_len:]
         
         #Xsnv=savgol_filter(X, gap, poly, der)
         
         
         data_snv = pd.DataFrame(Xsnv, columns = col)
         data_snv['ref'] = y.to_numpy()
         #print(data_snv.head(2))
         #print(data_snv.shape)
         
         
         self.cal_pd = data_snv.iloc[0:index_len,:]
         #print(self.cal_pd.shape)
         
         self.val_pd = data_snv.iloc[index_len:,:]
         #print(self.val_pd.shape)
         
         
         plt.rcParams.update({'font.size': 16,})
         plt.rcParams["font.weight"] = "bold"
         plt.rcParams["axes.labelweight"] = "bold"
         
         
         
         fig2, ax2 = plt.subplots(1)
         #ax2.plot(wl, Xsnv.T, lw=4)
         ax2.plot(wl, Xm_c.T, lw=4)
         ax2.set_xlabel('Wavenumber')
         ax2.set_ylabel('Absorbance/Reflectance')
         ax2.set_title("SG Preprocessed Train Spectra")
         #ax2.legend()
         ax2.grid()
         plt.tight_layout()
         
         fig3, ax3 = plt.subplots(1)
         #ax2.plot(wl, Xsnv.T, lw=4)
         ax3.plot(wl, Xm_t.T, lw=4)
         ax3.set_xlabel('Wavenumber')
         ax3.set_ylabel('Absorbance/Reflectance')
         ax3.set_title("SG Preprocessed Test Spectra")
         #ax2.legend()
         ax3.grid()
         plt.tight_layout()
         plt.show()
         
        
         
         self.sgrun_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
 "background-color: rgb(85, 255, 0);")
         
         #print(self.val_pd.columns)
         self.prerocessing_type = "SG"+self.der_le.text()
         
         #new added to generate csv files
         
         filepath = Path("Partitioned data/"+self.prerocessing_type+"_train.csv")  
         filepath.parent.mkdir(parents=True, exist_ok=True)  
         self.cal_pd.to_csv(filepath,index=False)
         
         filepath2 = Path("Partitioned data/"+self.prerocessing_type+"_test.csv")  
         filepath2.parent.mkdir(parents=True, exist_ok=True)  
         self.val_pd.to_csv(filepath2,index=False)
         self.disable_preprocessing()
    
    def disable_preprocessing(self):
        self.pre_label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.pre_label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Preprocessing Selected</span></p></body></html>")
        self.raw_button.setEnabled(False)  
        self.msc_button.setEnabled(False)  
        self.snv_button.setEnabled(False)  
        self.sg_button.setEnabled(False)  
        self.sgrun_button.setEnabled(False) 
        self.der_le.setEnabled(False)
        self.poly_le.setEnabled(False)
        self.gap_le.setEnabled(False)
        self.run_button.setEnabled(True)
        
        
        
            
        
        
    def instruction_window(self):
        MainWindow.hide()
        self.i_window=QtWidgets.QMainWindow()
        self.ui_i=Ui_Instruction()
        self.ui_i.setupUi(self.i_window)
        self.i_window.show()
        QApplication.processEvents()
        self.ui_i.home_button.clicked.connect(self.go_home_ins)
    
    def go_home_ins(self):
        self.i_window.hide()
        MainWindow.show()
    
    def about_window(self):
        MainWindow.hide()
        self.a_window=QtWidgets.QMainWindow()
        self.ui_a=Ui_About()
        self.ui_a.setupUi(self.a_window)
        self.a_window.show()
        QApplication.processEvents()
        self.ui_a.home_button.clicked.connect(self.go_home_ab)
    
    def go_home_ab(self):
        self.a_window.hide()
        MainWindow.show()    
        
    def output_window(self):
        MainWindow.hide()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OutputWindow()
        self.ui.setupUi(self.window)
        
        
        #self.ui.feat_label.setText(self.feat)
        self.ui.feat_label.addItem(self.feat_list)
        self.ui.time_label.setText(self.time_)
        
        self.ui.mlr_button.clicked.connect(self.show_output_mlr)
        self.ui.pslr_button.clicked.connect(self.show_output_plsr)
        
        self.ui.reset_button.clicked.connect(self.reset_analysis)
        
       
        res_check = self.selected_list[:]
        data = self.cal_pd
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        
        wl = (X1.columns).astype(float)
        
        X=X1.to_numpy()
        y=y1.to_numpy()
        
        X0=X[0]
       
        
       
        
       
       
        X_pd_cal=X1.iloc[:,res_check]
        wl_selected = (X_pd_cal.columns).astype(float)
        
        #print(wl_selected)
       
        #print(X_pd_cal)
        Xpd_c=X_pd_cal.to_numpy()
        
        
        
        

        
        
        
        #plt.show()
        #print(X0)
        

        #MainWindow.hide()
        
        self.window.show()
        #print(self.total_feat)
        if(len(X_pd_cal.columns)<int(self.total_feat)):
            plt.rcParams.update({'font.size': 16,})
            plt.rcParams["font.weight"] = "bold"
            plt.rcParams["axes.labelweight"] = "bold"
            fig3, ax3 = plt.subplots(1)
            ax3.plot(wl, X0.T, lw=4)
            for i in wl_selected:
                ax3.axvline(x=i,color='red')
            ax3.set_xlabel('Wavenumber')
            ax3.set_ylabel('Absorbance/Reflectance')
            ax3.set_title("Selected features ", color="red")
            
            #print(X0[0])
            #print(X_pd_cal[str(feat_)])
            #ax3.scatter(feat_, X0[feat_].T, s=100, edgecolors=(0, 0, 0))
            
            #ax3.legend()
            ax3.grid()
            plt.tight_layout()
            plt.show()
        
    def reset_analysis(self):
        
        self.pop=""
        self.gen=""
        self.mut=""
        self.feat=""
        self.ref="0.0000001"
        #self.cal=""
        #self.pred=""
        self.rmsec=""
        self.rmsep=""
        self.r2c=""
        self.r2p=""
        self.time_=""
        self.feat_list=""
        self.y=[]
        self.y_=[]
        self.yt=[]
        self.yt_=[]
        self.selected_list=[]
        self.cal_pd = None        
        self.val_pd = None
        #self.total_feat = None
        self.prerocessing_type = ""
        #results = {"Number":[],"Regression":[],"LV":[],"Preprocessing":[],"R2C":[],"RMSEC":[],"R2P":[],"RMSEP":[],"RPD":[],"Feats":[]}
        #count_row = 0
        self.lvs= None
        
        self.msc_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.raw_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.snv_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.sg_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.sgrun_button.setStyleSheet("font: 75 10pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        
        self.pop_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.gen_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.feat_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mut_label.setStyleSheet("background-color: rgb(255, 255, 127);")
        
        self.pop_le.setText("")
        self.gen_le.setText("")
        self.feat_le.setText("")
        self.mut_le.setText("")
        
        self.der_label.hide()
        self.gap_label.hide()
        self.poly_label.hide()
        self.der_le.hide()
        self.gap_le.hide()
        self.poly_le.hide()
        self.sg_button.show()
        self.sgrun_button.hide()
        
        
        
        self.pre_label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")
        self.pre_label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Select Preprocessing</span></p></body></html>")
        self.raw_button.setEnabled(True)  
        self.msc_button.setEnabled(True)  
        self.snv_button.setEnabled(True)  
        self.sg_button.setEnabled(True)  
        self.sgrun_button.setEnabled(True) 
        self.der_le.setEnabled(True)
        self.poly_le.setEnabled(True)
        self.gap_le.setEnabled(True)
        self.run_button.setEnabled(False)
        self.tr_button_2.hide()
        self.tr_button_2.setStyleSheet("font: 75 9pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.tr_button_2.setText("Analyzing results please wait...")
        self.tr_button_2.setEnabled(False)
        
        
        self.window.hide()
        MainWindow.show()
        
    def show_output_plsr(self):
        #self.ui.mlr_button.setEnabled(False)
        #self.ui.pslr_button.setEnabled(False)
        
        
        self.rmsec=""
        self.r2c=""
        self.rmsep=""
        self.r2p=""
        self.ui.rmsec_label.setText(self.rmsec)
        self.ui.rmsep_label.setText(self.rmsep)
        self.ui.r2c_label.setText(self.r2c)
        self.ui.r2p_label.setText(self.r2p)
        
        self.y=[]
        self.y_=[]
        self.yt=[]
        self.yt_=[]
        
    
        
        feat_num = int(self.feat)
        ten_fold = model_selection.KFold(n_splits=10, shuffle=True, random_state=1)
        rmse_list = []
        rmse_pen_list = []
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        res_check = self.selected_list[:]
        
        # data = pd.read_csv(cal_file)
        # y1 = data['ref']
        # X1 = data.drop(columns='ref')
        
        data = self.cal_pd
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        
        X=X1.to_numpy()
        y=y1.to_numpy()
        #print(X.shape)
        #print(y.shape)
        
    
        # dataT2 = pd.read_csv(pred_file)
        # y1test = dataT2['ref']
        # X1test = dataT2.drop(columns='ref')
        dataT2 = self.val_pd
        y1test = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        
        Xtest=X1test.to_numpy()
        ytest=y1test.to_numpy()
        #print(Xtest.shape)
        #print(ytest.shape)
        
       
        #print("rescheck",res_check)
        X_pd_cal=X1.iloc[:,res_check]
        X_pd_test=X1test.iloc[:,res_check]
        #print(X_pd_cal)
        Xpd_c=X_pd_cal.to_numpy()
        Xpd_test=X_pd_test.to_numpy()
        
        if(feat_num>20):
            feat_num =20
        
        for i in np.arange(1, feat_num+1):
            pls = PLSRegression(n_components=i)
            score = model_selection.cross_val_score(pls, Xpd_c, y, cv=ten_fold, scoring='neg_mean_squared_error').mean()
            rmse_list.append(sqrt(-score))
            #rmse_pen_list.append(sqrt(-score)*(e**(i*0.05))) #penalized rmsecv
            
        
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        fig, ax = plt.subplots(1)
        ax.plot(np.arange(1, feat_num+1), np.array(rmse_list), '-v',label='RMSECV',lw=1.5)
        #ax.plot(np.arange(1, feat_num+1), np.array(rmse_pen_list), '-v',label='Penalized RMSECV',color='red',lw=1.5) #penalized lv
        ax.scatter(rmse_list.index(min(rmse_list))+1, min(rmse_list), s=200, edgecolors=(1, 0, 1),marker='v',color='red') # Haland and Thomas criterion for lv selection
        #ax.scatter(rmse_pen_list.index(min(rmse_pen_list))+1, min(rmse_pen_list), s=200, edgecolors=(1, 0, 1),marker='v',color='red')
        #ax.plot(rmse_pen_list.index(min(rmse_pen_list))+1, min(rmse_pen_list), '-v',label='Penalized RMSECV',color='red',lw=1.5)
        ax.set_xlabel('No. of LVs selected')
        ax.set_ylabel('RMSE')
        #ax.set_title('RMSE change based on LVs')
        ax.set_title('Haland-Thomas Lv selection')
        #self.min_lv = rmse_pen_list.index(min(rmse_pen_list))+1
        #ax.xlim(xmin=-1)
        ax.legend()
        ax.grid()
        plt.tight_layout()
        plt.show()
        
        self.ui.lv_label.show()
        self.ui.lv_le.show()
        self.ui.pslr_run_button.setStyleSheet("font: 75 9pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.ui.pslr_run_button.show()
        self.ui.lv_le.setDisabled(False)
        self.ui.pslr_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.ui.pslr_button.setDisabled(True)
        self.ui.mlr_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        #self.ui.lv_le.editingFinished.connect(self.plsr_output)
        self.ui.pslr_run_button.clicked.connect(self.plsr_output)
        
    def plsr_output(self):
        
        
        self.ui.pslr_run_button.setStyleSheet("font: 75 9pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.ui.pslr_run_button.setDisabled(True)
        if (self.ui.lv_le.text()=="") or (int(self.ui.lv_le.text())>int(self.feat)) or (int(self.ui.lv_le.text())<=0):
            self.ui.lv_le.setText(self.feat)
            lv_num = int(self.feat)
        else:
            lv_num = int(self.ui.lv_le.text())
            
            
        self.ui.lv_le.setDisabled(True)
            
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        res_check = self.selected_list[:]
        
        # data = pd.read_csv(cal_file)
        # y1 = data['ref']
        # X1 = data.drop(columns='ref')
        
        data = self.cal_pd
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        
        
        X=X1.to_numpy()
        y=y1.to_numpy()
        #print(X.shape)
        #print(y.shape)
        
    
        # dataT2 = pd.read_csv(pred_file)
        # y1test = dataT2['ref']
        # X1test = dataT2.drop(columns='ref')
        
        dataT2 = self.val_pd
        y1test = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        
        Xtest=X1test.to_numpy()
        ytest=y1test.to_numpy()
        #print(Xtest.shape)
        #print(ytest.shape)
        
        
        
        X_pd_cal=X1.iloc[:,res_check]
        X_pd_test=X1test.iloc[:,res_check]
        #print(X_pd_cal)
        Xpd_c=X_pd_cal.to_numpy()
        Xpd_test=X_pd_test.to_numpy()
        
        pls = PLSRegression(n_components=lv_num)
        pls.fit(Xpd_c, y)
        
        y_=pls.predict(Xpd_c)
        y_test=pls.predict(Xpd_test)
        
        msec = mean_squared_error(y, y_)
        rmsec = sqrt(msec)
        msep = mean_squared_error(ytest, y_test)
        rmsep = sqrt(msep)
        rpd =np.std(ytest)/rmsep
        
        
        r2c=r2_score(y, y_)
        r2p=r2_score(ytest, y_test)
        r2c = "{:.4f}".format(r2c)
        r2p = "{:.4f}".format(r2p)
        rmsec="{:.4f}".format(rmsec)
        rmsep="{:.4f}".format(rmsep)
        rpd="{:.4f}".format(rpd)
        
        self.y=y
        self.y_=y_
        self.yt = ytest
        self.yt_=y_test
        
        
        
        """
        Y_plsr = pd.DataFrame(y_)
    
        # save the dataframe as a csv file
        Y_plsr.to_csv("Predicted_PLSR_train.csv",index = False,header=False)
        
        
        Y_plsr_test = pd.DataFrame(y_test)
        # save the dataframe as a csv file
        Y_plsr_test.to_csv("Predicted_PLSR_test.csv",index = False,header=False)
        """
        
        feat_=[]
        for i in X_pd_cal.columns:
            feat_.append(float(i))
        #print("feat_=",feat_)
        
        method="GA_FS_REG"
        
        
        
       
        self.rmsec=str(rmsec)
        self.r2c=str(r2c)
        self.rmsep=str(rmsep)
        self.r2p=str(r2p)
        self.count_row += 1
        self.results["Number"].append(self.count_row)
        self.results["Regression"].append("PLSR")
        self.results["LV"].append(int(self.ui.lv_le.text()))
        self.results["Preprocessing"].append(self.prerocessing_type)
        self.results["R2C"].append(float(self.r2c))
        self.results["R2P"].append(float(self.r2p))
        self.results["RMSEC"].append(float(self.rmsec))
        self.results["RMSEP"].append(float(self.rmsep))
        self.results["RPD"].append(float(rpd))
        self.results["Feats"].append(int(self.feat))
        self.results["Selected feats"].append(str(feat_))
        #print(self.results)
        """
        f = open(method+"_plsr_result_"+str(self.count_row)+".txt", "w+")
        f.write(method)
        f.write("\n")
        f.write("Number of features selected:"+str(len(X_pd_cal.columns)))
        f.write("\n")
        f.write("Selected Features:"+str(feat_))
        f.write("\n")
        f.write("LV="+str(lv_num))
        f.write("\n")
        f.write("R2c="+str(r2c))
        f.write("\n")
        f.write("RMSEC="+str(rmsec))
        f.write("\n")
        f.write("R2p="+str(r2p))
        f.write("\n")
        f.write("RMSEP="+str(rmsep))
        f.write("\n")
        f.close()
        """
        
        
        
        
        df = pd.DataFrame(self.results)
        #df.to_excel('Predictive results.xlsx', sheet_name='stats', index= False)
        df.to_excel(self.output_filename, sheet_name='stats', index= False)
        """
        ###
        workbook = openpyxl.load_workbook('Predictive results.xlsx')
        workbook.create_sheet("Prediction"+str(self.count_row))
        worksheet = workbook["Prediction"+str(self.count_row)]
        col = "A"
        row = 0
        worksheet[col+str(row)]="Predicted_ycal"
        col = "B"
        row = 0
        worksheet[col+str(row)]="Predicted_yval"
        i=1
        col="A"
        for item in self.y_:
            worksheet[col+str(row+i)]=item
            i += 1
        
        i=1
        col="B"
        for item in self.y_test:
            worksheet[col+str(row+i)]=item
            i += 1
        workbook.save('Predictive results.xlsx')
        workbook.close()
        
        """
        self.show_gui()
        self.show_plot("Actual vs Predicted Plot using PLSR")
        self.show_rc(pls,feat_)
        self.show_vip(pls,feat_)
        
    def show_rc(self,pls,feat_):
        # Extract the coefficients
        coefficients = pls.coef_.ravel()  # Flatten the coefficients array
        #print(coefficients.shape)
        # Plotting
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        plt.figure(figsize=(10, 6))
        #plt.plot(feat_,coefficients, marker='o', linestyle='-', color='b',lw=2)
        plt.plot(feat_,coefficients, color='b',lw=2)
        plt.xlabel('Features')
        plt.ylabel('Regression coefficient')
        plt.title('PLSR regression coefficients')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    def show_vip(self,model,feat_):
        t = model.x_scores_
        w = model.x_weights_
        q = model.y_loadings_
        p, h = w.shape
        vips = np.zeros((p,))
        s = np.diag(t.T @ t @ q.T @ q).reshape(h, -1)
        total_s = np.sum(s)
        for i in range(p):
            weight = np.array([ (w[i,j] / np.linalg.norm(w[:,j]))**2 for j in range(h) ])
            vips[i] = np.sqrt(p*(s.T @ weight)/total_s)
        #print(vips.shape)
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        plt.figure(figsize=(10, 6))
        #plt.plot(feat_,vips, marker='o', linestyle='-', color='r',lw=2)
        plt.bar(feat_,vips)
        plt.axhline(y=1, color='r', linestyle='--')
        plt.xlabel('Features')
        plt.ylabel('VIP score')
        plt.title('VIP score plot')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    
        
        
    def show_output_mlr(self):
        #self.ui.mlr_button.setEnabled(False)
        #self.ui.pslr_button.setEnabled(False)
        self.ui.pslr_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 255);")
        self.ui.mlr_button.setStyleSheet("font: 75 12pt\"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.ui.mlr_button.setDisabled(True)
        self.rmsec=""
        self.r2c=""
        self.rmsep=""
        self.r2p=""
        self.ui.rmsec_label.setText(self.rmsec)
        self.ui.rmsep_label.setText(self.rmsep)
        self.ui.r2c_label.setText(self.r2c)
        self.ui.r2p_label.setText(self.r2p)
        
        self.y=[]
        self.y_=[]
        self.yt=[]
        self.yt_=[]
        
        self.ui.lv_label.hide()
        self.ui.lv_le.hide()
        self.ui.pslr_run_button.hide()
        
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        res_check = self.selected_list[:]
        
        # data = pd.read_csv(cal_file)
        # y1 = data['ref']
        # X1 = data.drop(columns='ref')
        
        data = self.cal_pd
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        
        X=X1.to_numpy()
        y=y1.to_numpy()
        #print(X.shape)
        #print(y.shape)
        
    
        # dataT2 = pd.read_csv(pred_file)
        # y1test = dataT2['ref']
        # X1test = dataT2.drop(columns='ref')
        
        dataT2 = self.val_pd
        y1test = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        
        Xtest=X1test.to_numpy()
        ytest=y1test.to_numpy()
        #print(Xtest.shape)
        #print(ytest.shape)
        
        
        
        X_pd_cal=X1.iloc[:,res_check]
        X_pd_test=X1test.iloc[:,res_check]
        #print(X_pd_cal)
        Xpd_c=X_pd_cal.to_numpy()
        Xpd_test=X_pd_test.to_numpy()
        '''
        #Linear Regression
        RPDp=(np.std(ytt)/rmsep)
        '''
        clf2 = LinearRegression()
        clf2.fit(Xpd_c,y)
        y_=clf2.predict(Xpd_c)
        y_test=clf2.predict(Xpd_test)
        
        msec = mean_squared_error(y, y_)
        rmsec = sqrt(msec)
        msep = mean_squared_error(ytest, y_test)
        rmsep = sqrt(msep)
        rpd =np.std(ytest)/rmsep
        
        
        r2c=r2_score(y, y_)
        r2p=r2_score(ytest, y_test)
        r2c = "{:.4f}".format(r2c)
        r2p = "{:.4f}".format(r2p)
        rmsec="{:.4f}".format(rmsec)
        rmsep="{:.4f}".format(rmsep)
        rpd="{:.4f}".format(rpd)
        
        self.y=y
        self.y_=y_
        self.yt=ytest
        self.yt_=y_test
        """
        Y_plsr = pd.DataFrame(y_)
    
        # save the dataframe as a csv file
        Y_plsr.to_csv("Predicted_MLR_train.csv",index = False,header=False)
        
        
        Y_plsr_test = pd.DataFrame(y_test)
        # save the dataframe as a csv file
        Y_plsr_test.to_csv("Predicted_MLR_test.csv",index = False,header=False)
        
        """
        
        
        
        feat_=[]
        for i in X_pd_cal.columns:
            feat_.append(float(i))
        #print("feat_=",feat_)
        
        method="GA_FS_REG"
        
  
        
       
        self.rmsec=str(rmsec)
        self.r2c=str(r2c)
        self.rmsep=str(rmsep)
        self.r2p=str(r2p)
        
        
        
        self.rmsec=str(rmsec)
        self.r2c=str(r2c)
        self.rmsep=str(rmsep)
        self.r2p=str(r2p)
        self.count_row += 1
        self.results["Number"].append(self.count_row)
        self.results["Regression"].append("MLR")
        self.results["LV"].append("N/A")
        self.results["Preprocessing"].append(self.prerocessing_type)
        self.results["R2C"].append(float(self.r2c))
        self.results["R2P"].append(float(self.r2p))
        self.results["RMSEC"].append(float(self.rmsec))
        self.results["RMSEP"].append(float(self.rmsep))
        self.results["RPD"].append(float(rpd))
        self.results["Feats"].append(int(self.feat))
        self.results["Selected feats"].append(str(feat_))
        #print(self.results)
        
        """
        
        f = open(method+"_mlr_result_"+str(self.count_row)+".txt", "w+")
        f.write(method)
        f.write("\n")
        f.write("Number of features selected:"+str(len(X_pd_cal.columns)))
        f.write("\n")
        f.write("Selected Features:"+str(feat_))
        f.write("\n")
        f.write("R2c="+str(r2c))
        f.write("\n")
        f.write("RMSEC="+str(rmsec))
        f.write("\n")
        f.write("R2p="+str(r2p))
        f.write("\n")
        f.write("RMSEP="+str(rmsep))
        f.write("\n")
        f.close()
        """
        
        
        df = pd.DataFrame(self.results)
        #df.to_excel('Predictive results.xlsx', sheet_name='stats', index= False)
        df.to_excel(self.output_filename, sheet_name='stats', index= False)
        
        self.show_gui()
        self.show_plot("Actual vs Predicted Plot using MLR")
        
    def show_gui(self):
        self.ui.rmsec_label.setText(self.rmsec)
        self.ui.rmsep_label.setText(self.rmsep)
        self.ui.r2c_label.setText(self.r2c)
        self.ui.r2p_label.setText(self.r2p)
        
        
    def show_plot(self,title):
        plt.rcParams.update({'font.size': 16,})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        fig, ax = plt.subplots(2)
        ax[0].scatter(self.y, self.y_, s=100, edgecolors=(0, 0, 0))
        ax[1].scatter(self.yt, self.yt_, s=100, edgecolors=(1, 0, 1))
        ax[0].plot([self.y.min(), self.y.max()], [self.y.min(), self.y.max()],label='Train fit line', color='red', lw=4)
        ax[1].plot([self.yt.min(), self.yt.max()], [self.yt.min(), self.yt.max()],label='Test fit line', color='green', lw=4)
        ax[0].set_xlabel('Measured')
        ax[0].set_ylabel('Predicted')
        ax[0].set_title(title)
        ax[0].legend()
        ax[0].grid()
        ax[1].set_xlabel('Measured')
        ax[1].set_ylabel('Predicted')
        ax[1].legend()
        ax[1].grid()
        plt.tight_layout()
        plt.show()
        
        
    def tr_handler(self):
        #print("Button pressed")
        now_2 = datetime.now()
        self.output_filename= now_2.strftime("Predictive results_%m-%d-%y_%H-%M.xlsx")
        self.time_now = now_2.strftime("_%m-%d-%y_%H-%M_")
        #print(self.output_filename)
        #self.output_filename = "Predicted.xlsx"
        self.open_dialog_box_tr()
        
    def open_dialog_box_tr(self):
        filename = QFileDialog.getOpenFileName()
        self.cal = filename[0]
        data = pd.read_csv(self.cal)
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        X=X1.to_numpy()
        self.total_feat = X.shape[1]

        
    def ts_handler(self):
        #print("Button pressed")
        self.open_dialog_box_ts()
        
    def open_dialog_box_ts(self):
        filename = QFileDialog.getOpenFileName()
        self.pred = filename[0]
        if((self.cal)!="" and (self.pred)!=""):
            self.tr_button.setEnabled(False)
            self.ts_button.setEnabled(False)
            #self.run_button.setEnabled(True)
            #self.file_label.setText("Files Selected")
        
            self.file_label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
            self.file_label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Files Selected</span></p></body></html>")
            
            
            
       
        
    def le_pop(self):
        self.pop=self.pop_le.text()
        self.pop_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
        
    def le_gen(self):
        self.gen=self.gen_le.text()
        self.gen_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
    def le_mut(self):
        self.mut=self.mut_le.text()
        self.mut_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
    def le_feat(self):
        self.feat=self.feat_le.text()
        self.feat_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        
    def le_ref(self):
        self.ref=self.ref_le.text()
        self.ref_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        #print(self.pop,self.gen,self.mut,self.feat,self.ref,self.cal,self.pred)
    
    def check_param(self):
        if((self.pop!="")and(self.gen!="")and(self.mut!="")and(self.feat!="")and(self.ref!="")):
            self.run_button.setEnabled(True)
            
        else:
            if(self.pop==""):
                self.pop_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
                self.pop_le.setText("1")
                self.pop=self.pop_le.text()
            if(self.gen==""):
                self.gen_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
                self.gen_le.setText("1")
                self.gen=self.gen_le.text()
            if(self.feat==""):
                self.feat_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
                self.feat_le.setText(str(self.total_feat))
                self.feat=self.feat_le.text()
            if(self.mut==""):
                self.mut_le.setText("0.003")
                self.mut_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
                self.mut=self.mut_le.text()
            """
            if(self.ref==""):
                self.ref_le.setText("0.0001")
                self.ref_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
                self.ref=self.ref_le.text()
            """
            self.run_button.setEnabled(True)
            
        
            
        
        
    def ga(self):
        # Loading the GIF
        self.check_param()
        self.run_button.setEnabled(False)
        self.sample_label.hide()
        self.tr_button_2.show()
        
        """
        self.animate_label.show()
        self.movie = QMovie(":/icons/loading2.gif")
        self.animate_label.setMovie(self.movie)
        self.movie.start()
        """
    
        #QApplication.processEvents()
        old = datetime.now()
        feat_size=int(self.feat)#10
        
        cal_file=self.cal#"Mois_Corn_Cal.csv"
        pred_file=self.pred#"Mois_Corn_Val.csv"
        mutation_probability=float(self.mut)#.003
        population_size = int(self.pop)#50
        maximum_generation = int(self.gen)#10
        ref_val=float(self.ref)#0.001
        method="GA_FS_REG"
        
        
        ping=0
        data_cal=pd.read_csv(cal_file)
        y1_cal = data_cal['ref']
        X1_cal = data_cal.drop(columns='ref')
        
        
        data_pred=pd.read_csv(pred_file)
        y1_val = data_pred['ref']
        X1_val = data_pred.drop(columns='ref')
        
        if((feat_size*2)<X1_cal.to_numpy().shape[1]):
            feat_size = feat_size*2
            ping=1
            
        
        
        def create_reference_solution(chromosome_length):
            number_of_ones=feat_size
            #number_of_ones = int(chromosome_length /feat_size_sel)
        
            # Build an array with an equal mix of zero and ones
            reference = np.zeros(chromosome_length)
            reference[0: number_of_ones] = 1
        
            # Shuffle the array to mix the zeros and ones
            np.random.shuffle(reference)
            
            return reference
        # Print an example target array
        
        
        ###############################################################################
        #print("reference\n",ob)
        def get_fitness(individual):
          #score=0
          #for i in range (0,len(individual)):
            #score=score+(individual[i]*(2**(len(individual)-i-1)))
          #return score
          QApplication.processEvents()
          res = [p for p, val in enumerate(individual) if val]
          #data = pd.read_csv("C_tr.xlsx.csv")
          #data=pd.read_csv("Corn_Train.csv")
          data=pd.read_csv(cal_file)
          y1 = data['ref']
          X1 = data.drop(columns='ref')
          X_pd=X1.iloc[:,res]
          Xtr=X_pd.to_numpy()
          y=y1.to_numpy()
          clf = LinearRegression()
          clf.fit(Xtr,y)
          y_=clf.predict(Xtr)
          #r2c=r2_score(y, y_)
          msec = mean_squared_error(y, y_)
          rmsec = sqrt(msec)
          #print("Res fit",res,"     r2c=",r2c,"    indiv=",individual)
         
          score=rmsec
          return score
        
        
        def best_feat_keep(individual,score,feat_size):
          
          #print (np.count_nonzero(ob == 1))
          
          res = [p for p, val in enumerate(individual) if val]
          #print("res======",res)
          total_feat=len(individual)
          r=len(res)
          num_available=total_feat-r
          cg=r-feat_size
          p=cg
          #print("CG====",cg)
          temp_fit=[]
          ran_cal=[]
          
          res2=[]
          for i in res:
            res2.append(i)
          #print(res2)
          if(p<0):
            f=p*-1
            for i in range(f): 
              for k in range(num_available):
                QApplication.processEvents()
                if(len(res2)<len(individual)):
                  ran_num=random.choice([x for x in range(len(individual)) if x not in res2])
                  #print("ran_num",ran_num)
                  individual[ran_num]=1
                  #print("indiviiii===============",individual)
                  temp_fit.append(get_fitness(individual))
                  ran_cal.append(ran_num)
                  #count=count+1
        
        
                  if(temp_fit[ran_cal.index(ran_num)]<score):
                    individual[ran_num]=0
                    
                    res2.append(ran_num)
                    #print("in inner    index",ran_num,"deleted","res=",res,"res2=",res2)
                  #k=k+1
                  
              
        
              #if(i==(cg-1)):# and count==len(res)):
              new_score=min(temp_fit)
              ran_num=ran_cal[temp_fit.index(new_score)]
              #print("RAN NUM+++++++++++++++",ran_num)
              individual[ran_num]=1
              res.append(ran_num)
              res2=[]
              for t in res:
                res2.append(t)
        
              temp_fit=[]
              ran_cal=[]
        
          #print("p====",p)
        
        
        
        
        
          if(p>0):
            count=0
            for i in range(p): 
              for k in range(len(res2)):
                if(len(res2)>0):
                  QApplication.processEvents()
                  ran_num=random.choice([x for x in range(max(res2)+1) if x in res2])
                  #print("ran_num",ran_num)
                  individual[ran_num]=0
                  #print("indiviiii===============",individual)
                  temp_fit.append(get_fitness(individual))
                  ran_cal.append(ran_num)
                  count=count+1
        
        
                  if(temp_fit[ran_cal.index(ran_num)]>score):
                    individual[ran_num]=1
                    
                    res2.remove(ran_num)
                    #print("in inner    index",ran_num,"deleted","res=",res,"res2=",res2)
                    #k=k+1
                  
              
        
              #if(i==(cg-1)):# and count==len(res)):
              new_score=min(temp_fit)
              ran_num=ran_cal[temp_fit.index(new_score)]
              #print("RAN NUM+++++++++++++++",ran_num)
              individual[ran_num]=0
              temp_fit=[]
              ran_cal=[]
              res2=[]
              for t in res:
                res2.append(t)
              #print("RESSSSSSSSSSSSSSSSSSSSSSSSS",res)
              res2.remove(ran_num)
              res.remove(ran_num)
              #print("in outer    index",ran_num,"deleted","res=",res)
        
                #break
              #if(temp_fit[ran_cal.index(ran_num)]<score):
                #individual[ran_num]=1
                #i=i-1
                 
          new_individual=individual
          new_score=get_fitness(new_individual)
          return new_individual,new_score
        
        
        
        
        
        ######################################GA OP###########################
        def create_starting_population(individuals, chromosome_length):
            # Set up an initial array of all zeros
            population = np.zeros((individuals, chromosome_length))
            feat_size_sel=50
            feat_num=feat_size
            #feat_num=int(chromosome_length /feat_size_sel )
            # Loop through each row (individual)
            for i in range(individuals):
                # Choose a random number of ones to create
                ones = random.randint(feat_num, feat_num)
                #print(ones)
                # Change the required number of zeros to ones
                population[i, 0:ones] = 1
                # Sfuffle row
                np.random.shuffle(population[i])
            
            return population
      
        
        def select_individual_by_tournament(population, scores):
            # Get population size
            population_size = len(scores)
            
            # Pick individuals for tournament
            fighter_1 = random.randint(0, population_size-1)
            fighter_2 = random.randint(0, population_size-1)
            
            # Get fitness score for each
            fighter_1_fitness = scores[fighter_1]
            fighter_2_fitness = scores[fighter_2]
            
            # Identify undividual with highest fitness
            # Fighter 1 will win if score are equal
            if fighter_1_fitness <= fighter_2_fitness:
                winner = fighter_1
            else:
                winner = fighter_2
            
            # Return the chromsome of the winner
            return population[winner, :]
        
        
        
        
        
        def breed_by_crossover(parent_1, parent_2):
            # Get length of chromosome
            chromosome_length = len(parent_1)
            
            # Pick crossover point, avoding ends of chromsome
            crossover_point = random.randint(1,chromosome_length-1)
            
            # Create children. np.hstack joins two arrays
            child_1 = np.hstack((parent_1[0:crossover_point],
                                parent_2[crossover_point:]))
            
            child_2 = np.hstack((parent_2[0:crossover_point],
                                parent_1[crossover_point:]))
            
            # Return children
            return child_1, child_2
        
     
        
        def randomly_mutate_population(individual):
          x = random.random()
          #print("x=",x)
          res = [p for p, val in enumerate(individual) if val]
          ran_num=random.choice([x for x in range(len(individual))])
          #print("rN=",ran_num)
          if(mutation_probability>x):
            individual[ran_num]=1-individual[ran_num]
          return individual
        

        
        data = pd.read_csv(cal_file)
        y1 = data['ref']
        X1 = data.drop(columns='ref')
        X=X1.to_numpy()
        y=y1.to_numpy()
        #print(X.shape)
        #print(y.shape)
        
    
        dataT2 = pd.read_csv(pred_file)
        y1test = dataT2['ref']
        X1test = dataT2.drop(columns='ref')
        Xtest=X1test.to_numpy()
        ytest=y1test.to_numpy()
        #print(Xtest.shape)
        #print(ytest.shape)
        
    
        clf = LinearRegression()
        clf.fit(X,y)
        y_=clf.predict(X)
        y_test=clf.predict(Xtest)
        
        msec = mean_squared_error(y, y_)
        rmsec = sqrt(msec)
        msep = mean_squared_error(ytest, y_test)
        rmsep = sqrt(msep)
        
        
        r2c=r2_score(y, y_)
        r2p=r2_score(ytest, y_test)
        r2c = "{:.4f}".format(r2c)
        r2p = "{:.4f}".format(r2p)
        rmsec="{:.4f}".format(rmsec)
        rmsep="{:.4f}".format(rmsep)
        
        #print(" With all features:\n RMSEC",rmsec, "  R2c=",r2c)
        #print("RMSEP=",rmsep,"   R2p=",r2p)
        
        
        #chromosome_length = 10
        
        chromosome_length=len(X[0])
        #print("Chromosome length=",chromosome_length)
        # feat_size=100
        best_score_progress = [] # Tracks progress
        best_indiv=[]
        
        
        indivs=[]
        score_trace=[]
        scores=[]
        
        # Create reference solution 
        # (this is used just to illustrate GAs)
        
        reference = create_reference_solution(chromosome_length)
        
        # Create starting population
        population = create_starting_population(population_size, chromosome_length)
        
        # Display best score in starting population
        #scores = calculate_fitness(reference, population)
        for i in population:
          score = get_fitness(i)
          indivs.append(i)
          scores.append(score)
          score_trace.append(score)
          #print(i,"     ",score)
        best_score = min(scores)
        best_score_progress.append(best_score)
        best_individual=indivs[scores.index(best_score)]
        best_indiv.append(best_individual)
        #print("best individual=",best_individual)
        #print ('Starting best score:', best_score)
        
        
        # Add starting best score to progress tracker
        #best_score_progress.append(best_score)
        
        # Now we'll go through the generations of genetic algorithm
        #for generation in range(maximum_generation):
        generation=0
        while(min(best_score_progress)>ref_val):
            # Create an empty list for new population
            QApplication.processEvents()
            new_population = []
            new_scores=[]
            #print("Generation no:",generation)
            generation=generation+1
          
            
            # Create new popualtion generating two children at a time
            for i in range(int(population_size/2)):
                QApplication.processEvents()
                parent_1 = select_individual_by_tournament(population, scores)
                parent_2 = select_individual_by_tournament(population, scores)
                child1=create_reference_solution(chromosome_length)
                child2=create_reference_solution(chromosome_length)
                child_1, child_2 = breed_by_crossover(parent_1, parent_2)
                #####mutation
                child1=randomly_mutate_population(child1)
                child2=randomly_mutate_population(child2)
        
                child_1,score1=best_feat_keep(child1,get_fitness(child1),feat_size)
                child_2,score2=best_feat_keep(child2,get_fitness(child2),feat_size)
        
                new_population.append(child_1)
                new_population.append(child_2)
                new_scores.append(child1)
                new_scores.append(child2)
            
        
            # Apply mutation
            #mutation_rate = 0.002
        
        
            # Replace the old population with the new one
        
        
            population2 = np.array(new_population)
            #rest1 = [p for p, val in enumerate(population2[0]) if val]
            #print("feats before good pop selection", rest1)
            scores2=[]
        
            score_gen=[]
            pop_gen=[]
        
            new_pop_gen=[]
            new_score_gen=[]
            
            # Apply mutation
            #mutation_rate = 0.002
            #population = randomly_mutate_population(population, mutation_rate)
        
            # Score best solution, and add to tracker
            #scores = calculate_fitness(reference, population)
            for i in population2:
              #i=best_feat_keep(i,get_fitness(i),feat_size)
              score = get_fitness(i)
              indivs.append(i)
              scores2.append(score)
              score_trace.append(score)
            #best_score = max(scores)
            best_score = min(score_trace)
            best_score_progress.append(best_score)
            best_individual=indivs[score_trace.index(best_score)]
            best_indiv.append(best_individual)
            
            for b in best_score_progress:
              score_gen.append(b)
        
            for nn in scores2:
              new_score_gen.append(nn)
            new_score_gen.sort(reverse=True)
            for nnp in new_score_gen:
              temp=scores2.index(nnp)
              new_pop_gen.append(new_population[temp])
        
            
            score_gen.sort(reverse=True)
            for i in score_gen:
              temp=best_score_progress.index(i)
              pop_gen.append(best_indiv[temp])
            
            pop_temp=[]
            l=len(best_indiv)
            p=len(new_population)
            half=int(p/2)
            if(l<=half):
              for r in pop_gen:
                pop_temp.append(r)
              for j in range (l,p):
                pop_temp.append(new_pop_gen[j-l])
            else:
              for ii in range (0,half):
                pop_temp.append(pop_gen[ii])
              for kk in range (half,p):
                pop_temp.append(new_pop_gen[kk])
            population = np.array(new_pop_gen)
            scores=[]
            for ppp in population:
              score = get_fitness(ppp)
              scores.append(score)
            #rest = [p for p, val in enumerate(population[0]) if val]
            #print(len(population), rest)
            if(generation==maximum_generation):
              print("optimal sol not found!!!")
              break
        
        
        # GA has completed required generation
        #print ('End best score, percent target: %.1f' %best_score)
        mut_score = min(best_score_progress)
        mut_indiv=best_indiv[best_score_progress.index(mut_score)]
        #print("best individual=",mut_indiv)
        #print ('lowest rmsec',mut_score)
        
        
        
        def best_subset(list_,k):
            n = len(list_)
            temp_rmse = []
            temp_r2 = []
            temp_comb = []
            comb = combinations(list_, n-k)
            
            data_cal=pd.read_csv(cal_file)
            y1_cal = data_cal['ref']
            X1_cal = data_cal.drop(columns='ref')
            y=y1_cal.to_numpy()
            
            data_pred=pd.read_csv(pred_file)
            y1_val = data_pred['ref']
            X1_val = data_pred.drop(columns='ref')
            ytest=y1_val.to_numpy()
            
            for i in list(comb):
                #print(i)
                i = list(i)
                #print("i======>",i)
                
                
                X_pd=X1_cal.iloc[:,i]
                Xtr=X_pd.to_numpy()
                
                
                
                
                X1_pd_test = X1_val.iloc[:,i] 
                Xtest=X1_pd_test.to_numpy()
                
                
                
                clf = LinearRegression()
                clf.fit(Xtr,y)
                y_=clf.predict(Xtr)
                ytest_ = clf.predict(Xtest)
                #r2c=r2_score(y, y_)
                msep_temp = mean_squared_error(ytest, ytest_)
                rmsep_temp = sqrt(msep_temp)
                temp_rmse.append(float(rmsep_temp))
                temp_comb.append(i)
                
                X_pd=None
                X_tr=None
                clf=None
                Xtest=None#print
                X1_pd_test=None
                
            minpos = temp_rmse.index(min(temp_rmse))  #min rmse location
            #print(temp_rmse)
            #print("Minpos=",minpos)
            return temp_comb[minpos]
                
        
        res_check = [p for p, val in enumerate(mut_indiv) if val]
        #print("best individual=",res_check)
        list_=res_check
        temp_list = []
        #combination for best features
        if(ping==1):
            feat_org = feat_size//2
        else:
            feat_org = feat_size
            
        while(len(list_)>feat_org):
            temp_list = best_subset(list_,1)
            list_=[]
            list_=temp_list
            #print(list_)
            temp_list=[]
        #print(list_)
        
        
        res_check = []
        res_check = list_
        #print("res_check--->",res_check)
        
        
        
        self.selected_list = res_check[:]
        
        
        X_pd_cal=X1.iloc[:,res_check]
        X_pd_test=X1test.iloc[:,res_check]
        #print(X_pd_cal)
        Xpd_c=X_pd_cal.to_numpy()
        Xpd_test=X_pd_test.to_numpy()
        '''
        #Linear Regression
        RPDp=(np.std(ytt)/rmsep)
        '''
        clf2 = LinearRegression()
        clf2.fit(Xpd_c,y)
        y_=clf2.predict(Xpd_c)
        y_test=clf2.predict(Xpd_test)
        
        msec = mean_squared_error(y, y_)
        rmsec = sqrt(msec)
        msep = mean_squared_error(ytest, y_test)
        rmsep = sqrt(msep)
        
        
        r2c=r2_score(y, y_)
        r2p=r2_score(ytest, y_test)
        r2c = "{:.4f}".format(r2c)
        r2p = "{:.4f}".format(r2p)
        rmsec="{:.4f}".format(rmsec)
        rmsep="{:.4f}".format(rmsep)
        
        #print(" With selected features:\n RMSEC",rmsec, "  R2c=",r2c, "  RMSEP=",rmsep," R2p=",r2p)
        #print("Number of features selected:",str(len(X_pd_cal.columns)))
        
        
        
        new=datetime.now()
        time_=new-old
        feat_=[]
        for i in X_pd_cal.columns:
            feat_.append(float(i))
        #print("feat_=",feat_)
        
        
        
       
        
        
        
        
        
        self.feat_list=str(feat_)
        self.time_=str(time_)
        
        #self.animate_label.hide()
        
        self.tr_button_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 0);")
        self.tr_button_2.setText("SHOW RESULTS")
        self.tr_button_2.setEnabled(True)
        
        
        
        
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

