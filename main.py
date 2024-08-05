import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from DurationDialog import Ui_DurationDialog
import pyqtgraph

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        # Initialization
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Set window title of app
        self.setWindowTitle("PV Testing")
        
        # Functional save button
        self.save.clicked.connect(self.save_file_dialog)
        
        # Functional control buttons
        self.run_pause_btn.clicked.connect(self.control_button_pressed)
        self.reset_stop_btn.clicked.connect(self.control_button_pressed)
        self.curr_state = "waiting"
        
        
        # Functional datetime
        self.controls_settings_tab.tabBarClicked.connect(self.update_datetime)
        
        # Functional duration dialog
        self.duration_combobox.currentIndexChanged.connect(self.open_duration_dialog)
        self.dialog = DurationDialog(self)
        
        # Save file formats
        self.file_formats = {
            "CSV Files (*.csv)": ".csv",
            "Text Files (*.txt)": ".txt"
        }
        
        # Default test times
        self.curr_duration = 30
        self.timer_durations = {
            0: (-1, 0),
            1: (0, 10),
            2: (0, 20),
            3: (0, 30),
            4: (0, 45),
            5: (1, 0),
            6: (2, 0),
            7: (4, 0),
            8: (10, 0)
        }
        
    def control_button_pressed(self):
        """
        Functionality for the start/stop and reset/stop control buttons
        """
        # Get the name of the widget, either run/pause or reset/stop
        object_name = self.focusWidget().objectName()

        # Toggle between paused and running if the program has been started
        if self.curr_state == "waiting" and object_name == "run_pause_btn":
            self.run_pause_btn.setText("Pause")
            self.reset_stop_btn.setText("Stop")
            self.curr_state = "running"
        elif self.curr_state == "running" and object_name == "run_pause_btn":
            self.run_pause_btn.setText("Resume")
            self.curr_state = "paused"
        elif self.curr_state == "paused" and object_name == "run_pause_btn":
            self.run_pause_btn.setText("Pause")
            self.curr_state = "running"
        elif object_name == "reset_stop_btn" and self.curr_state in [
                "running", "paused"
        ]:
            self.run_pause_btn.setText("Start")
            self.reset_stop_btn.setText("Reset")
            self.curr_state = "waiting"
            
    def save_file_dialog(self):
        """
        Saves the test results to a file specified by filepath
        """
        # Get the current date from Qt library
        current_QDate = QtCore.QDate.currentDate()

        # Create the file name based off of the current day
        name_type = "PV_{}_{}_{}".format(current_QDate.month(),
                                         current_QDate.day(),
                                         current_QDate.year())

        # Get the file name and type from the line editor in the dialog
        fname, ftype = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget, "Save File", name_type,
            "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)")

        fname = str(fname)
        ftype = str(ftype)

        if fname == '': return

        # Iterate through file formats and see if match in file name
        for file_format in self.file_format.values():
            if file_format in fname:
                ftype = ''
                break
        else:
            ftype = self.file_format[ftype]

        # Combine the name and extension
        full = fname + ftype

        # Open file using given name and extension
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
        # Get the current datetime from QtCore library
        current_QDate = QtCore.QDate.currentDate()
        current_QTime = QtCore.QTime.currentTime()
        self.date_time.setDate(current_QDate)
        self.date_time.setTime(current_QTime)

    def open_duration_dialog(self, arg):
        """
        Define the amount of time for the test
        """

        # Functionality for "Custom..." argument
        if arg == 9:

            # Open dialog, save result and change text to custom duration
            if self.dialog.exec():
                self.timer_duration = self.dialog.get_duration()
                hr_str = '' if self.timer_duration[
                    0] == 0 else f"{self.timer_duration[0]}hr "
                min_str = '' if self.timer_duration[
                    1] == 0 else f"{self.timer_duration[1]}min"
                self.duration_combobox.setItemText(arg, hr_str + min_str)
        else:

            # Argument indexes dictionary
            self.timer_duration = self.timer_duration_dict[arg]
            self.duration_combobox.setItemText(9, "Custom...")
        print(arg, self.timer_duration)
        
    def get_duration(self):
        """
        Return the spinbox values for hour and time as a tuple.
        """
        return (self.ui.hour_spinbox.value(), self.ui.minute_spinbox.value())

class DurationDialog(QtWidgets.QDialog):
    """
    Dialog that pops up when "Custom" option is selected for duration.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DurationDialog()
        self.ui.setupUi(self)

        # Set dialog window title
        self.setWindowTitle("Set Duration")
        self.ui.minute_spinbox.setMaximum(59)
        self.ui.cancel_ok.accepted.connect(self.get_duration)

    def get_duration(self):
        """
        Return the spinbox values for hour and time as a tuple.
        """
        return (self.ui.hour_spinbox.value(), self.ui.minute_spinbox.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
