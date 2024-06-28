import sys
from PyQt5.QtWidgets import (
	 QMainWindow,
	 QApplication,
	 QPushButton,
	 QVBoxLayout,
	 QWidget,
	 QCheckBox
)
from PyQt5 import QtCore

import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt
import random

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("PVSL Temperature and Pressure")
		layout = QVBoxLayout()
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)

		self.button = QPushButton("Plot")
		self.button.clicked.connect(self.plot)

		self.checkbox = QCheckBox("Show/Hide")
		self.checkbox.stateChanged.connect(self.show_hide)

		self.data = [0.1 * random.random() for i in range(10)]

		layout.addWidget(self.toolbar)
		layout.addWidget(self.canvas)
		layout.addWidget(self.button)
		layout.addWidget(self.checkbox)

		widget = QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)

	def plot(self):
		self.data = [0.1 * random.random() for i in range(10)]
		self.figure.clear()
		ax = self.figure.add_subplot(111)
		ax.plot(self.data, '-r')
		self.canvas.draw()

	def show_hide(self):
		if self.checkbox.isChecked():
			self.canvas.hide()
		else:
			#QtCore.QTimer.singleShot(3000, lambda: self.canvas.show()) 
			self.canvas.show()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

