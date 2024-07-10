import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from MainWindow import Ui_MainWindow
from DurationDialog import Ui_Duration


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("PV Testing")
        self.save.clicked.connect(self.save_file_dialog)
        self.run_pause.clicked.connect(self.control_button_pressed)
        self.reset_stop.clicked.connect(self.control_button_pressed)
        self.controls_settings_tab.tabBarClicked.connect(self.update_datetime)
        self.duration.currentIndexChanged.connect(self.open_DurationDialog)

        self.file_format = {
            "CSV Files (*.csv)": ".csv",
            "Text Files (*.txt)": ".txt"
        }
        
        # states for app operation
        self.testing_states = {"waiting":0, "testing":1, "paused":2, "reset":3}
        # waiting to start, testing, paused, reset
        self.current_state = self.testing_states["waiting"]
        
        self.plot([1, 5, 2, 3, 5, 1, 4])
        
    def control_button_pressed(self):
        # run/pause, reset/stop
        object_name = self.focusWidget().objectName()
        print(object_name)
        
        
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
            "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)")
        
        fname = str(fname)
        ftype = str(ftype)
        
        for file_format in self.file_format.values():
            if file_format in fname:
                ftype = ''
                break
        else:
            ftype = self.file_format[ftype]
        # full name with extension
        full = fname + ftype
        
        # open file
        with open(full, 'w') as f:
            f.write(name_type)
            f.write('\n')
            f.write(QtCore.QDate.currentDate().toString())
            f.write(" at ")
            f.write(QtCore.QTime.currentTime().toString())
            f.close()
        

        #ftype = str(ftype)[-5:-1]
        #name_type = fname + ftype
        #with open(name_type, 'w') as f:
        #    f.write(name_type)
        #    f.close()

    def update_datetime(self, tabIndex=0):
        """
        Updates the app datetime to match the internal on Raspberry Pi
        """
        print("Updated")
        current_QDate = QtCore.QDate.currentDate()
        current_QTime = QtCore.QTime.currentTime()
        self.date_time.setDate(current_QDate)
        self.date_time.setTime(current_QTime)

    def open_DurationDialog(self, arg):
        if arg == 0: self.duration = -1
        # if self.duration = -1 then it runs until stopped
        # otherwise, time in minutes
        elif arg == 1: self.duration = 10
        elif arg == 2: self.duration = 20
        elif arg == 3: self.duration = 30
        elif arg == 4: self.duration = 45
        elif arg == 5: self.duration = 60
        elif arg == 6: self.duration = 75
        elif arg == 9:
            dialog = DurationDialog(self)
            dialog.exec()

    def plot(self, num):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(num)
        self.canvas.draw()


class DurationDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        print(parent)
        super().__init__(parent)
        self.ui = Ui_Duration()
        self.ui.setupUi(self)
        self.setWindowTitle("Set Duration")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # as opposed to window.show(), opens on fullscreen
    #window.showMaximized()
    window.show()
    sys.exit(app.exec_())
"""
NOTE: pyqtgraph might be faster than matplotlib, worth checking out?
NOTE: use > yapf -i main.py to autoformat according to pep8 formatting 
"""
