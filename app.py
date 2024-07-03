# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib

matplotlib.use('Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import matplotlib.pyplot as plt


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 690)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.controls_settings = QtWidgets.QHBoxLayout()
        self.controls_settings.setObjectName("controls_settings")
        self.controls_settings_tab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.controls_settings_tab.sizePolicy().hasHeightForWidth())
        self.controls_settings_tab.setSizePolicy(sizePolicy)
        self.controls_settings_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controls_settings_tab.setStyleSheet(u"QPushButton#reset_stop {\n"
                                                 "	color: red;	\n"
                                                 "}")
        self.controls_settings_tab.setTabPosition(QtWidgets.QTabWidget.East)
        self.controls_settings_tab.setObjectName("controls_settings_tab")
        self.controls_tab = QtWidgets.QWidget()
        self.controls_tab.setObjectName("controls_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.controls_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_and_system = QtWidgets.QLabel(self.controls_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graph_and_system.sizePolicy().hasHeightForWidth())
        self.graph_and_system.setSizePolicy(sizePolicy)
        self.graph_and_system.setStyleSheet("")
        self.graph_and_system.setScaledContents(False)
        self.graph_and_system.setWordWrap(True)
        self.graph_and_system.setObjectName("graph_and_system")
        self.verticalLayout.addWidget(self.graph_and_system)
        self.pv_test_controls = QtWidgets.QGroupBox(self.controls_tab)
        self.pv_test_controls.setMouseTracking(False)
        self.pv_test_controls.setAutoFillBackground(False)
        self.pv_test_controls.setStyleSheet("")
        self.pv_test_controls.setObjectName("pv_test_controls")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pv_test_controls)
        self.verticalLayout_4.setContentsMargins(9, 10, 9, -1)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.run_pause = QtWidgets.QPushButton(self.pv_test_controls)
        self.run_pause.setStyleSheet("")
        self.run_pause.setCheckable(False)
        self.run_pause.setDefault(False)
        self.run_pause.setObjectName("run_pause")
        self.verticalLayout_4.addWidget(self.run_pause)
        self.reset_stop = QtWidgets.QPushButton(self.pv_test_controls)
        self.reset_stop.setObjectName("reset_stop")
        self.verticalLayout_4.addWidget(self.reset_stop)
        self.time_remaining = QtWidgets.QLabel(self.pv_test_controls)
        self.time_remaining.setWordWrap(True)
        self.time_remaining.setObjectName("time_remaining")
        self.verticalLayout_4.addWidget(self.time_remaining)
        self.verticalLayout.addWidget(self.pv_test_controls)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.graph_controls = QtWidgets.QGroupBox(self.controls_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graph_controls.sizePolicy().hasHeightForWidth())
        self.graph_controls.setSizePolicy(sizePolicy)
        self.graph_controls.setObjectName("graph_controls")
        self.graph_settings_container = QtWidgets.QVBoxLayout(
            self.graph_controls)
        self.graph_settings_container.setContentsMargins(-1, 5, -1, 0)
        self.graph_settings_container.setSpacing(0)
        self.graph_settings_container.setObjectName("graph_settings_container")
        self.pressure_checkbox = QtWidgets.QCheckBox(self.graph_controls)
        self.pressure_checkbox.setStyleSheet("")
        self.pressure_checkbox.setIconSize(QtCore.QSize(24, 24))
        self.pressure_checkbox.setChecked(True)
        self.pressure_checkbox.setObjectName("pressure_checkbox")
        self.graph_settings_container.addWidget(self.pressure_checkbox)
        self.temperature_checkbox = QtWidgets.QCheckBox(self.graph_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.temperature_checkbox.sizePolicy().hasHeightForWidth())
        self.temperature_checkbox.setSizePolicy(sizePolicy)
        self.temperature_checkbox.setMinimumSize(QtCore.QSize(0, 0))
        self.temperature_checkbox.setChecked(True)
        self.temperature_checkbox.setObjectName("temperature_checkbox")
        self.graph_settings_container.addWidget(self.temperature_checkbox)
        self.legend_checkbox = QtWidgets.QCheckBox(self.graph_controls)
        self.legend_checkbox.setChecked(True)
        self.legend_checkbox.setObjectName("legend_checkbox")
        self.graph_settings_container.addWidget(self.legend_checkbox)
        self.verticalLayout.addWidget(self.graph_controls)
        self.save_data_to = QtWidgets.QLabel(self.controls_tab)
        self.save_data_to.setObjectName("save_data_to")
        self.verticalLayout.addWidget(self.save_data_to)
        self.save = QtWidgets.QPushButton(self.controls_tab)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)
        """attach save_file_dialog() function to button"""
        self.save.clicked.connect(self.save_file_dialog)

        self.controls_settings_tab.addTab(self.controls_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.settings_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settings_description = QtWidgets.QLabel(self.settings_tab)
        self.settings_description.setObjectName("settings_description")
        self.verticalLayout_3.addWidget(self.settings_description)
        self.choose_date = QtWidgets.QLabel(self.settings_tab)
        self.choose_date.setObjectName("choose_date")
        self.verticalLayout_3.addWidget(self.choose_date)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.settings_tab)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout_3.addWidget(self.dateTimeEdit)

        # auto set date and time
        # every time tab is switched, update the time?
        self.update_datetime()

        self.choose_duration = QtWidgets.QLabel(self.settings_tab)
        self.choose_duration.setObjectName("choose_duration")
        self.verticalLayout_3.addWidget(self.choose_duration)
        self.comboBox = QtWidgets.QComboBox(self.settings_tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.note = QtWidgets.QLabel(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.note.sizePolicy().hasHeightForWidth())
        self.note.setSizePolicy(sizePolicy)
        self.note.setScaledContents(False)
        self.note.setWordWrap(True)
        self.note.setObjectName("note")
        self.verticalLayout_3.addWidget(self.note)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.controls_settings_tab.addTab(self.settings_tab, "")
        self.controls_settings.addWidget(self.controls_settings_tab)
        self.gridLayout.addLayout(self.controls_settings, 0, 4, 1, 1)
        self.graph_window = QtWidgets.QVBoxLayout()
        self.graph_window.setContentsMargins(-1, -1, -1, 0)
        self.graph_window.setObjectName("graph_window")
        """matplotlib injection"""
        # replace previous self.canvas with FigureCanvasQTAgg
        # replace previous self.toolbar with NavigationToolbar2QT
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas)

        #self.toolbar = QtWidgets.QDial(self.centralwidget)
        self.toolbar.setObjectName("toolbar")
        self.graph_window.addWidget(self.toolbar)
        #self.canvas = QtWidgets.QGraphicsView(self.centralwidget)
        
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 3, 5, 6], '-')
        self.canvas.draw()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.graph_window.addWidget(self.canvas)
        self.gridLayout.addLayout(self.graph_window, 0, 0, 1, 4)
        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.controls_settings_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.controls_settings_tab, self.run_pause)
        MainWindow.setTabOrder(self.run_pause, self.reset_stop)
        MainWindow.setTabOrder(self.reset_stop, self.pressure_checkbox)
        MainWindow.setTabOrder(self.pressure_checkbox,
                               self.temperature_checkbox)
        MainWindow.setTabOrder(self.temperature_checkbox, self.legend_checkbox)
        MainWindow.setTabOrder(self.legend_checkbox, self.dateTimeEdit)
        MainWindow.setTabOrder(self.dateTimeEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.canvas)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "PVSL Temperature and Pressure"))
        self.graph_and_system.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:14pt;\">Graph and system controls</span></p></body></html>"
            ))
        self.pv_test_controls.setTitle(
            _translate("MainWindow", "PV Test Controls"))
        self.run_pause.setText(_translate("MainWindow", "Run"))
        self.reset_stop.setText(_translate("MainWindow", "Reset"))
        self.time_remaining.setText(_translate("MainWindow", "Remaining:"))
        self.graph_controls.setTitle(_translate("MainWindow",
                                                "Graph Controls"))
        self.pressure_checkbox.setText(_translate("MainWindow", "Pressure"))
        self.temperature_checkbox.setText(
            _translate("MainWindow", "Temperature"))
        self.legend_checkbox.setText(_translate("MainWindow", "Legend"))
        self.save_data_to.setText(
            _translate("MainWindow", "Save data to file:"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.controls_settings_tab.setTabText(
            self.controls_settings_tab.indexOf(self.controls_tab),
            _translate("MainWindow", "Controls"))
        self.settings_description.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:14pt;\">App settings</span></p></body></html>"
            ))
        self.choose_date.setText(
            _translate("MainWindow", "Choose date and time:"))
        self.choose_duration.setText(
            _translate("MainWindow", "Choose duration:"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10min"))
        self.comboBox.setItemText(2, _translate("MainWindow", "20min"))
        self.comboBox.setItemText(3, _translate("MainWindow", "30min"))
        self.comboBox.setItemText(4, _translate("MainWindow", "45min"))
        self.comboBox.setItemText(5, _translate("MainWindow", "1hr"))
        self.comboBox.setItemText(6, _translate("MainWindow", "2hr"))
        self.comboBox.setItemText(7, _translate("MainWindow", "4hr"))
        self.comboBox.setItemText(8, _translate("MainWindow", "10hr"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Custom..."))
        self.note.setText(
            _translate(
                "MainWindow",
                "Note: unspecified duration will run until manually stopped "))
        self.controls_settings_tab.setTabText(
            self.controls_settings_tab.indexOf(self.settings_tab),
            _translate("MainWindow", "Settings"))
            
    def save_file_dialog(self):
        """
        Saves the test results to a file specified by filepath
        """
        # open file dialog
        current_QDate = QtCore.QDate.currentDate()
        print(current_QDate.day())
        name_type = "PV_{}_{}_{}".format(current_QDate.month(), current_QDate.day(), current_QDate.year())
        fname, ftype = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "Save File", name_type, "CSV Files(*.csv);;Text Files(*.txt);;All Files (*)")
        
        if fname:
            fname = str(fname)
            ftype = str(ftype)[-5:-1]
            name_type = fname + ftype
            with open(name_type, 'w') as f:
                f.write(name_type)
                f.close()

    def update_datetime(self):
        """
        Updates the app datetime to match internal Raspberry Pi datetime.
        """
        # QDate has some useful methods, same vernacular as QTime
        current_QDate = QtCore.QDate.currentDate()
        current_QTime = QtCore.QTime.currentTime()
        self.dateTimeEdit.setDate(current_QDate)
        self.dateTimeEdit.setTime(current_QTime)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
