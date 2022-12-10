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
def enableComponent(component):
    component.setEnabled(True)

def disableComponent(component):
    component.setDisabled(True)

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
        disableComponent(ui.deleteButton)
        disableCountElements()
    elif len(selectedItems) == 1:
        enableCountElements()
        enableComponent(ui.deleteButton)
    else:
        disableCountElements()
        enableComponent(ui.deleteButton)
    
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
    disableComponent(ui.deleteButton)
    disableCountElements()
    reassignIds()

def deleteButtonVisibilityHandler(button: QtWidgets.QPushButton):
    if len(selectedItems) == 0:
        disableComponent(button)
    else:
        enableComponent(button)
        
def reassignIds():
    listWidget = ui.pdfTreeWidget
    i = 0
    while i < listWidget.topLevelItemCount():
        listWidget.topLevelItem(i).setText(0,str(i+1))
        i+=1

def countButtonHandler():
    text = ""
    listWidget = ui.pdfTreeWidget
    i = int(selectedItems[0].text(0)) - 1
    pdf = pdf_list[i]
    if ui.charsCheckBox.isChecked():
        chars = str(char_counter(pdf))
        text = text + "Chars: " + chars + "\n"
        uiCount.charTextBrowser.setText(chars)
        enableComponent(uiCount.charTextBrowser)
    else:
        disableComponent(uiCount.charTextBrowser)
        uiCount.charTextBrowser.setText("")
    if ui.wordsCheckBox.isChecked():
        words = str(word_counter(pdf))
        text = text + "Words: " + words + "\n"
        uiCount.wordsTextBrowser.setText(words)
        enableComponent(uiCount.wordsTextBrowser)
    else:
        disableComponent(uiCount.wordsTextBrowser)
        uiCount.wordsTextBrowser.setText("")
    if ui.linesCheckBox.isChecked():
        lines = str(line_counter(pdf))
        text = text + "Lines: " + lines + "\n"
        uiCount.linesTextBrowser.setText(lines)
        enableComponent(uiCount.linesTextBrowser)
    else:
        disableComponent(uiCount.linesTextBrowser)
        uiCount.linesTextBrowser.setText("")
    if ui.pagesCheckBox.isChecked():
        pages = str(page_counter(pdf))
        text = text + "Pages: " + pages  + "\n"
        uiCount.pagesTextBrowser.setText(pages)
        enableComponent(uiCount.pagesTextBrowser)
    else:
        disableComponent(uiCount.pagesTextBrowser)
        uiCount.pagesTextBrowser.setText("")
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
    disableComponent(ui.deleteButton)
    #clear inputs
    ui.charsCheckBox.setChecked(False)
    ui.wordsCheckBox.setChecked(False)
    ui.linesCheckBox.setChecked(False)
    ui.pagesCheckBox.setChecked(False)

def checkBoxCountHandler():
    if ui.charsCheckBox.isChecked() or ui.wordsCheckBox.isChecked() or ui.linesCheckBox.isChecked() or ui.pagesCheckBox.isChecked():
        enableComponent(ui.countButton)
    else:
        disableComponent(ui.countButton)

def enableCountElements():
    enableComponent(ui.charsCheckBox)
    enableComponent(ui.wordsCheckBox)
    enableComponent(ui.linesCheckBox)
    enableComponent(ui.pagesCheckBox)
    checkBoxCountHandler()

def disableCountElements():
    disableComponent(ui.countButton)
    disableComponent(ui.charsCheckBox)
    disableComponent(ui.wordsCheckBox)
    disableComponent(ui.linesCheckBox)
    disableComponent(ui.pagesCheckBox)
    
def initGuiElements():
    disableComponent(ui.deleteButton)
    disableComponent(ui.countButton)
    disableComponent(ui.removeButton)
    disableComponent(ui.extractButton)
    disableComponent(ui.mergeButton)
    disableComponent(ui.splitButton)
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
    ui.charsCheckBox.clicked.connect(lambda: checkBoxCountHandler())
    ui.wordsCheckBox.clicked.connect(lambda: checkBoxCountHandler())
    ui.linesCheckBox.clicked.connect(lambda: checkBoxCountHandler())
    ui.pagesCheckBox.clicked.connect(lambda: checkBoxCountHandler())
    
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