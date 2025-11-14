from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 550)
        MainWindow.setMinimumSize(QtCore.QSize(372, 550))
        MainWindow.setMaximumSize(QtCore.QSize(372, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #212121;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.expression_label = QtWidgets.QLabel(self.centralwidget)
        self.expression_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.expression_label.setFont(font)
        self.expression_label.setStyleSheet(
            "color: #eaebed;\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "background-color: #2b2a2b;"
        )
        self.expression_label.setObjectName("expression_label")
        self.verticalLayout.addWidget(self.expression_label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.numButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_4.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_4.setFont(font)
        self.numButton_4.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_4.setDefault(False)
        self.numButton_4.setObjectName("numButton_4")
        self.gridLayout.addWidget(self.numButton_4, 1, 0, 1, 1)
        self.numButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_6.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_6.setFont(font)
        self.numButton_6.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_6.setDefault(False)
        self.numButton_6.setObjectName("numButton_6")
        self.gridLayout.addWidget(self.numButton_6, 1, 2, 1, 1)
        self.numButton_point = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_point.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_point.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_point.setFont(font)
        self.numButton_point.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_point.setDefault(False)
        self.numButton_point.setObjectName("numButton_point")
        self.gridLayout.addWidget(self.numButton_point, 3, 2, 1, 1)
        self.actionButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton_add.setMinimumSize(QtCore.QSize(80, 80))
        self.actionButton_add.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.actionButton_add.setFont(font)
        self.actionButton_add.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "background-color: #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.actionButton_add.setDefault(False)
        self.actionButton_add.setObjectName("actionButton_add")
        self.gridLayout.addWidget(self.actionButton_add, 0, 3, 1, 1)
        self.numButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_9.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_9.setFont(font)
        self.numButton_9.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_9.setDefault(False)
        self.numButton_9.setObjectName("numButton_9")
        self.gridLayout.addWidget(self.numButton_9, 0, 2, 1, 1)
        self.numButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_2.setFont(font)
        self.numButton_2.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_2.setDefault(False)
        self.numButton_2.setObjectName("numButton_2")
        self.gridLayout.addWidget(self.numButton_2, 2, 1, 1, 1)
        self.generalButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.generalButton_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.generalButton_clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.generalButton_clear.setFont(font)
        self.generalButton_clear.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #91162c;\n"
            "color: #91162c;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "color: #eaebed;\n"
            "background-color: #91162c;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #7a0d21;\n"
            "}"
        )
        self.generalButton_clear.setDefault(False)
        self.generalButton_clear.setObjectName("generalButton_clear")
        self.gridLayout.addWidget(self.generalButton_clear, 3, 0, 1, 1)
        self.numButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_8.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_8.setFont(font)
        self.numButton_8.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )

        self.numButton_8.setDefault(False)
        self.numButton_8.setObjectName("numButton_8")
        self.gridLayout.addWidget(self.numButton_8, 0, 1, 1, 1)
        self.actionButton_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton_subtract.setMinimumSize(QtCore.QSize(80, 80))
        self.actionButton_subtract.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.actionButton_subtract.setFont(font)
        self.actionButton_subtract.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "background-color: #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.actionButton_subtract.setDefault(False)
        self.actionButton_subtract.setObjectName("actionButton_subtract")
        self.gridLayout.addWidget(self.actionButton_subtract, 1, 3, 1, 1)
        self.actionButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton_multiply.setMinimumSize(QtCore.QSize(80, 80))
        self.actionButton_multiply.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.actionButton_multiply.setFont(font)
        self.actionButton_multiply.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "background-color: #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.actionButton_multiply.setDefault(False)
        self.actionButton_multiply.setObjectName("actionButton_multiply")
        self.gridLayout.addWidget(self.actionButton_multiply, 2, 3, 1, 1)
        self.actionButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton_divide.setMinimumSize(QtCore.QSize(80, 80))
        self.actionButton_divide.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.actionButton_divide.setFont(font)
        self.actionButton_divide.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "background-color: #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.actionButton_divide.setDefault(False)
        self.actionButton_divide.setObjectName("actionButton_divide")
        self.gridLayout.addWidget(self.actionButton_divide, 3, 3, 1, 1)
        self.numButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_5.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_5.setFont(font)
        self.numButton_5.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_5.setDefault(False)
        self.numButton_5.setObjectName("numButton_5")
        self.gridLayout.addWidget(self.numButton_5, 1, 1, 1, 1)
        self.numButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_7.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_7.setFont(font)
        self.numButton_7.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_7.setDefault(False)
        self.numButton_7.setObjectName("numButton_7")
        self.gridLayout.addWidget(self.numButton_7, 0, 0, 1, 1)
        self.numButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_1.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_1.setFont(font)
        self.numButton_1.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_1.setDefault(False)
        self.numButton_1.setObjectName("numButton_1")
        self.gridLayout.addWidget(self.numButton_1, 2, 0, 1, 1)
        self.numButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_3.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_3.setFont(font)
        self.numButton_3.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_3.setDefault(False)
        self.numButton_3.setObjectName("numButton_3")
        self.gridLayout.addWidget(self.numButton_3, 2, 2, 1, 1)
        self.numButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.numButton_0.setMinimumSize(QtCore.QSize(80, 80))
        self.numButton_0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.numButton_0.setFont(font)
        self.numButton_0.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #2b2a2b;\n"
            "color: #eaebed;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #262526;\n"
            "}"
        )
        self.numButton_0.setDefault(False)
        self.numButton_0.setObjectName("numButton_0")
        self.gridLayout.addWidget(self.numButton_0, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.generalButton_result = QtWidgets.QPushButton(self.centralwidget)
        self.generalButton_result.setMinimumSize(QtCore.QSize(0, 80))
        self.generalButton_result.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.generalButton_result.setFont(font)
        self.generalButton_result.setStyleSheet(
            "QPushButton {\n"
            "padding: 5px;\n"
            "border-radius: 10px;\n"
            "border: 1px solid #6834d9;\n"
            "color: #6834d9;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "color: #eaebed;\n"
            "background-color: #6834d9;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: #5d2fc2;\n"
            "}"
        )
        self.generalButton_result.setDefault(False)
        self.generalButton_result.setObjectName("generalButton_result")
        self.verticalLayout.addWidget(self.generalButton_result)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Task 5 | Python Lab5"))
        self.expression_label.setText(_translate("MainWindow", "0"))
        self.numButton_4.setText(_translate("MainWindow", "4"))
        self.numButton_6.setText(_translate("MainWindow", "6"))
        self.numButton_point.setText(_translate("MainWindow", ","))
        self.actionButton_add.setText(_translate("MainWindow", "+"))
        self.numButton_9.setText(_translate("MainWindow", "9"))
        self.numButton_2.setText(_translate("MainWindow", "2"))
        self.generalButton_clear.setText(_translate("MainWindow", "C"))
        self.numButton_8.setText(_translate("MainWindow", "8"))
        self.actionButton_subtract.setText(_translate("MainWindow", "-"))
        self.actionButton_multiply.setText(_translate("MainWindow", "*"))
        self.actionButton_divide.setText(_translate("MainWindow", "/"))
        self.numButton_5.setText(_translate("MainWindow", "5"))
        self.numButton_7.setText(_translate("MainWindow", "7"))
        self.numButton_1.setText(_translate("MainWindow", "1"))
        self.numButton_3.setText(_translate("MainWindow", "3"))
        self.numButton_0.setText(_translate("MainWindow", "0"))
        self.generalButton_result.setText(_translate("MainWindow", "="))

    def add_functions(self):
        pass
