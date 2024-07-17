#-----------------------------------------------------------------------
# PlotWidget.py
#
# Adds functionality to plotting widgets. Note: with matplotlib,
# realtime graphing gets annoying to set up.
#-----------------------------------------------------------------------

import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import matplotlib
matplotlib.use('Agg')
import numpy as np
from random import randrange

class PlotWidget():
	def __init__(self, MainWindow):
		self.MainWindow = MainWindow
		self.x_data = [1, 2, 3, 4]
		self.y_data = [10, 1, 5, 10]
		
	def clear(self):
		self.MainWindow.figure.clear()
		
	def update(self, frame):
		pass
	
	def anim_plot(self):
		pass
		# Cannot use 'Agg' and figure
		# Need figure to plot rt
	
	def plot(self, *args):
		self.MainWindow.figure.clear()
		ax = matplotlib.pyplot.subplot()
		ax.plot(*args)
