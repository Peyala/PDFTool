# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/frames/count.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultCount(object):
    def setupUi(self, resultCount):
        resultCount.setObjectName("resultCount")
        resultCount.resize(245, 221)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(resultCount.sizePolicy().hasHeightForWidth())
        resultCount.setSizePolicy(sizePolicy)
        resultCount.setMinimumSize(QtCore.QSize(245, 221))
        resultCount.setMaximumSize(QtCore.QSize(245, 221))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/frames\\../img/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resultCount.setWindowIcon(icon)
        self.pagesLabel = QtWidgets.QLabel(resultCount)
        self.pagesLabel.setGeometry(QtCore.QRect(32, 128, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pagesLabel.sizePolicy().hasHeightForWidth())
        self.pagesLabel.setSizePolicy(sizePolicy)
        self.pagesLabel.setMinimumSize(QtCore.QSize(75, 23))
        self.pagesLabel.setMaximumSize(QtCore.QSize(75, 23))
        self.pagesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pagesLabel.setObjectName("pagesLabel")
        self.charTextBrowser = QtWidgets.QTextBrowser(resultCount)
        self.charTextBrowser.setGeometry(QtCore.QRect(130, 29, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charTextBrowser.sizePolicy().hasHeightForWidth())
        self.charTextBrowser.setSizePolicy(sizePolicy)
        self.charTextBrowser.setMinimumSize(QtCore.QSize(81, 23))
        self.charTextBrowser.setMaximumSize(QtCore.QSize(81, 23))
        self.charTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.charTextBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.charTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.charTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.charTextBrowser.setObjectName("charTextBrowser")
        self.charLabel = QtWidgets.QLabel(resultCount)
        self.charLabel.setGeometry(QtCore.QRect(32, 29, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.charLabel.sizePolicy().hasHeightForWidth())
        self.charLabel.setSizePolicy(sizePolicy)
        self.charLabel.setMinimumSize(QtCore.QSize(75, 23))
        self.charLabel.setMaximumSize(QtCore.QSize(75, 23))
        self.charLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.charLabel.setObjectName("charLabel")
        self.pagesTextBrowser = QtWidgets.QTextBrowser(resultCount)
        self.pagesTextBrowser.setGeometry(QtCore.QRect(130, 128, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pagesTextBrowser.sizePolicy().hasHeightForWidth())
        self.pagesTextBrowser.setSizePolicy(sizePolicy)
        self.pagesTextBrowser.setMinimumSize(QtCore.QSize(81, 23))
        self.pagesTextBrowser.setMaximumSize(QtCore.QSize(81, 23))
        self.pagesTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pagesTextBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pagesTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pagesTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pagesTextBrowser.setObjectName("pagesTextBrowser")
        self.wordsLabel = QtWidgets.QLabel(resultCount)
        self.wordsLabel.setGeometry(QtCore.QRect(32, 62, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordsLabel.sizePolicy().hasHeightForWidth())
        self.wordsLabel.setSizePolicy(sizePolicy)
        self.wordsLabel.setMinimumSize(QtCore.QSize(75, 23))
        self.wordsLabel.setMaximumSize(QtCore.QSize(75, 23))
        self.wordsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wordsLabel.setObjectName("wordsLabel")
        self.wordsTextBrowser = QtWidgets.QTextBrowser(resultCount)
        self.wordsTextBrowser.setGeometry(QtCore.QRect(130, 62, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordsTextBrowser.sizePolicy().hasHeightForWidth())
        self.wordsTextBrowser.setSizePolicy(sizePolicy)
        self.wordsTextBrowser.setMinimumSize(QtCore.QSize(81, 23))
        self.wordsTextBrowser.setMaximumSize(QtCore.QSize(81, 23))
        self.wordsTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.wordsTextBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wordsTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wordsTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wordsTextBrowser.setObjectName("wordsTextBrowser")
        self.linesLabel = QtWidgets.QLabel(resultCount)
        self.linesLabel.setGeometry(QtCore.QRect(32, 95, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linesLabel.sizePolicy().hasHeightForWidth())
        self.linesLabel.setSizePolicy(sizePolicy)
        self.linesLabel.setMinimumSize(QtCore.QSize(75, 23))
        self.linesLabel.setMaximumSize(QtCore.QSize(75, 23))
        self.linesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.linesLabel.setObjectName("linesLabel")
        self.linesTextBrowser = QtWidgets.QTextBrowser(resultCount)
        self.linesTextBrowser.setGeometry(QtCore.QRect(130, 95, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linesTextBrowser.sizePolicy().hasHeightForWidth())
        self.linesTextBrowser.setSizePolicy(sizePolicy)
        self.linesTextBrowser.setMinimumSize(QtCore.QSize(81, 23))
        self.linesTextBrowser.setMaximumSize(QtCore.QSize(81, 23))
        self.linesTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.linesTextBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.linesTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.linesTextBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.linesTextBrowser.setObjectName("linesTextBrowser")
        self.pushButton = QtWidgets.QPushButton(resultCount)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(81, 23))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(resultCount)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 170, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(81, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(81, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(resultCount)
        QtCore.QMetaObject.connectSlotsByName(resultCount)

    def retranslateUi(self, resultCount):
        _translate = QtCore.QCoreApplication.translate
        resultCount.setWindowTitle(_translate("resultCount", "Count results"))
        self.pagesLabel.setText(_translate("resultCount", "Pages"))
        self.charTextBrowser.setHtml(_translate("resultCount", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.charLabel.setText(_translate("resultCount", "Characters"))
        self.pagesTextBrowser.setHtml(_translate("resultCount", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.wordsLabel.setText(_translate("resultCount", "Words"))
        self.wordsTextBrowser.setHtml(_translate("resultCount", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.linesLabel.setText(_translate("resultCount", "Lines"))
        self.linesTextBrowser.setHtml(_translate("resultCount", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("resultCount", "Export"))
        self.pushButton_2.setText(_translate("resultCount", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultCount = QtWidgets.QDialog()
    ui = Ui_resultCount()
    ui.setupUi(resultCount)
    resultCount.show()
    sys.exit(app.exec_())
