import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from MainWindow import Ui_MainWindow
from DurationDialog import Ui_Duration

#from enum import Enum

#state_t = Enum("state_t", "waiting running paused reset")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    The main application window, containing the controls and the matplotlib graph
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("PV Testing")
        self.save.clicked.connect(self.save_file_dialog)
        self.run_pause.clicked.connect(self.control_button_pressed)
        self.reset_stop.clicked.connect(self.control_button_pressed)
        self.controls_settings_tab.tabBarClicked.connect(self.update_datetime)
        self.duration.currentIndexChanged.connect(self.open_DurationDialog)

        # add DurationDialog
        self.dialog = DurationDialog(self)

        # duration of the test
        self.timer_duration = 30

        # different file formats to be saved
        self.file_format = {
            "CSV Files (*.csv)": ".csv",
            "Text Files (*.txt)": ".txt"
        }

        self.current_state = "waiting"

        self.plot([1, 5, 2, 3, 5, 1, 4])

    def control_button_pressed(self):
        """
        Functionality for the start/stop control buttons
        """
        # run/pause, reset/stop
        object_name = self.focusWidget().objectName()
                    
        if self.current_state == "waiting" and object_name == "run_pause":
            self.run_pause.setText("Pause")
            self.reset_stop.setText("Stop")
            self.current_state = "running"
        elif self.current_state == "running" and object_name == "run_pause":
            self.run_pause.setText("Resume")
            self.current_state = "paused"
        elif self.current_state == "paused" and object_name == "run_pause":
            self.run_pause.setText("Pause")
            self.current_state = "running"
        elif object_name == "reset_stop" and self.current_state in ["running", "paused"]:
            self.run_pause.setText("Start")
            self.reset_stop.setText("Reset")
            self.current_state = "waiting"


    def save_file_dialog(self):
        """
        Saves the test results to a file specified by filepath
        """
        # open file dialog
        current_QDate = QtCore.QDate.currentDate()
        name_type = "PV_{}_{}_{}".format(current_QDate.month(),
                                         current_QDate.day(),
                                         current_QDate.year())
        fname, ftype = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget, "Save File", name_type,
            "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)")

        fname = str(fname)
        ftype = str(ftype)

        if fname == '': return

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

    def update_datetime(self):
        """
        Updates the app datetime to match the internal on Raspberry Pi
        """
        current_QDate = QtCore.QDate.currentDate()
        current_QTime = QtCore.QTime.currentTime()
        self.date_time.setDate(current_QDate)
        self.date_time.setTime(current_QTime)

    def open_DurationDialog(self, arg):
        """
        Define the amount of time for the test
        """
        timer_duration_dict = {
            0: (-1,0),
            1: (0,10),
            2: (0,20),
            3: (0,30),
            4: (0,45),
            5: (1,0),
            6: (2,0),
            7: (4,0),
            8: (10,0)
        }
        if arg == 9:
            if self.dialog.exec():
                self.timer_duration = self.dialog.get_duration()
                hr_str = '' if self.timer_duration[0] == 0 else f"{self.timer_duration[0]}hr "
                min_str = '' if self.timer_duration[1] == 0 else f"{self.timer_duration[1]}min"
                self.duration.setItemText(arg, hr_str + min_str)
        else:
            self.timer_duration = timer_duration_dict[arg]
            self.duration.setItemText(9, "Custom...")
        print(arg, self.timer_duration)

    def plot(self, num):
        """
        Plots array num to the canvas
        """
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(num)
        self.canvas.draw()


class DurationDialog(QtWidgets.QDialog):
    """
    Dialog that pops up when "Custom" option is selected for duration.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Duration()
        self.ui.setupUi(self)
        self.setWindowTitle("Set Duration")
        self.ui.minute_box.setMaximum(59)
        self.ui.cancel_ok.accepted.connect(self.get_duration)

    def get_duration(self):
        """
        Return the spinbox values for hour and time as a tuple.
        """
        return (self.ui.hour_box.value(), self.ui.minute_box.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # as opposed to window.show(), opens on fullscreen
    window.showMaximized()
    #window.show()
    sys.exit(app.exec_())
"""
NOTE: pyqtgraph might be faster than matplotlib, worth checking out?
NOTE: use > yapf -i main.py to autoformat according to pep8 formatting 
NOTE: use > pylint main.py to check the readability of the code
NOTE: generating image with scipy and then updating a Qt image widget might be faster
      check John's "Signal Delay System" repository
"""
