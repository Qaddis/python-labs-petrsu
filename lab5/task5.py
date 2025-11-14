import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from task5_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # - Хранилище -
        self.calc_expression = "0"

        # Инициализация интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация действий при нажатии на кнопки
        self.initButtonActions()

    def initButtonActions(self):
        num_buttons = [
            self.ui.numButton_0, self.ui.numButton_1, self.ui.numButton_2,
            self.ui.numButton_3, self.ui.numButton_4, self.ui.numButton_5,
            self.ui.numButton_6, self.ui.numButton_7, self.ui.numButton_8,
            self.ui.numButton_9
        ]
        
        self.ui.numButton_point.clicked.connect(self.calc_add_point)
        
        action_buttons = [
            self.ui.actionButton_add, self.ui.actionButton_subtract,
            self.ui.actionButton_multiply, self.ui.actionButton_divide
        ]
        
        for btn in num_buttons:
            btn.clicked.connect(self.calc_add_num)
            
        for btn in action_buttons:
            btn.clicked.connect(self.calc_add_action)
        
        self.ui.generalButton_clear.clicked.connect(self.calc_clear)
        self.ui.generalButton_result.clicked.connect(self.calc_result)
        
    def calc_add_num(self):
        btn_value = self.sender().text()
        
        if self.calc_expression == '0' and len(self.calc_expression) == 1:
            self.calc_expression = str(btn_value)
        else:
            self.calc_expression += btn_value
        
        self.calc_update_display()

    def calc_add_point(self):
        actions = ["+", "-", "*", "/", ","]
        
        expr = self.calc_expression.replace(" ", "")
        
        if expr[-1] not in actions:
            self.calc_expression += ","
        elif expr[-1] == ",":
            return
        else:
            self.calc_expression = self.calc_expression[:-3] +  ","
        
        self.calc_update_display()

    def calc_add_action(self):
        actions = ["+", "-", "*", "/", ","]
        
        value = " " + self.sender().text() + " "
        
        expr = self.calc_expression.replace(" ", "")
        
        if expr[-1] not in actions:
            self.calc_expression += value
        else:
            self.calc_expression = self.calc_expression[:-3 if expr[-1] != "," else -1] + value
            
        self.calc_update_display()

    def calc_clear(self):
        self.calc_expression = "0"
        
        self.calc_update_display()

    def calc_result(self):
        expr = self.calc_expression.replace(" ", "").replace(",", ".")
        
        self.calc_expression = str(eval(expr)).replace(".", ",")
        
        self.calc_update_display()

    def calc_update_display(self):
         self.ui.expression_label.setText(self.calc_expression)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
