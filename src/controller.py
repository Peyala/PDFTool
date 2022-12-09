import pdfplumber as pdfpl
import pdf_manager as model
import gui as gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
import datetime as dt
import sys
import count_gui as count_gui
import tree as tree


# Operations 
def open_pdf(path: str):
    return model.open_pdf(path)

def close_pdf(pdf: pdfpl.PDF):
    return model.close_pdf(pdf)

def word_counter(pdf: pdfpl.PDF):
    return model.word_counter(pdf)

def char_counter(pdf: pdfpl.PDF):
    return model.char_counter(pdf)

def line_counter(pdf: pdfpl.PDF):
    return model.line_counter(pdf)

def page_counter(pdf: pdfpl.PDF):
    return model.page_counter(pdf)

def export_plain_txt(pdf: pdfpl.PDF):
    return model.export_plain_txt(pdf)

def merge_pdfs(pdfs: list, fileName: str):
    return model.merge_pdfs(pdfs, fileName)

def split_pdfs(pdfs: pdfpl.PDF, pages_range: list):
    return model.split_pdfs(pdfs,pages_range)

def remove_pages_pdf(pdf: pdfpl.PDF, i_pages: list):
    return model.remove_pages_pdf(pdf,i_pages)

def extract_pdfs(pdf: pdfpl.PDF, i_pages: list):
    return model.extract_pdfs(pdf,i_pages)

# Controllers
def enableButton(button: QtWidgets.QPushButton):
    button.setEnabled(True)

def disableButton(button: QtWidgets.QPushButton):
    button.setDisabled(True)

def addButtonHandler(ui: gui.Ui_MainWindow):
    pdf_paths = QFileDialog.getOpenFileNames(None,'Add your PDF files', './','PDF Files (*pdf)')[0]
    icon = QIcon('resources/img/pdf_icon')
    listWidget = ui.pdfTreeWidget
    _translate = QtCore.QCoreApplication.translate
    for pdf_path in pdf_paths:
        pdfItem = QtWidgets.QTreeWidgetItem(listWidget)
        pdfItem.setIcon(1, icon)
        pdfItem.setCheckState(2, QtCore.Qt.Unchecked)
        pdf = open_pdf(pdf_path)
        pdf_list.append(pdf)
        numberItems = len(pdf_list)
        pdfItem.setText(0, _translate("MainWindow", str(numberItems)))
        pdfItem.setText(1, _translate("MainWindow", pdf_path.split('/')[-1]))
    
def onItemClicked(it, col):
    if it.checkState(2) == 0:
        status = "Desactivado"
        if it in selectedItems:
            selectedItems.remove(it)
    else:
        status = "Activado"
        if it not in selectedItems:
            selectedItems.append(it)
    print(it.text(1), col, status)
    print(selectedItems)
    if len(selectedItems) == 0:
        disableButton(ui.deleteButton)
    else:
        enableButton(ui.deleteButton)
    
#before we had: for item in selectedItems: This is incorrect because we cant remove element while we are iterating. 
#Because there are elements that we couldn't reach. Instead, create a copy of the list in order to iterate on a copy
#So we can remove from selectedItems every item 
#See more: "https://stackoverflow.com/questions/6022764/python-removing-list-element-while-iterating-over-list"
def deleteButtonHandler():
    listWidget = ui.pdfTreeWidget
    root = listWidget.invisibleRootItem()
    for item in list(selectedItems):
        index = listWidget.indexOfTopLevelItem(item)
        print(index)
        close_pdf(pdf_list[index])
        del pdf_list[index]
        (item.parent() or root).removeChild(item)
        selectedItems.remove(item)
    disableButton(ui.deleteButton)
    reassignIds()

def deleteButtonVisibilityHandler(button: QtWidgets.QPushButton):
    if len(selectedItems) == 0:
        disableButton(button)
    else:
        enableButton(button)
        
def reassignIds():
    listWidget = ui.pdfTreeWidget
    i = 0
    while i < listWidget.topLevelItemCount():
        listWidget.topLevelItem(i).setText(0,str(i+1))
        i+=1

def countButtonHandler():
    text = ""
    listWidget = ui.pdfTreeWidget
    item = listWidget.selectedItems()[0]
    index = listWidget.row(item)
    pdf = pdf_list[index]
    if ui.charsCheckBox.isChecked():
        text = text + "Chars: " + str(char_counter(pdf)) + "\n"
    if ui.wordsCheckBox.isChecked():
        text = text + "Words: " + str(word_counter(pdf)) + "\n"
    if ui.linesCheckBox.isChecked():
        text = text + "Lines: " + str(line_counter(pdf)) + "\n"
    if ui.pagesCheckBox.isChecked():
        text = text + "Pages: " + str(page_counter(pdf)) + "\n"
    print(text)
    resultCount.show()

def mergeButtonHandler(widgetItems):
    elgible_pdfs = []
    listWidget = ui.pdfTreeWidget
    for item in widgetItems:
        i = listWidget.row(item) 
        elgible_pdfs.append(pdf_list[i])
    time = dt.date.today()
    file_name = QFileDialog.getSaveFileName(None,'Save merged PDF file', str(time) + '_merged.pdf','PDF Files (*pdf)')[0]
    if file_name.split('.')[-1] != 'pdf':
        file_name = file_name + '.pdf'
    merge_pdfs(elgible_pdfs,file_name)
    
def newActionHandler():
    #clear the pdf widget list
    ui.pdfTreeWidget.clear() 
    #close pdfs
    for pdf in pdf_list:
        close_pdf(pdf)
    #manage buttons
    disableButton(ui.deleteButton)
    #clear inputs
    ui.charsCheckBox.setChecked(False)
    ui.wordsCheckBox.setChecked(False)
    ui.linesCheckBox.setChecked(False)
    ui.pagesCheckBox.setChecked(False)
    
def initGuiElements():
    disableButton(ui.deleteButton)
    disableButton(ui.countButton)
    disableButton(ui.removeButton)
    disableButton(ui.extractButton)
    disableButton(ui.mergeButton)
    disableButton(ui.splitButton)
    ui.charsCheckBox.setChecked(False)
    ui.wordsCheckBox.setChecked(False)
    ui.linesCheckBox.setChecked(False)
    ui.pagesCheckBox.setChecked(False)
    ui.charsCheckBox.setEnabled(False)
    ui.wordsCheckBox.setEnabled(False)
    ui.linesCheckBox.setEnabled(False)
    ui.pagesCheckBox.setEnabled(False)
    ui.remLineEdit.setEnabled(False)
    ui.extrLineEdit.setEnabled(False)
    ui.bottomSplitSpinBox.setEnabled(False)
    ui.topSplitSpinBox.setEnabled(False)
    
def initGuiHandlers():
    ui.addButton.clicked.connect(lambda: addButtonHandler(ui))
    ui.deleteButton.clicked.connect(deleteButtonHandler)
    ui.countButton.clicked.connect(countButtonHandler)
    ui.mergeButton.clicked.connect(lambda: mergeButtonHandler(ui.pdfTreeWidget.selectedItems()))
    ui.newAction.triggered.connect(lambda: newActionHandler())
    
def initGui():
    global app, MainWindow, ui, resultCount, uiCount, pdf_list, selectedItems
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    resultCount = QtWidgets.QDialog()
    uiCount = count_gui.Ui_resultCount()
    uiCount.setupUi(resultCount)
    initGuiElements()
    initGuiHandlers()
    pdf_list = []
    ui.pdfTreeWidget.itemClicked.connect(onItemClicked)
    selectedItems = []
    # A incluir en gui pero como se sobreescribe lo dejo aqui por ahora
    ui.pdfTreeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    ui.pdfTreeWidget.header().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    ui.pdfTreeWidget.header().setFirstSectionMovable(True)
    ui.pdfTreeWidget.header().stretchLastSection()
    ui.pdfTreeWidget.header().resizeSection(1, 170)
    ui.pdfTreeWidget.header().setMinimumSectionSize(50)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    initGui()
    sys.exit(app.exec_())