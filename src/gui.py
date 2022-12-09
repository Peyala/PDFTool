# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/frames/anotherGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import tree as tree

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 343)
        MainWindow.setMinimumSize(QtCore.QSize(321, 343))
        MainWindow.setMaximumSize(QtCore.QSize(321, 343))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/frames\\../img/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.operationsTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.operationsTabWidget.setEnabled(True)
        self.operationsTabWidget.setGeometry(QtCore.QRect(20, 170, 281, 121))
        self.operationsTabWidget.setObjectName("operationsTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.countButton = QtWidgets.QPushButton(self.tab)
        self.countButton.setEnabled(True)
        self.countButton.setGeometry(QtCore.QRect(95, 60, 80, 23))
        self.countButton.setDefault(False)
        self.countButton.setFlat(False)
        self.countButton.setObjectName("countButton")
        self.charsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.charsCheckBox.setGeometry(QtCore.QRect(15, 22, 76, 17))
        self.charsCheckBox.setObjectName("charsCheckBox")
        self.linesCheckBox = QtWidgets.QCheckBox(self.tab)
        self.linesCheckBox.setGeometry(QtCore.QRect(158, 22, 47, 17))
        self.linesCheckBox.setObjectName("linesCheckBox")
        self.wordsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.wordsCheckBox.setGeometry(QtCore.QRect(98, 22, 54, 17))
        self.wordsCheckBox.setObjectName("wordsCheckBox")
        self.pagesCheckBox = QtWidgets.QCheckBox(self.tab)
        self.pagesCheckBox.setGeometry(QtCore.QRect(210, 22, 52, 17))
        self.pagesCheckBox.setObjectName("pagesCheckBox")
        self.operationsTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(50, 20, 170, 22))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pagesRemLabel = QtWidgets.QLabel(self.layoutWidget_5)
        self.pagesRemLabel.setObjectName("pagesRemLabel")
        self.horizontalLayout_7.addWidget(self.pagesRemLabel)
        self.remLineEdit = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.remLineEdit.setText("")
        self.remLineEdit.setObjectName("remLineEdit")
        self.horizontalLayout_7.addWidget(self.remLineEdit)
        self.removeButton = QtWidgets.QPushButton(self.tab_2)
        self.removeButton.setGeometry(QtCore.QRect(95, 60, 80, 23))
        self.removeButton.setObjectName("removeButton")
        self.operationsTabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.extractButton = QtWidgets.QPushButton(self.tab_6)
        self.extractButton.setGeometry(QtCore.QRect(95, 60, 80, 23))
        self.extractButton.setObjectName("extractButton")
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab_6)
        self.layoutWidget_6.setGeometry(QtCore.QRect(50, 20, 170, 22))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pagesExtrLabel = QtWidgets.QLabel(self.layoutWidget_6)
        self.pagesExtrLabel.setObjectName("pagesExtrLabel")
        self.horizontalLayout_11.addWidget(self.pagesExtrLabel)
        self.extrLineEdit = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.extrLineEdit.setText("")
        self.extrLineEdit.setObjectName("extrLineEdit")
        self.horizontalLayout_11.addWidget(self.extrLineEdit)
        self.operationsTabWidget.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.mergeButton = QtWidgets.QPushButton(self.tab_4)
        self.mergeButton.setGeometry(QtCore.QRect(95, 60, 80, 23))
        self.mergeButton.setObjectName("mergeButton")
        self.operationsTabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.splitButton = QtWidgets.QPushButton(self.tab_5)
        self.splitButton.setGeometry(QtCore.QRect(95, 60, 80, 23))
        self.splitButton.setObjectName("splitButton")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 20, 138, 24))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.intervalSplitLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.intervalSplitLabel.setObjectName("intervalSplitLabel")
        self.horizontalLayout_8.addWidget(self.intervalSplitLabel)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.bottomSplitSpinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.bottomSplitSpinBox.setObjectName("bottomSplitSpinBox")
        self.horizontalLayout_9.addWidget(self.bottomSplitSpinBox)
        self.separatorSplitLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.separatorSplitLabel.setObjectName("separatorSplitLabel")
        self.horizontalLayout_9.addWidget(self.separatorSplitLabel)
        self.topSplitSpinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.topSplitSpinBox.setObjectName("topSplitSpinBox")
        self.horizontalLayout_9.addWidget(self.topSplitSpinBox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.operationsTabWidget.addTab(self.tab_5, "")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(220, 110, 81, 23))
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(130, 110, 81, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 145, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pdfTreeWidget = tree.TreeWidget(self.centralwidget)
        self.pdfTreeWidget.setGeometry(QtCore.QRect(20, 10, 281, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfTreeWidget.sizePolicy().hasHeightForWidth())
        self.pdfTreeWidget.setSizePolicy(sizePolicy)
        self.pdfTreeWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pdfTreeWidget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pdfTreeWidget.setAcceptDrops(True)
        self.pdfTreeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pdfTreeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.pdfTreeWidget.setAutoScroll(False)
        self.pdfTreeWidget.setDragEnabled(False)
        self.pdfTreeWidget.setDragDropOverwriteMode(False)
        self.pdfTreeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.pdfTreeWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.pdfTreeWidget.setAlternatingRowColors(True)
        self.pdfTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pdfTreeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.pdfTreeWidget.setUniformRowHeights(False)
        self.pdfTreeWidget.setItemsExpandable(False)
        self.pdfTreeWidget.setAnimated(False)
        self.pdfTreeWidget.setWordWrap(False)
        self.pdfTreeWidget.setObjectName("pdfTreeWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 321, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.newAction = QtWidgets.QAction(MainWindow)
        self.newAction.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.newAction.setObjectName("newAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.actionAbout_PDFTool = QtWidgets.QAction(MainWindow)
        self.actionAbout_PDFTool.setObjectName("actionAbout_PDFTool")
        self.actionSee_help = QtWidgets.QAction(MainWindow)
        self.actionSee_help.setObjectName("actionSee_help")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionSelect_all = QtWidgets.QAction(MainWindow)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.menuFile.addAction(self.newAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exitAction)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuHelp.addAction(self.actionSee_help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_PDFTool)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.operationsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDFTool"))
        self.countButton.setText(_translate("MainWindow", "Count"))
        self.charsCheckBox.setText(_translate("MainWindow", "Characters"))
        self.linesCheckBox.setText(_translate("MainWindow", "Lines"))
        self.wordsCheckBox.setText(_translate("MainWindow", "Words"))
        self.pagesCheckBox.setText(_translate("MainWindow", "Pages"))
        self.operationsTabWidget.setTabText(self.operationsTabWidget.indexOf(self.tab), _translate("MainWindow", "Count"))
        self.pagesRemLabel.setText(_translate("MainWindow", "Pages"))
        self.remLineEdit.setPlaceholderText(_translate("MainWindow", " 1-5,7,9-11,15"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.operationsTabWidget.setTabText(self.operationsTabWidget.indexOf(self.tab_2), _translate("MainWindow", "Remove"))
        self.extractButton.setText(_translate("MainWindow", "Extract"))
        self.pagesExtrLabel.setText(_translate("MainWindow", "Pages"))
        self.extrLineEdit.setPlaceholderText(_translate("MainWindow", " 1-5,7,9-11,15"))
        self.operationsTabWidget.setTabText(self.operationsTabWidget.indexOf(self.tab_6), _translate("MainWindow", "Extract"))
        self.mergeButton.setText(_translate("MainWindow", "Merge"))
        self.operationsTabWidget.setTabText(self.operationsTabWidget.indexOf(self.tab_4), _translate("MainWindow", "Merge"))
        self.splitButton.setText(_translate("MainWindow", "Split"))
        self.intervalSplitLabel.setText(_translate("MainWindow", "Interval"))
        self.separatorSplitLabel.setText(_translate("MainWindow", "-"))
        self.operationsTabWidget.setTabText(self.operationsTabWidget.indexOf(self.tab_5), _translate("MainWindow", "Split"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.pdfTreeWidget.setSortingEnabled(False)
        self.pdfTreeWidget.headerItem().setText(0, _translate("MainWindow", "Order"))
        self.pdfTreeWidget.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.pdfTreeWidget.headerItem().setText(2, _translate("MainWindow", "Selected"))
        __sortingEnabled = self.pdfTreeWidget.isSortingEnabled()
        self.pdfTreeWidget.setSortingEnabled(False)
        self.pdfTreeWidget.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.newAction.setText(_translate("MainWindow", "New"))
        self.newAction.setStatusTip(_translate("MainWindow", "Create a new blank workspace"))
        self.newAction.setWhatsThis(_translate("MainWindow", "Create a new blank workspace"))
        self.newAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.exitAction.setText(_translate("MainWindow", "Exit"))
        self.exitAction.setStatusTip(_translate("MainWindow", "Exit the application"))
        self.exitAction.setWhatsThis(_translate("MainWindow", "Exit the application"))
        self.actionAbout_PDFTool.setText(_translate("MainWindow", "About PDFTool"))
        self.actionSee_help.setText(_translate("MainWindow", "See the Help"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionSelect_all.setText(_translate("MainWindow", "Select all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
