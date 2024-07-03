import sys
from PyQt5.QtWidgets import (
	 QMainWindow,
	 QApplication,
	 QPushButton,
	 QVBoxLayout,
	 QWidget,
	 QCheckBox,
	 QGroupBox,
	 QRadioButton
)
from PyQt5 import QtCore, QtTest

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

		# remove checkbox
		self.checkbox = QCheckBox("Show/Hide")
		self.checkbox.stateChanged.connect(self.show_hide)

		self.button2 = QPushButton("Change color")
		self.button2.clicked.connect(self.change_color)
		self.color_data = list(matplotlib.colors._colors_full_map.values())
		self.color = 0

		self.data = [0.1 * random.random() for i in range(10)]
		
		self.groupBox = QGroupBox("asdf")
		self.radio1 = QRadioButton("&Radio button 1")
		self.radio2 = QRadioButton("R&adio button 2")
		self.radio3 = QRadioButton("Ra&dio button 3")
		
		self.radio1.setChecked(True)

		vbox = QVBoxLayout()
		vbox.addWidget(self.radio1)
		vbox.addWidget(self.radio2)
		vbox.addWidget(self.radio3)
		vbox.addStretch(1)
		self.groupBox.setLayout(vbox)

		layout.addWidget(self.toolbar)
		layout.addWidget(self.canvas)
		layout.addWidget(self.button)
		#layout.addWidget(self.checkbox)
		layout.addWidget(self.button2)

		widget = QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)

	def plot(self):
		self.data = [0.1 * random.random() for i in range(10)]
		self.reload_graph()

	def show_hide(self):
		if self.checkbox.isChecked():
			self.canvas.hide()
			#self.checkbox.setText("Checked")
		else:
			#QtCore.QTimer.singleShot(3000, lambda: self.canvas.show()) 
			self.canvas.show()
			#self.checkbox.setText("Unchecked")

	def change_color(self):
		# add rave mode
		modifiers = QApplication.keyboardModifiers()
		if modifiers == QtCore.Qt.ShiftModifier: num = 30
		
		else: num = 1

		for i in range(num):
			self.color = (self.color + (1 if num == 1 else random.randint(0, len(self.color_data)))) % len(self.color_data)
			self.reload_graph()
			QtTest.QTest.qWait(5)

	def reload_graph(self):
		self.figure.clear()
		ax = self.figure.add_subplot(111)
		ax.plot(self.data, '-', color=self.color_data[self.color])
		self.canvas.draw()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

