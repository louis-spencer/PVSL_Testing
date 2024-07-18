#-----------------------------------------------------------------------
# MainWindow.py
#
# PyQt UI for the main window and dialog, provides all widgets and
# layouts
#-----------------------------------------------------------------------

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from MainWindow import MainWindow_ui
from DurationDialog import DurationDialog_ui
import matplotlib
from PlotWidget import PlotWidget


class MainWindow(QtWidgets.QMainWindow, MainWindow_ui):
    """
    The main application window, containing the controls and the matplotlib graph
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Set the window title of the application
        self.setWindowTitle("PV Testing")

        # Connect save button functionality
        self.save.clicked.connect(self.save_file_dialog)

        # Connect control button functionality
        self.run_pause.clicked.connect(self.control_button_pressed)
        self.reset_stop.clicked.connect(self.control_button_pressed)

        # Update datetime whenever tab is switched
        self.controls_settings_tab.tabBarClicked.connect(self.update_datetime)

        # Open dialog to choose test duration
        self.duration_combobox.currentIndexChanged.connect(
            self.open_duration_dialog)

        # Attach dialog to main
        self.dialog = DurationDialog(self)

        # File formats to be used when saving files
        self.file_format = {
            "CSV Files (*.csv)": ".csv",
            "Text Files (*.txt)": ".txt"
        }

        self.current_state = "waiting"
        self.timer_duration = 30

        # Dictionary with different default times
        self.timer_duration_dict = {
            # Formatted in (hours, minutes)
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
        
        # PlotWidget
        self.PlotWidget = PlotWidget(self)
        

    def control_button_pressed(self):
        """
        Functionality for the start/stop and reset/stop control buttons
        """
        # Get the name of the widget, either run/pause or reset/stop
        object_name = self.focusWidget().objectName()

        # Toggle between paused and running if the program has been started
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
        elif object_name == "reset_stop" and self.current_state in [
                "running", "paused"
        ]:
            self.run_pause.setText("Start")
            self.reset_stop.setText("Reset")
            self.current_state = "waiting"

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


class DurationDialog(QtWidgets.QDialog):
    """
    Dialog that pops up when "Custom" option is selected for duration.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = DurationDialog_ui()
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
    #.QApplication.setStyle(QtWidgets.QStyleFactory.create('gtk2'))
    window = MainWindow()

    # Opens window on fullscreen
    # TODO: fullscreen should cover taskbar
    window.showMaximized()
    #window.show()
    
    window.PlotWidget.plot([1, 2, 3, 4], [1, 5, 1, 5])
    
    sys.exit(app.exec_())
"""
NOTE: pyqtgraph might be faster than matplotlib, worth checking out?
NOTE: use > yapf -i main.py to autoformat according to pep8 formatting 
NOTE: use > pylint main.py to check the readability of the code
NOTE: generating image with scipy and then updating a Qt image widget might be faster
      check John's "Signal Delay System" repository
NOTE: import the preferred PyQt package before importing pyqtgraph as
	  it will force pyqtgraph to use the right package
TODO: create a PlotWidget.py file to handle graphing data in both matplotlib and pyqtgraph
      create different git branches to handle respectively
"""
