# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Nextcloud\Python\Termo_potok_1_2\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table = QtWidgets.QTableWidget(self.tab)
        self.table.setMinimumSize(QtCore.QSize(400, 400))
        self.table.setMaximumSize(QtCore.QSize(600, 16777215))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table)
        self.table2 = QtWidgets.QTableWidget(self.tab)
        self.table2.setMinimumSize(QtCore.QSize(200, 150))
        self.table2.setMaximumSize(QtCore.QSize(600, 150))
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(0)
        self.table2.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.spinBox.setMinimum(-365)
        self.spinBox.setMaximum(365)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_left = QtWidgets.QLabel(self.tab)
        self.label_left.setMinimumSize(QtCore.QSize(0, 20))
        self.label_left.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_left.setObjectName("label_left")
        self.verticalLayout_3.addWidget(self.label_left)
        self.slider_left = QtWidgets.QSlider(self.tab)
        self.slider_left.setMinimumSize(QtCore.QSize(0, 20))
        self.slider_left.setMaximumSize(QtCore.QSize(16777215, 20))
        self.slider_left.setOrientation(QtCore.Qt.Horizontal)
        self.slider_left.setObjectName("slider_left")
        self.verticalLayout_3.addWidget(self.slider_left)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_right = QtWidgets.QLabel(self.tab)
        self.label_right.setMinimumSize(QtCore.QSize(0, 20))
        self.label_right.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_right.setObjectName("label_right")
        self.verticalLayout_4.addWidget(self.label_right)
        self.slider_right = QtWidgets.QSlider(self.tab)
        self.slider_right.setMinimumSize(QtCore.QSize(0, 20))
        self.slider_right.setMaximumSize(QtCore.QSize(16777215, 20))
        self.slider_right.setStyleSheet("")
        self.slider_right.setOrientation(QtCore.Qt.Horizontal)
        self.slider_right.setObjectName("slider_right")
        self.verticalLayout_4.addWidget(self.slider_right)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        self.table_calc = QtWidgets.QTableWidget(self.tab_2)
        self.table_calc.setMinimumSize(QtCore.QSize(500, 200))
        self.table_calc.setObjectName("table_calc")
        self.table_calc.setColumnCount(0)
        self.table_calc.setRowCount(0)
        self.verticalLayout_9.addWidget(self.table_calc)
        self.table_r = QtWidgets.QTableWidget(self.tab_2)
        self.table_r.setMinimumSize(QtCore.QSize(500, 200))
        self.table_r.setObjectName("table_r")
        self.table_r.setColumnCount(0)
        self.table_r.setRowCount(0)
        self.verticalLayout_9.addWidget(self.table_r)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setMinimumSize(QtCore.QSize(500, 0))
        self.label_18.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_11.addWidget(self.tabWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setMinimumSize(QtCore.QSize(0, 24))
        self.button1.setMaximumSize(QtCore.QSize(16777215, 24))
        self.button1.setObjectName("button1")
        self.horizontalLayout_5.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setMinimumSize(QtCore.QSize(0, 24))
        self.button2.setMaximumSize(QtCore.QSize(16777215, 24))
        self.button2.setObjectName("button2")
        self.horizontalLayout_5.addWidget(self.button2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setObjectName("button4")
        self.horizontalLayout_5.addWidget(self.button4)
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setObjectName("button5")
        self.horizontalLayout_5.addWidget(self.button5)
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setObjectName("button6")
        self.horizontalLayout_5.addWidget(self.button6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработка данных датчиков"))
        self.label_21.setText(_translate("MainWindow", "Сдвиг времени измерения в днях"))
        self.label_left.setText(_translate("MainWindow", "Начало измерений"))
        self.label_right.setText(_translate("MainWindow", "Конец измерений"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Исходные данные"))
        self.label_2.setText(_translate("MainWindow", "Наименование конструкции"))
        self.label.setText(_translate("MainWindow", "Номер конструкции"))
        self.label_18.setText(_translate("MainWindow", "График показаний датчиков"))
        self.label_19.setText(_translate("MainWindow", "График сопротивлений теплопередаче"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Обработанные данные"))
        self.button1.setText(_translate("MainWindow", "Импорт файла Excel"))
        self.button2.setText(_translate("MainWindow", "Импорт файла с потока"))
        self.button4.setText(_translate("MainWindow", "Сохранить"))
        self.button5.setText(_translate("MainWindow", "Открыть"))
        self.button6.setText(_translate("MainWindow", "Экспорт в Word"))