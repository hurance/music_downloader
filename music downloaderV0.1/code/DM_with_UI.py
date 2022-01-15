from Download_Mutiple_Source import QQ_music,wangyy
from muisc_downloader import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)

        self.music_info = []

        self.init()

        self.selt = self.comboBox.currentIndex()+1

        self.current_page = 1

        self.all_page = 0

        self.search_music = ""

        self.re = 1

        self.select_download = []

        self.music_num = 0

    def init(self):
        # 设置窗口名字
        self.setWindowTitle("Music Downloader")

        self.pushButton.clicked.connect(self.search)

        self.pushButton_5.clicked.connect(self.next_page)
        self.pushButton_5.setEnabled(False)

        self.pushButton_4.clicked.connect(self.pre_page)
        self.pushButton_4.setEnabled(False)

        self.pushButton_3.clicked.connect(self.first_page)
        self.pushButton_3.setEnabled(False)

        self.pushButton_6.clicked.connect(self.last_page)
        self.pushButton_6.setEnabled(False)

        self.comboBox.currentTextChanged.connect(self.change_source)

        self.pushButton_2.clicked.connect(self.download)

        self.tableWidget.itemClicked.connect(self.select_music_id)

    def select_music_id(self):
        self.pushButton_2.setText("下载")
        for i in range(len(self.select_download)):
            if self.tableWidget.currentItem() in self.select_download[i]:
                self.music_num = i+1

    def download(self):
        if self.selt == 1:
            Q1 = QQ_music(self.search_music)
            Q1.search()
            Q1.sel = self.music_num
            Q1.keepit()
            if Q1.purl:
                self.pushButton_2.setText("下载成功！")
            else:
                self.pushButton_2.setText("vip歌曲，无法下载")
        elif self.selt == 2:
            W1 = wangyy(self.search_music)
            W1.search()
            W1.sel = self.music_num
            W1.keepit()
            self.pushButton_2.setText("下载成功！")

    def change_source(self):
        self.pushButton_2.setText("下载")
        self.select_download = []

    def next_page(self):
        if self.current_page != self.all_page:
            self.pushButton_4.setEnabled(True)
            self.current_page += 1
            self.label_4.setText(str(self.current_page))

            for i in range((self.current_page-1)*10, self.current_page*10):
                self.select_download.append([])
                if self.music_info[i]:
                    for j in range(4):
                        if j == 0:
                            newItem = QTableWidgetItem(str(i+1))
                            self.tableWidget.setItem(i-(self.current_page-1)*10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 1:
                            newItem = QTableWidgetItem(str(self.music_info[i][1]))
                            self.tableWidget.setItem(i-(self.current_page-1)*10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 2:
                            newItem = QTableWidgetItem("")
                            self.tableWidget.setItem(i-(self.current_page-1)*10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 3:
                            newItem = QTableWidgetItem(str(self.music_info[i][2]))
                            self.tableWidget.setItem(i-(self.current_page-1)*10, j, newItem)
                            self.select_download[i].append(newItem)
                else:
                    for j in range(4):
                        newItem = QTableWidgetItem("")
                        self.tableWidget.setItem(i-(self.current_page-1)*10, j, newItem)
                        self.select_download[i].append(newItem)

        else:
            self.pushButton_5.setEnabled(False)

    def pre_page(self):
        if self.current_page != 1:
            self.pushButton_5.setEnabled(True)
            self.current_page -= 1
            self.label_4.setText(str(self.current_page))

            for i in range((self.current_page - 1) * 10, self.current_page * 10):
                self.select_download.append([])
                if self.music_info[i]:
                    for j in range(4):
                        if j == 0:
                            newItem = QTableWidgetItem(str(i + 1))
                            self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 1:
                            newItem = QTableWidgetItem(str(self.music_info[i][1]))
                            self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 2:
                            newItem = QTableWidgetItem("")
                            self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                            self.select_download[i].append(newItem)
                        elif j == 3:
                            newItem = QTableWidgetItem(str(self.music_info[i][2]))
                            self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                            self.select_download[i].append(newItem)
                else:
                    for j in range(4):
                        newItem = QTableWidgetItem("")
                        self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                        self.select_download[i].append(newItem)

        else:
            self.pushButton_4.setEnabled(False)

    def first_page(self):
        self.current_page = 1
        self.label_4.setText(str(self.current_page))

        for i in range(10):
            self.select_download.append([])
            for j in range(4):
                if j == 0:
                    newItem = QTableWidgetItem(str(i + 1))
                    self.tableWidget.setItem(i, j, newItem)
                    self.select_download[i].append(newItem)
                elif j == 1:
                    newItem = QTableWidgetItem(str(self.music_info[i][1]))
                    self.tableWidget.setItem(i, j, newItem)
                    self.select_download[i].append(newItem)
                elif j == 2:
                    newItem = QTableWidgetItem("")
                    self.tableWidget.setItem(i, j, newItem)
                    self.select_download[i].append(newItem)
                elif j == 3:
                    newItem = QTableWidgetItem(str(self.music_info[i][2]))
                    self.tableWidget.setItem(i, j, newItem)
                    self.select_download[i].append(newItem)

    def last_page(self):
        self.current_page = self.all_page
        self.label_4.setText(str(self.current_page))

        for i in range((self.current_page - 1) * 10, self.current_page * 10):
            self.select_download.append([])
            if self.music_info[i]:
                for j in range(4):
                    if j == 0:
                        newItem = QTableWidgetItem(str(i + 1))
                        self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j ==1:
                        newItem = QTableWidgetItem(str(self.music_info[i][1]))
                        self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j == 2:
                        newItem = QTableWidgetItem("")
                        self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j == 3:
                        newItem = QTableWidgetItem(str(self.music_info[i][2]))
                        self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                        self.select_download[i].append(newItem)
            else:
                for j in range(4):
                    newItem = QTableWidgetItem("")
                    self.tableWidget.setItem(i - (self.current_page - 1) * 10, j, newItem)
                    self.select_download[i].append(newItem)

    def search(self):
        self.selt = self.comboBox.currentIndex()+1
        self.search_music = self.lineEdit.text()
        if self.selt == 1 and self.search_music:
            self.pushButton_5.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_6.setEnabled(True)

            Q1 = QQ_music(self.search_music)
            Q1.search()
            self.music_info = Q1.song_info
            for i in range(len(self.music_info)):
                self.select_download.append([])
                for j in range(4):
                    newItem = QTableWidgetItem(str(self.music_info[i][j]))
                    self.tableWidget.setItem(i, j, newItem)
                    self.select_download[i].append(newItem)

            self.label_4.setText(str(self.current_page))
            self.all_page = len(self.music_info)//10
            self.label_6.setText(str(self.all_page))

        elif self.selt == 2 and self.search_music:
            self.pushButton_5.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_6.setEnabled(True)

            W1 = wangyy(self.search_music)
            W1.search()
            self.music_info = W1.music_info
            for i in range(10):
                self.select_download.append([])
                for j in range(4):
                    if j == 0:
                        newItem = QTableWidgetItem(str(i+1))
                        self.tableWidget.setItem(i, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j ==1:
                        newItem = QTableWidgetItem(str(self.music_info[i][1]))
                        self.tableWidget.setItem(i, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j == 2:
                        newItem = QTableWidgetItem("")
                        self.tableWidget.setItem(i, j, newItem)
                        self.select_download[i].append(newItem)
                    elif j == 3:
                        newItem = QTableWidgetItem(str(self.music_info[i][2]))
                        self.tableWidget.setItem(i, j, newItem)
                        self.select_download[i].append(newItem)

            self.label_4.setText(str(self.current_page))
            self.all_page = len(self.music_info) // 10
            self.label_6.setText(str(self.all_page))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ITN = window()
    ITN.show()
    sys.exit(app.exec_())