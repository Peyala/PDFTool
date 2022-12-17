import pdfplumber as pdfpl
import pdf_manager as model
import gui as gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import datetime as dt
import sys
import count_gui as count_gui
import tree as tree
import regularexpr as reg

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

# GUI Controllers 
def enableComponent(component):
    component.setEnabled(True)

def disableComponent(component):
    component.setDisabled(True)

def addButtonHandler():
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
        items_list.append(pdfItem)
    if len(items_list) > 0 :
        enableComponent(ui.actionSelect_all)
    
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
        disableCountElements() #we cant count elements here so we disable count elements
        disableRemoveComponents()
        disableComponent(ui.actionUnselect_all)
        disableComponent(ui.mergeButton)
    elif len(selectedItems) == 1:
        enableComponent(ui.deleteButton)
        enableCountElements() #we can count elements here so we enable count elements
        enableRemoveComponents()
        enableComponent(ui.actionUnselect_all)
        disableComponent(ui.mergeButton)
    else:
        enableComponent(ui.deleteButton)
        disableCountElements() #we cant count elements here so we disable count elements
        disableRemoveComponents()
        enableComponent(ui.actionUnselect_all)
        enableComponent(ui.mergeButton)
    # Comparison to manage menu bar options enabling
    #selectedItems.sort()
    #items_list.sort()
    if selectedItems == items_list:
        disableComponent(ui.actionSelect_all)
    else:
        enableComponent(ui.actionSelect_all)
    reorderPdfList()
    
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
        items_list.remove(item)
    disableComponent(ui.deleteButton)
    disableCountElements()
    disableRemoveComponents()
    disableComponent(ui.actionUnselect_all)
    disableComponent(ui.mergeButton)
    reassignIds()

def deleteButtonVisibilityHandler(button: QtWidgets.QPushButton):
    if len(selectedItems) == 0:
        disableComponent(button)
    else:
        enableComponent(button)

#function that reassigns ID for the TreeWidgetView. This method is also at tree.py in order to reassign IDS when a PDF was dragged and dropped somewhere else
def reassignIds():
    listWidget = ui.pdfTreeWidget
    i = 0
    while i < listWidget.topLevelItemCount():
        listWidget.topLevelItem(i).setText(0,str(i+1))
        i+=1

def countButtonHandler():
    #change cursor to waiting cursor while computing 
    app.setOverrideCursor(Qt.WaitCursor)
    text = ""
    i = int(selectedItems[0].text(0)) - 1 #gets the first selected item (only one can be selected here lol)
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
    #resrote the original cursor
    app.restoreOverrideCursor()
    resultCount.show()
    
#method to substract by one every element of the input list (in order to get the indexes pages of the PDF)
def substractOne(list):
    for i in range(len(list)):
        list[i] = list[i]-1
    return list

#method to reoirder the pdf_list every time there is a TreeWidget event
def reorderPdfList():
    global pdf_list
    listWidget = ui.pdfTreeWidget
    sorted_pdf_list = []
    for i in range(listWidget.topLevelItemCount()):
        pdfName = listWidget.topLevelItem(i).text(1)
        pdf = searchPDFByName(pdfName)
        sorted_pdf_list.append(pdf)
        
    pdf_list = sorted_pdf_list
    
def removeButtonHandler():
    selectedPdf = selectedItems[0]
    index = int(selectedPdf.text(0))-1
    interval_input = ui.remLineEdit.text()
    print(interval_input)
    interval_list = reg.parsePDFsInput(interval_input)
    time = dt.date.today()
    file_name = QFileDialog.getSaveFileName(None,'Save removed PDF file', str(time) + '_removed.pdf','PDF Files (*pdf)')[0]
    if file_name.split('.')[-1] != 'pdf':
        file_name = file_name + '.pdf'
    indexes_interval = substractOne(interval_list)
    print(pdf_list[index],indexes_interval)
    remove_pages_pdf(pdf_list[index],indexes_interval)
    

    
def mergeButtonHandler():
    global pdf_list
    elgible_pdfs = []
    listWidget = ui.pdfTreeWidget
    i = 0
    for i in range(len(selectedItems)):
        if listWidget.topLevelItem(i).checkState(2):
            pdfIndex = int(listWidget.topLevelItem(i).text(0)) - 1
            elgible_pdfs.append(pdf_list[pdfIndex])
        
    time = dt.date.today()
    file_name = QFileDialog.getSaveFileName(None,'Save merged PDF file', str(time) + '_merged.pdf','PDF Files (*pdf)')[0]
    if file_name.split('.')[-1] != 'pdf':
        file_name = file_name + '.pdf'
    print(elgible_pdfs)
    merge_pdfs(elgible_pdfs,file_name)
    
def searchPDFByName(pdfName):
    for pdf in pdf_list:
        name = pdf.stream.name.split('/')[-1]
        if name == pdfName:
            return pdf
    
def newActionHandler():
    #clear the pdf widget list
    ui.pdfTreeWidget.clear() 
    #close pdfs
    for pdf in pdf_list:
        close_pdf(pdf)
    pdf_list.clear()
    items_list.clear()
    selectedItems.clear()
    #manage buttons
    disableComponent(ui.deleteButton)
    #clear inputs
    setCountCheckState(False)
    """ui.charsCheckBox.setChecked(False)
    ui.wordsCheckBox.setChecked(False)
    ui.linesCheckBox.setChecked(False)
    ui.pagesCheckBox.setChecked(False)"""

#handler that is call when any checkbox is clicked in order to enable or disable the count button
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
    checkBoxCountHandler() #check if we can enable the count button (at least a checkbox is checked)

def disableCountElements():
    disableComponent(ui.countButton)
    disableComponent(ui.charsCheckBox)
    disableComponent(ui.wordsCheckBox)
    disableComponent(ui.linesCheckBox)
    disableComponent(ui.pagesCheckBox)
    
def enableRemoveComponents():
    enableComponent(ui.remLineEdit)
    enableComponent(ui.removeButton)

def disableRemoveComponents():
    disableComponent(ui.remLineEdit)
    disableComponent(ui.removeButton)
    
def setCountCheckState(state: bool):
    ui.charsCheckBox.setChecked(state)
    ui.wordsCheckBox.setChecked(state)
    ui.linesCheckBox.setChecked(state)
    ui.pagesCheckBox.setChecked(state)

def selectAllPdfs():
    global selectedItems
    for item in items_list:
        item.setCheckState(2, QtCore.Qt.Checked)
    selectedItems = items_list.copy()
    if len(selectedItems) == 1:
        disableComponent(ui.mergeButton)
        enableCountElements() #we can count elements here so we enable count elements
        enableRemoveComponents()
    else:
        enableComponent(ui.mergeButton)
        disableCountElements() #we cant count elements here so we disable count elements
        disableRemoveComponents()
    enableComponent(ui.deleteButton)
    disableComponent(ui.actionSelect_all)
    enableComponent(ui.actionUnselect_all)

def unselectAllPdfs():
    global selectedItems
    for item in selectedItems:
        item.setCheckState(2, QtCore.Qt.Unchecked)
    selectedItems.clear()
    disableComponent(ui.deleteButton)
    disableCountElements() #we cant count elements here so we disable count elements
    disableRemoveComponents()
    disableComponent(ui.actionUnselect_all)
    enableComponent(ui.actionSelect_all)
    disableComponent(ui.mergeButton)

def initGuiElements():
    disableComponent(ui.deleteButton)
    disableComponent(ui.removeButton)
    disableComponent(ui.extractButton)
    disableComponent(ui.mergeButton)
    disableComponent(ui.splitButton)
    disableComponent(ui.actionSelect_all)
    disableComponent(ui.actionUnselect_all)
    disableComponent(ui.actionUndo)
    disableCountElements()
    disableRemoveComponents()
    setCountCheckState(False)
    """ui.charsCheckBox.setChecked(False)
    ui.wordsCheckBox.setChecked(False)
    ui.linesCheckBox.setChecked(False)
    ui.pagesCheckBox.setChecked(False)"""
    ui.remLineEdit.setEnabled(False)
    ui.extrLineEdit.setEnabled(False)
    ui.bottomSplitSpinBox.setEnabled(False)
    ui.topSplitSpinBox.setEnabled(False)
    
def initGuiHandlers():
    # anotherGUI
    ui.addButton.clicked.connect(addButtonHandler)
    ui.deleteButton.clicked.connect(deleteButtonHandler)
    ui.countButton.clicked.connect(countButtonHandler)
    ui.mergeButton.clicked.connect(mergeButtonHandler)
    ui.newAction.triggered.connect(newActionHandler)
    ui.charsCheckBox.clicked.connect(checkBoxCountHandler)
    ui.wordsCheckBox.clicked.connect(checkBoxCountHandler)
    ui.linesCheckBox.clicked.connect(checkBoxCountHandler)
    ui.pagesCheckBox.clicked.connect(checkBoxCountHandler)
    ui.removeButton.clicked.connect(removeButtonHandler)
    # Menu bar
    ui.exitAction.triggered.connect(MainWindow.close)
    ui.actionSelect_all.triggered.connect(selectAllPdfs)
    ui.actionUnselect_all.triggered.connect(unselectAllPdfs)
    # countGUI
    uiCount.okButton.clicked.connect(resultCount.close)
    uiCount.exportButton.clicked.connect(exportButtonHandler)
    
def initGui():
    global app, MainWindow, ui, resultCount, uiCount, pdf_list, items_list, selectedItems
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
    items_list = []
    ui.pdfTreeWidget.itemClicked.connect(onItemClicked)
    selectedItems = []
    # A incluir en gui pero como se sobreescribe lo dejo aqui por ahora
    ui.pdfTreeWidget.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    ui.pdfTreeWidget.header().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    ui.pdfTreeWidget.header().setFirstSectionMovable(True)
    ui.pdfTreeWidget.header().stretchLastSection()
    ui.pdfTreeWidget.header().resizeSection(1, 160)
    ui.pdfTreeWidget.header().setMinimumSectionSize(50)

# Count_GUI Controllers 

def exportButtonHandler():
    x=0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    initGui()
    sys.exit(app.exec_())