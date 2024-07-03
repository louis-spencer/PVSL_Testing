import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.update_datetime()
        self.save.clicked.connect(self.save_file_dialog)

    def save_file_dialog(self):
        """
        Saves the test results to a file specified by filepath
        """
        # open file dialog
        current_QDate = QtCore.QDate.currentDate()
        print(current_QDate.day())
        name_type = "PV_{}_{}_{}".format(current_QDate.month(),
                                         current_QDate.day(),
                                         current_QDate.year())
        fname, ftype = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget, "Save File", name_type,
            "CSV Files(*.csv);;Text Files(*.txt);;All Files (*)")

        if fname:
            fname = str(fname)
            ftype = str(ftype)[-5:-1]
            name_type = fname + ftype
            with open(name_type, 'w') as f:
                f.write(name_type)
                f.close()
                
    def update_datetime(self):
        """
        Updates the app datetime to match the internal on Raspberry Pi
        """
        current_QDate = QtCore.QDate.currentDate()
        current_QTime = QtCore.QTime.currentTime()
        self.date_time.setDate(current_QDate)
        self.date_time.setTime(current_QTime)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# NOTE: pyqtgraph might be faster than matplotlib, worth checking out?
