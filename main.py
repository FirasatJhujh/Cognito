from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton, QStackedWidget, QLabel, QFrame, QVBoxLayout,QGridLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys
from random import shuffle

class AppCute(QMainWindow):
    def __init__(self):
        super(AppCute,self).__init__()

        # Loading the file
        loadUi("interface.ui",self)

        # Adding the variables
        

        self.rule_slider_value = 0
        
        self.col_values = {
            0:['A','E','I','M','Q','U','Y'],
            1:['B','F','J','N','R','V','Z'],
            2:['C','G','K','O','S','W'," "],
            3:['D','H','L','P','T','X'," "],
            4:['0','0','0','0','0','0','0']}
        
        self.col_arranged_values = []
        self.col_btn_pressed_time = 0
        self.ordinal_numbers = {1:'first',2:'second',3:'third',4:'fourth',5:'fifth',6:'sixth',7:'seventh',8:'eight',9:'ninth',10:'tenth',11:'eleventh',12:"twelfth"}
        self.col_all_btns = [self.col_btn_1,self.col_btn_2,self.col_btn_3,self.col_btn_4]

        self.row_arranged_values = []
        self.row_all_count_label = list()
        self.row_btn_pressed_time = 0
        self.row_btn_pressed_times = []
        self.row_all_btns = [
            self.row_btn_1,self.row_btn_2,self.row_btn_3,
            self.row_btn_4,self.row_btn_5,self.row_btn_6,
            self.row_btn_7]
        self.characters = []

        # Adding the widget
        self.stacked_window = self.findChild(QStackedWidget,"stacked_window")
        self.welcome_start = self.findChild(QPushButton, "welcome_start")

        self.rule_slider = self.findChild(QSlider,"rule_slider")
        self.rule_next = self.findChild(QPushButton,"rule_next")

        self.col_heading = self.findChild(QLabel,"col_heading")
        self.col_btn_1 = self.findChild(QPushButton,"col_btn_1")
        self.col_btn_2 = self.findChild(QPushButton,"col_btn_2")
        self.col_btn_3 = self.findChild(QPushButton,"col_btn_3")
        self.col_btn_4 = self.findChild(QPushButton,"col_btn_4")
        self.col_count_label_1 = self.findChild(QLabel,"col_count_label_1")
        self.col_count_label_2 = self.findChild(QLabel,"col_count_label_2")
        self.col_count_label_3 = self.findChild(QLabel,"col_count_label_3")
        self.col_count_label_4 = self.findChild(QLabel,"col_count_label_4")
        self.col_count_all_labels = [self.col_count_label_1,self.col_count_label_2,self.col_count_label_3,self.col_count_label_4]
        self.col_next = self.findChild(QPushButton,"col_next")

        self.row_heading = self.findChild(QLabel,"row_heading")
        self.row_frame = self.findChild(QFrame,"row_frame")
        self.row_btn_1 = self.findChild(QPushButton,"row_btn_1")
        self.row_btn_2 = self.findChild(QPushButton,"row_btn_2")
        self.row_btn_3 = self.findChild(QPushButton,"row_btn_3")
        self.row_btn_4 = self.findChild(QPushButton,"row_btn_4")
        self.row_btn_5 = self.findChild(QPushButton,"row_btn_5")
        self.row_btn_6 = self.findChild(QPushButton,"row_btn_6")
        self.row_btn_7 = self.findChild(QPushButton,"row_btn_7")
        self.row_next = self.findChild(QPushButton,"row_next")
        self.row_grid_layout = self.findChild(QGridLayout,"row_grid_layout")

        self.output_word_area = self.findChild(QLabel,"output_word_area")
        self.output_play_again = self.findChild(QPushButton,"output_play_again")
        self.output_exit = self.findChild(QPushButton,"output_exit")

        # Adding the signals
        self.welcome_start.clicked.connect(self.welcome_over)

        self.rule_next.clicked.connect(self.rule_over)

        self.col_btn_1.clicked.connect(lambda:self.col_btn_pressed(0))
        self.col_btn_2.clicked.connect(lambda:self.col_btn_pressed(1))
        self.col_btn_3.clicked.connect(lambda:self.col_btn_pressed(2))
        self.col_btn_4.clicked.connect(lambda:self.col_btn_pressed(3))
        self.col_next.clicked.connect(self.col_over)

        self.row_btn_1.clicked.connect(lambda:self.row_btn_pressed(0))
        self.row_btn_2.clicked.connect(lambda:self.row_btn_pressed(1))
        self.row_btn_3.clicked.connect(lambda:self.row_btn_pressed(2))
        self.row_btn_4.clicked.connect(lambda:self.row_btn_pressed(3))
        self.row_btn_5.clicked.connect(lambda:self.row_btn_pressed(4))
        self.row_btn_6.clicked.connect(lambda:self.row_btn_pressed(5))
        self.row_btn_7.clicked.connect(lambda:self.row_btn_pressed(6))
        self.row_next.clicked.connect(self.row_over)

        self.output_play_again.clicked.connect(self.output_playAgain)
        self.output_exit.clicked.connect(self.close)
        # Applying properties before execute
        self.col_next.hide()

        self.row_next.hide()
        
        self.row_grid_layout.setSpacing(0)
        self.row_grid_layout.setContentsMargins(0,0,0,0)

        # Showing the main window
        self.show()

    def welcome_over(self):
        # Changing the page
        self.stacked_window.setCurrentIndex(1)
        # Seting focus on rule page's slider
        self.rule_slider.setFocus()

    def rule_over(self):
        # Storing the value  of horizontal slider
        self.rule_slider_value = self.rule_slider.value()
        # changing the page
        self.stacked_window.setCurrentIndex(2)

    def col_btn_pressed(self,col_no):
        # Noting that col_btn has pressed
        self.col_btn_pressed_time += 1
        # The times as ordinal number
        ordinal_value = self.ordinal_numbers.get(self.col_btn_pressed_time + 1)
        # Checking press is in range
        if (self.rule_slider_value > self.col_btn_pressed_time):
            # Changing the title of window
            self.col_heading.setText(f"In the following columns where is your {ordinal_value} character")
            # Getting the col's value by col no
            col_value = self.col_values.get(col_no)
            # Storing the col's value into list
            self.col_arranged_values.append(col_value) 
            # Increases the value of count label by 1
            self.col_count_value_increser(col_no,1)
        else:
            # Getting the col's value by col no
            col_value = self.col_values.get(col_no)
            # Storing the col's value into list
            self.col_arranged_values.append(col_value)
            # Showing the hided btn
            self.col_next.show()
            # Looping to disable all col btns
            for btn in self.col_all_btns:
                btn.setDisabled(True)
            # Increases the value of count label by 1
            self.col_count_value_increser(col_no,1)


    def col_count_value_increser(self,col_no,increase_by):
            # Getting the corresponding count label 
            label = self.col_count_all_labels[col_no]
            # Getting the value of corresponding count label as int
            label_value = int(label.text())
            # Increasing the value by one
            label_value += increase_by
            # Updating the value of label
            label.setText(str(label_value))


    def col_over(self):
        # Getting absents col's vlaue (1.getting the values which are absent in chosen columns from whole column) (2. Addinf the list 1 and list 2) (3.getting the values which are absent in whole from chosen columns)
        abs_cols = [values for values in self.col_values.values() if values not in self.col_arranged_values] + [values for values in self.col_arranged_values if values not in self.col_values.values()]

        # Append the absents columns in arrangment
        for abs_col in abs_cols:
            self.col_arranged_values.append(abs_col)
        
        # Append the values excluding last column
        for col_no, col_values in enumerate(self.col_arranged_values):
            # Itereating the column's list
            print(col_no,len(self.col_arranged_values))
            # Seprating the last column
            if (col_no != len(self.col_arranged_values) - 1):
                # CREating the inner frame for main frame
                frm = QFrame(self.row_frame)
                # adding the layout in inner frame(frm)
                layout = QVBoxLayout(frm)
                

                # Itreaing to put the values of columns in thier postions
                for col_value in col_values:
                    # Creating the label
                    lb= QLabel(col_value)
                    # seting horizontal elignment
                    lb.setAlignment(Qt.AlignCenter)
                    # Adding style to lable(lb)
                    lb.setStyleSheet('font: 20pt "Lucida Sans Unicode";')
                    # Appending the label(lb) into inner frame(frm)
                    layout.addWidget(lb)
                
            
            else:
                # CREating the inner frame for main frame
                frm = QFrame(self.row_frame)
                # adding the layout in inner frame(frm)
                layout = QVBoxLayout(frm)
                # Giving the layout space
                layout.setSpacing(20)
                # Itreaing to put the values of columns in thier postions
                for col_value in col_values:
                    # Creating the label
                    lb= QLabel(col_value)
                    # seting horizontal elignment
                    lb.setAlignment(Qt.AlignCenter)
                    # Assigning the max height
                    lb.setMaximumHeight(44)
                    # Adding style to lable(lb)
                    lb.setStyleSheet('font: 14pt "Trebuchet MS";background-color:#EAF6F6;color:grey;')
                    # Appending to li to access them
                    self.row_all_count_label.append(lb)
                    # Appending the label(lb) into inner frame(frm)
                    layout.addWidget(lb)
                
            # Adding the inner frame(frm) in grid layout
            self.row_grid_layout.addWidget(frm,1,col_no)

        # Changing the page
        self.stacked_window.setCurrentIndex(3)

        # Removing the absents columns in arrangment
        for abs_col in abs_cols:
            self.col_arranged_values.remove(abs_col)

    def row_btn_pressed(self,row):
        # Increase the push value to show that btn has pressed
        self.row_btn_pressed_time += 1
        # The times as ordinal number
        ordinal_value = self.ordinal_numbers.get(self.row_btn_pressed_time + 1)
        print(self.row_btn_pressed_time + 1,ordinal_value)
        # Checking press is in range
        if (self.rule_slider_value > self.row_btn_pressed_time):
            # Changing the title
            self.row_heading.setText(f"In the following row where is your {ordinal_value} character")
            # Taking the transpose of list of list
            self.row_swaped_values = [list(row) for row in zip(*self.col_arranged_values)]
            # Noting the pushes time
            self.row_btn_pressed_times.append(self.row_btn_pressed_time)
            # appending the row's value 
            self.row_arranged_values.append(self.row_swaped_values[row])

            # Updating the count label
            self.row_count_value_increser(row,increase_by=1)
        else:
            # Noting the pushes time
            self.row_btn_pressed_times.append(self.row_btn_pressed_time)
            # appending the row's value 
            self.row_arranged_values.append(self.row_swaped_values[row])
            # Updating the count label
            self.row_count_value_increser(row,increase_by=1)
            # Looping to disable all btns
            for btn in self.row_all_btns:
                btn.setDisabled(True)
            # Showing the see button
            self.row_next.show()

    def row_over(self):
        # Iterating the index of character
        for push in self.row_btn_pressed_times:
            # iterating the row
            for index, row in enumerate(self.row_arranged_values):
                # Checking that is that characatr which we need
                if (push-1) == index:
                    # appending the character into list
                    self.characters.append(row[push-1])
        # concatinating the characters to form word
        word = "".join(self.characters)
        # lowercasing all characters exclude first one
        word = word.title()
        # Changing the page
        self.stacked_window.setCurrentIndex(4)
        # Updating the label value
        self.output_word_area.setText(word)

    def output_playAgain(self):
        # Changing the window
        self.stacked_window.setCurrentIndex(0)
        # Giving the default value to rule's slider
        self.rule_slider.setValue(3)

        # giving default values to each col elements
        self.col_arranged_values = []
        self.col_btn_pressed_time = 0
        # Enabling all col_bnt
        for btn in self.col_all_btns:
            btn.setDisabled(False)
        # giving default value to all col count labels
        for lb in self.col_count_all_labels:
            lb.setText('0')

        # Changing the col page's heading title
        self.col_heading.setText(f"In the following column where is your first character")

        # giving default values to each col elements
        self.row_arranged_values = []
        self.row_all_count_label = list()
        self.row_btn_pressed_time = 0
        self.row_btn_pressed_times = []
        self.characters = []
        # Enabling all row btn
        for btn in self.row_all_btns:
            btn.setDisabled(False)
        # giving default value to all row count labels
        for lb in self.row_all_count_label:
            lb.setText('0')

        # Changing the row page's heading title
        self.row_heading.setText(f"In the following row where is your first character")
            
    def row_count_value_increser(self,row_no,increase_by):
        
        # Getting the corresponding count label 
        label = self.row_all_count_label[row_no]
        # Getting the value of corresponding count label as int
        label_value = int(label.text())
        # Increasing the value by one
        label_value += increase_by
        # Updating the value of label
        label.setText(str(label_value))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppCute()
    app.exec_()