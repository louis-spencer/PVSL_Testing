import sys

# PyQt5 for the GUI and app dev
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from PyQt5 import QtCore, QtTest

# matplotlib for graphical processing
import matplotlib
# used for embedding into PyQt GUI
matplotlib.use('Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # create window
        
        self.setWindowTitle("PVSL Temperature and Pressure")
        # TODO work on custom layout
        layout = QVBoxLayout()
        
        # matplotlib, PyQT elements
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.toolbar)
        
        # PyQT elements
        # checkbox for which traces to enable/disable
        self.checkbox1 = QCheckBox(text="Pressure", parent=self)
        self.checkbox2 = QCheckBox(text="Temperature", parent=self)
        self.checkbox_list = [self.checkbox1, self.checkbox2]
        for c in self.checkbox_list:
            layout.addWidget(c)
            c.setChecked(True)
            c.clicked.connect(self.plot)
        self.temperature_checkbox = self.pressure_checkbox = True
        
        # TODO add buttons for setting the time
        
        # TODO add button to be able to export the data
        
        # TODO add tab buttons to change simulation settings
        
        # TODO add simulation settings, time presets + custom
        
        #print(dir(self))
    
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
        self.plot()
        
    def plot(self):
        #print(dir(self.checkbox1))
        img = plt.imread(".water.jpg")
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        if not (self.checkbox1.isChecked() or self.checkbox2.isChecked()):
            ax.imshow(img, extent=[0, 3, 0, 3])
        if self.checkbox1.isChecked():
            ax.plot([0, 1, 2, 3], [1, 2, 0, 3])
        if self.checkbox2.isChecked():
            ax.plot([0, 1, 2, 3], [3, 1, 2, 0])
        self.canvas.draw()
        #plt.show()
            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
        
        
