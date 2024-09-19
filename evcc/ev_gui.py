"""
.. module:: evse_gui
   :platform: Unix
   :synopsis: A module that implements the client's side GUI.

.. Copyright 2022 EDF 

.. moduleauthor:: Oscar RODRIGUEZ INFANTE, Tony ZHOU, Trang PHAM, Efflam OLLIVIER 

.. License:: This source code is licensed under the MIT License.


"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from shared.gui import GUI
from shared.utils import rational_to_float
from shared.custom_canvas import CustomCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from evcc.ev_dummy_controller import EVDummyController 
from shared.threading import Worker
from evcc.start_ev import start_ev
import time


class EVMainWindow(GUI):
    def __init__(self):
        self.controller = EVDummyController()
        self.controller.data_model.attach(self)
        self.controller.state_machine.attach(self)
        self.has_started_ev = False

    def setup_ui(self, main_window):
        main_window.setObjectName("EVMainWindow")
        main_window.resize(1000, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMaximumSize(QtCore.QSize(1000, 750))
        main_window.setBaseSize(QtCore.QSize(1000, 750))
        font = QtGui.QFont()
        font.setPointSize(15)
        main_window.setFont(font)
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 601))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.setup_tab = QtWidgets.QWidget()
        self.setup_tab.setObjectName("setup_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.setup_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.departure_time = QtWidgets.QDoubleSpinBox(self.setup_tab)
        self.departure_time.setValue(24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.departure_time.sizePolicy().hasHeightForWidth())
        self.departure_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.departure_time.setFont(font)
        self.departure_time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.departure_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.departure_time.setPrefix("")
        self.departure_time.setDecimals(1)
        self.departure_time.setMaximum(1000.0)
        self.departure_time.setSingleStep(0.5)
        self.departure_time.setObjectName("departure_time")
        self.verticalLayout_4.addWidget(self.departure_time)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.target_soc = QtWidgets.QDoubleSpinBox(self.setup_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.target_soc.setFont(font)
        self.target_soc.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.target_soc.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.target_soc.setPrefix("")
        self.target_soc.setDecimals(0)
        self.target_soc.setMaximum(100)
        self.target_soc.setSingleStep(1)
        self.target_soc.setValue(80)
        self.target_soc.setObjectName("target_soc")
        self.verticalLayout_4.addWidget(self.target_soc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.set_button = QtWidgets.QPushButton(self.setup_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_button.setFont(font)
        self.set_button.setObjectName("set_button")
        self.verticalLayout_4.addWidget(self.set_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.line = QtWidgets.QFrame(self.setup_tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem6)
        self.start_button = QtWidgets.QPushButton(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_button.setFont(font)
        self.start_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_button.setObjectName("start_button")
        self.verticalLayout_6.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.setup_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stop_button.setFont(font)
        self.stop_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.stop_button.setAutoDefault(False)
        self.stop_button.setDefault(False)
        self.stop_button.setFlat(False)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setEnabled(False)
        self.verticalLayout_6.addWidget(self.stop_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.setup_tab, "")
        self.infos_tab = QtWidgets.QWidget()
        self.infos_tab.setObjectName("infos_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.infos_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.infos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem8)
        self.soc = QtWidgets.QProgressBar(self.infos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soc.sizePolicy().hasHeightForWidth())
        self.soc.setSizePolicy(sizePolicy)
        self.soc.setProperty("value", 0)
        self.soc.setAlignment(QtCore.Qt.AlignCenter)
        self.soc.setOrientation(QtCore.Qt.Horizontal)
        self.soc.setObjectName("soc")
        self.verticalLayout_3.addWidget(self.soc)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.infos_tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.target_soc_2 = QtWidgets.QLabel(self.infos_tab)
        self.target_soc_2.setFrameShape(QtWidgets.QFrame.Box)
        self.target_soc_2.setScaledContents(True)
        self.target_soc_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.target_soc_2.setObjectName("target_soc_2")
        self.horizontalLayout_6.addWidget(self.target_soc_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.infos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.provided_energy = QtWidgets.QLabel(self.infos_tab)
        self.provided_energy.setFrameShape(QtWidgets.QFrame.Box)
        self.provided_energy.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.provided_energy.setObjectName("provided_energy")
        self.horizontalLayout_2.addWidget(self.provided_energy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.infos_tab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.consumed_energy = QtWidgets.QLabel(self.infos_tab)
        self.consumed_energy.setFrameShape(QtWidgets.QFrame.Box)
        self.consumed_energy.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.consumed_energy.setObjectName("consumed_energy")
        self.horizontalLayout_4.addWidget(self.consumed_energy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.infos_tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.total_energy = QtWidgets.QLabel(self.infos_tab)
        self.total_energy.setFrameShape(QtWidgets.QFrame.Box)
        self.total_energy.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.total_energy.setObjectName("total_energy")
        self.horizontalLayout_5.addWidget(self.total_energy)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem17)
        self.line_3 = QtWidgets.QFrame(self.infos_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_9.addWidget(self.line_3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem18)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_20 = QtWidgets.QLabel(self.infos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem19)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.infos_tab)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.physical_state = QtWidgets.QLabel(self.infos_tab)
        self.physical_state.setFrameShape(QtWidgets.QFrame.Box)
        self.physical_state.setScaledContents(True)
        self.physical_state.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.physical_state.setObjectName("physical_state")
        self.horizontalLayout_7.addWidget(self.physical_state)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 1, 2, 1)
        self.line_2 = QtWidgets.QFrame(self.infos_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 3, 2, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QtWidgets.QLabel(self.infos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.cb1 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_boxes = []
        self.cb1.setFont(font)
        self.cb1.setObjectName("SupportedAppProtocol")
        self.verticalLayout.addWidget(self.cb1)
        self.check_boxes.append(self.cb1)
        self.cb2 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb2.setFont(font)
        self.cb2.setObjectName("SessionSetup")
        self.verticalLayout.addWidget(self.cb2)
        self.check_boxes.append(self.cb2)
        self.cb3 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb3.setFont(font)
        self.cb3.setObjectName("AuthorizationSetup")
        self.verticalLayout.addWidget(self.cb3)
        self.check_boxes.append(self.cb3)
        self.cb4 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb4.setFont(font)
        self.cb4.setObjectName("Authorization")
        self.verticalLayout.addWidget(self.cb4)
        self.check_boxes.append(self.cb4)
        self.cb5 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb5.setFont(font)
        self.cb5.setObjectName("ServiceDiscovery")
        self.check_boxes.append(self.cb5)
        self.verticalLayout.addWidget(self.cb5)
        self.cb6 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb6.setFont(font)
        self.cb6.setObjectName("ServiceDetail")
        self.verticalLayout.addWidget(self.cb6)
        self.check_boxes.append(self.cb6)
        self.cb7 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb7.setFont(font)
        self.cb7.setObjectName("ServiceSelection")
        self.verticalLayout.addWidget(self.cb7)
        self.check_boxes.append(self.cb7)
        self.cb8 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb8.setFont(font)
        self.cb8.setObjectName("DcChargeParameterDiscovery")
        self.verticalLayout.addWidget(self.cb8)
        self.check_boxes.append(self.cb8)
        self.cb9 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb9.setFont(font)
        self.cb9.setObjectName("ScheduleExchange")
        self.verticalLayout.addWidget(self.cb9)
        self.check_boxes.append(self.cb9)
        self.cb10 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb10.setFont(font)
        self.cb10.setObjectName("DcCableCheck")
        self.verticalLayout.addWidget(self.cb10)
        self.check_boxes.append(self.cb10)
        self.cb13 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb13.setFont(font)
        self.cb13.setObjectName("DcPreCharge")
        self.verticalLayout.addWidget(self.cb13)
        self.check_boxes.append(self.cb13)
        self.cb12 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb12.setFont(font)
        self.cb12.setObjectName("PowerDelivery")
        self.verticalLayout.addWidget(self.cb12)
        self.check_boxes.append(self.cb12)
        self.cb15 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb15.setFont(font)
        self.cb15.setObjectName("DcChargeLoop")
        self.verticalLayout.addWidget(self.cb15)
        self.check_boxes.append(self.cb15)
        self.cb14 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb14.setFont(font)
        self.cb14.setObjectName("DcWeldingDetection")
        self.verticalLayout.addWidget(self.cb14)
        self.check_boxes.append(self.cb14)
        self.cb11 = QtWidgets.QCheckBox(self.infos_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb11.setFont(font)
        self.cb11.setObjectName("SessionStop")
        self.verticalLayout.addWidget(self.cb11)
        self.check_boxes.append(self.cb11)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 5, 2, 1)
        spacerItem21 = QtWidgets.QSpacerItem(117, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem22, 1, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 1, 4, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(117, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem24, 1, 6, 1, 1)
        self.tabWidget.addTab(self.infos_tab, "")
        self.display_tab = QtWidgets.QWidget()
        self.display_tab.setObjectName("display_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.display_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem25, 0, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem26, 0, 2, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        power_limit = rational_to_float(self.controller.data_model.get_max_charge_parameters()[0])
        limits = (power_limit, -power_limit)
        battery = rational_to_float(self.controller.data_model.battery_capacity)
        self.graphics = CustomCanvas(
            self.controller.data_model.power_evolution, self.controller.data_model.energy_evolution, limits, battery)
        self.graphics.setObjectName("graphics")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics.sizePolicy().hasHeightForWidth())
        self.graphics.setSizePolicy(sizePolicy)
        self.verticalLayout_8.addWidget(self.graphics)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem27, 0, 4, 1, 1)
        self.tabWidget.addTab(self.display_tab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.departure_time_cd = QtWidgets.QLCDNumber(self.centralwidget)
        self.departure_time_cd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.departure_time_cd.setDigitCount(6)
        self.departure_time_cd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.departure_time_cd.setObjectName("departure_time_cd")
        self.horizontalLayout_9.addWidget(self.departure_time_cd)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem28)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.current_soc = QtWidgets.QLabel(self.centralwidget)
        self.current_soc.setFrameShape(QtWidgets.QFrame.Box)
        self.current_soc.setObjectName("current_soc")
        self.horizontalLayout_9.addWidget(self.current_soc)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.soc_timer = QtCore.QTimer()
        self.soc_timer.setInterval(1000)
        self.soc_timer.timeout.connect(self.update_soc)
        self.soc_timer.start()

        self.connect_signals()
        main_window.setCentralWidget(self.centralwidget)
        self.retranslate_ui(main_window)

        main_window.showMaximized()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("EVMainWindow", "EVMainWindow"))
        self.label_13.setText(_translate("EVMainWindow", "EV Mobility Needs"))
        self.label.setText(_translate("EVMainWindow", "Departure time:"))
        self.departure_time.setSuffix(_translate("EVMainWindow", " hours"))
        self.label_2.setText(_translate("EVMainWindow", "Target SoC:"))
        self.target_soc.setSuffix(_translate("EVMainWindow", " %"))
        self.set_button.setText(_translate("EVMainWindow", "Set"))
        self.label_14.setText(_translate("EVMainWindow", "Charging session"))
        self.start_button.setText(_translate("EVMainWindow", "Start"))
        self.stop_button.setText(_translate("EVMainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setup_tab), _translate("EVMainWindow", "Setup"))
        self.label_15.setText(_translate("EVMainWindow", "State of Charge"))
        self.label_6.setText(_translate("EVMainWindow", "Target SoC:"))
        self.target_soc_2.setText(_translate("EVMainWindow", "Not defined"))
        self.label_4.setText(_translate("EVMainWindow", "Energy provided by EV:"))
        self.provided_energy.setText(_translate("EVMainWindow", "Not defined"))
        self.label_8.setText(_translate("EVMainWindow", "Energy consumed by EV:"))
        self.consumed_energy.setText(_translate("EVMainWindow", "Not defined"))
        self.label_9.setText(_translate("EVMainWindow", "Total energy:"))
        self.total_energy.setText(_translate("EVMainWindow", "Not defined"))
        self.label_20.setText(_translate("EVMainWindow", "61851"))
        self.label_19.setText(_translate("EVMainWindow", "Current state:"))
        self.physical_state.setText(_translate("EVMainWindow", "Not defined"))
        self.label_17.setText(_translate("EVMainWindow", "15118 states"))
        self.cb1.setText(_translate("EVMainWindow", "SupportedAppProtocol"))
        self.cb2.setText(_translate("EVMainWindow", "SessionSetup"))
        self.cb3.setText(_translate("EVMainWindow", "AuthorizationSetup"))
        self.cb4.setText(_translate("EVMainWindow", "Authorization"))
        self.cb5.setText(_translate("EVMainWindow", "ServiceDiscovery"))
        self.cb6.setText(_translate("EVMainWindow", "ServiceDetail"))
        self.cb7.setText(_translate("EVMainWindow", "ServiceSelection"))
        self.cb8.setText(_translate("EVMainWindow", "DcChargeParameterDiscovery"))
        self.cb9.setText(_translate("EVMainWindow", "ScheduleExchange"))
        self.cb10.setText(_translate("EVMainWindow", "DcCableCheck"))
        self.cb13.setText(_translate("EVMainWindow", "DcPreCharge"))
        self.cb12.setText(_translate("EVMainWindow", "PowerDelivery"))
        self.cb15.setText(_translate("EVMainWindow", "DcChargeLoop"))
        self.cb14.setText(_translate("EVMainWindow", "DcWeldingDetection"))
        self.cb11.setText(_translate("EVMainWindow", "SessionStop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infos_tab), _translate("EVMainWindow", "Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.display_tab),
                                  _translate("EVMainWindow", "Charge Power"))
        self.label_12.setText(_translate("EVMainWindow", "Departure time:"))
        self.label_21.setText(_translate("EVMainWindow", "Current SoC:"))
        self.current_soc.setText(_translate("EVMainWindow", "Not defined"))

    def update(self, subject):
        if subject.notification_type == "61851":
            self.physical_state.setText(self.controller.state_machine.state)
        elif subject.notification_type == "15118":
            v2g_state = self.controller.data_model.state
            self.check_state_box(v2g_state)
        elif subject.notification_type == "ev_settings":
            self.graphics.evsemaximum_charge_power[-1] = rational_to_float(
                self.controller.data_model.evsemaximum_charge_power)
            self.graphics.evsemaximum_discharge_power[-1] = - rational_to_float(
                self.controller.data_model.evsemaximum_discharge_power)
            self.graphics.evmaximum_charge_power[-1] = rational_to_float(
                self.controller.data_model.evmaximum_charge_power)
            self.graphics.evmaximum_discharge_power[-1] = - rational_to_float(
                self.controller.data_model.evmaximum_discharge_power)
            self.graphics.maximum_battery_capacity[-1] = rational_to_float(
                self.controller.data_model.battery_capacity)
        elif subject.notification_type == "timer":
            self.update_timer()
        elif subject.notification_type == "target_soc":
            self.target_soc_2.setText(str(self.controller.data_model.target_soc)+"%")

    def check_state_box(self, state):
        state = state[:-3]
        checkbox = self.infos_tab.findChild(QtWidgets.QCheckBox, state)
        if not checkbox.isChecked():
            checkbox.setChecked(True)

    def startup_ev(self):
        if not self.has_started_ev:
            time.sleep(3)
            self.run_ev()
            self.has_started_ev = True
        else:
            pass

    def connect_signals(self):
        self.set_button.clicked.connect(self.set_ev_settings)
        self.start_button.clicked.connect(self.startup_ev)
        self.stop_button.clicked.connect(self.stop_ev)

    def set_ev_settings(self):
        self.controller.data_model.target_soc = int(self.target_soc.value())
        self.target_soc_2.setText(str(int(self.target_soc.value())) + "%")
        self.controller.data_model.departure_time = int(self.departure_time.value() * 3600)
        self.update_timer()

    def update_timer(self):
        self.departure_time_cd.display(self.controller.data_model.departure_time)

    def update_soc(self) -> None:
        """Updates the present soc.

        :return:
        """
        self.physical_state.setText(self.controller.state_machine.state)
        present_soc = self.controller.data_model.present_soc
        if isinstance(present_soc, int):
            self.soc.setProperty("value", present_soc)
            self.current_soc.setText(str(present_soc) + "%")
        self.provided_energy.setText(str(self.controller.data_model.provided_energy) + "Wh")
        self.consumed_energy.setText(str(self.controller.data_model.consumed_energy) + "Wh")
        self.total_energy.setText(str(self.controller.data_model.total_energy) + "Wh")

    def stop_ev(self) -> None:
        """Stops the EV.

        :return:
        """
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
        self.controller.stop()
        self.start_button.clicked.connect(self.reset_check_boxes)


    def reset_check_boxes(self) -> None:
        """Resets state checkboxes.

        :return:
        """
        for checkbox in self.check_boxes:
            if checkbox.isChecked():
                checkbox.setChecked(False)

    def run_ev(self) -> None:
        """Runs charging session from EV side.

        :return:
        """
        self.tabWidget.setCurrentIndex(1)
        # Step 2: Create a QThread object
        self.thread = QtCore.QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.controller, start_ev)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.thread.finished.connect(
            lambda: self.stop_button.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: print("Hello I'm finished")
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = EVMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
