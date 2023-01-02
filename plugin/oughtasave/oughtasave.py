 # By most_ghost
 # SPDX-License-Identifier: CC0-1.0
 
'''It's an autosave, except it actually saves automatically.

It is set up as a simple docker with minimal options, to keep it compact and out of the way.
'''
 
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QCheckBox, QSpinBox)
from krita import DockWidget
 
class AutosaveDocker(DockWidget):
    def __init__(self):
        super(AutosaveDocker, self).__init__()
        self.setWindowTitle(("Oughtasave"))

        self.func_initialize() # Pulls settings out of saving file, or initializes it if there are no settings yet

        self.autosave_button = QPushButton("Click to start Oughtasave.")
        self.autosave_button.setCheckable(True)            
        self.autosave_button.clicked.connect(self.toggle_on)

        self.settings_minutes = QSpinBox()
        self.settings_minutes.setValue(self.var_minutes)
        self.settings_minutes.setSuffix(" minutes")
        self.settings_minutes.setMinimum(1)
        self.settings_minutes.valueChanged.connect(self.set_minutes)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.func_autosave)
        self.timer.start(self.var_minutes * 1000 * 60) # 1000 milliseconds in a second, 60 seconds in a minute

        self.settings_check_increment = QCheckBox("Incremental Saves")
        self.settings_check_increment.stateChanged.connect(self.toggle_incremental)
        if self.var_increment == True:
            self.settings_check_increment.setChecked(True)
        self.var_increment = False

        self.settings_autostart = QCheckBox("Autostart")
        self.settings_autostart.stateChanged.connect(self.toggle_autostart)
        if self.var_autostart == True:
            self.settings_autostart.setChecked(True)

        self.settings_layout_left = QVBoxLayout()
        self.settings_layout_left.setAlignment(Qt.AlignTop)
        self.settings_layout_left.addWidget(self.settings_minutes)
        self.settings_layout_right = QVBoxLayout()
        self.settings_layout_right.setAlignment(Qt.AlignTop)
        self.settings_layout_right.addWidget(self.settings_autostart)
        self.settings_layout_right.addWidget(self.settings_check_increment)

        self.settings_widget_left = QWidget()
        self.settings_widget_left.setLayout(self.settings_layout_left)
        self.settings_widget_right = QWidget()
        self.settings_widget_right.setLayout(self.settings_layout_right)
        self.settings_combined = QHBoxLayout()
        self.settings_combined.addWidget(self.settings_widget_left)
        self.settings_combined.addWidget(self.settings_widget_right)

        self.settings_tab = QWidget()
        self.settings_tab.setLayout(self.settings_combined)

        tabWidget = QTabWidget()
        tabWidget.addTab(self.autosave_button, ("Toggle"))
        tabWidget.addTab(self.settings_tab, ("Settings"))

        main_layout = QVBoxLayout()
        main_layout.addWidget(tabWidget)
        
        main_docker_object = QWidget()
        main_docker_object.setLayout(main_layout)
        self.setWidget(main_docker_object)

        self.setMaximumHeight(125)

    def func_initialize(self):
        self.var_enabled = False
        self.var_increment = Krita.instance().readSetting('oughtasave','toggle_increment','')
        self.var_autostart = Krita.instance().readSetting('oughtasave','toggle_autostart','')
        self.var_minutes = Krita.instance().readSetting('oughtasave','num_minutes','')

        if self.var_increment == '' or self.var_increment == 'False': # Combining checks for compactness
            Krita.instance().writeSetting('oughtasave','toggle_increment','False')
            self.var_increment = False
        elif self.var_increment == 'True':
            self.var_increment = True

        if self.var_autostart == '' or self.var_autostart == 'False':
            Krita.instance().writeSetting('oughtasave','toggle_autostart','False')
            self.var_autostart = False
        elif self.var_autostart == 'True':
            self.var_autostart = True

        if self.var_minutes == '':
            Krita.instance().writeSetting('oughtasave','num_minutes','5')
            self.var_minutes = 5
        else:
            self.var_minutes = int(self.var_minutes)

    def toggle_autostart(self, s):
        if s == 2: # Checked
            Krita.instance().writeSetting('oughtasave','toggle_autostart','True')
        elif s == 0: # Unchecked
            Krita.instance().writeSetting('oughtasave','toggle_autostart','False')

    def toggle_on(self):
        self.state_check_auto = self.autosave_button.isChecked()
        if self.state_check_auto == True:
            self.autosave_button.setText("Oughtasave Enabled!")
            self.var_enabled = True
        elif self.state_check_auto == False:
            self.autosave_button.setText("Oughtasave Disabled.")
            self.var_enabled = False

    def toggle_incremental(self, s):
        if s == 2: # Checked
            self.var_increment = True
            Krita.instance().writeSetting('oughtasave','toggle_increment','True')
        elif s == 0: # Unchecked
            self.var_increment = False
            Krita.instance().writeSetting('oughtasave','toggle_increment','False')

    def set_minutes(self, i):
        Krita.instance().writeSetting('oughtasave','num_minutes',str(i))
        self.var_minutes = i
        self.timer.start(self.var_minutes * 1000 * 60)

    def func_autosave(self):
        if self.var_enabled:
            if self.var_increment == True:
                Krita.instance().action('save_incremental_backup').trigger()
            elif self.var_increment == False:
                Krita.instance().action('file_save').trigger()

    def canvasChanged(self, canvas):
        self.func_initialize()
        canvas_count = len(Krita.instance().documents()) # get the number of open documents
        if canvas_count > 0: # Don't autostart until krita has loaded at least 1 document
            if self.var_autostart == True:
                self.autosave_button.setChecked(True)
                self.toggle_on()