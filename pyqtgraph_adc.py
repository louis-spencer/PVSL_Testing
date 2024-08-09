## NOTE: import the specific version of PyQt first
## This will force pyqtgraph to use the proper package
## (instead of searching for a different package)

from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum=1)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setLabel("left", "Pressure (PSI)")
        self.plot_graph.setLabel("bottom", "Time (s)")
        self.plot_graph.setYRange(0, 30)
        
        self.time = list(range(10))
        self.pressure = []
        for i in range(10):
            self.pressure.append(adc.read_adc(0, gain=1) * (4.096/2048) * (30/5) - 5)
        
        self.line = self.plot_graph.plot( self.time, self.pressure)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        
    def update_plot(self):
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.pressure = self.pressure[1:]
        self.pressure.append(adc.read_adc(0, gain=1) * (4.096/2048) * (30/5) - 5)
        self.line.setData(self.time, self.pressure)



app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()
