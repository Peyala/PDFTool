import pdfplumber as pdfpl
import pdf_manager as model
import gui as gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
import sys



# Operations 
def open_pdf(path: str):
    return model.open_pdf(path)

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

def merge_pdfs(pdfs: list):
    return model.merge_pdfs(pdfs)

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
    for pdf_path in pdf_paths:
        pdfItem = QListWidgetItem(pdf_path.split('/')[-1])
        pdfItem.setIcon(icon)
        ui.pdfListWidget.addItem(pdfItem)
        pdf = open_pdf(pdf_path)
        pdf_list.append(pdf)

def deleteButtonHandler():
    listWidget = ui.pdfListWidget
    selectedItems = listWidget.selectedItems()
    for item in selectedItems:
        index = listWidget.row(item)
        listWidget.takeItem(index)
        del pdf_list[index]

def deleteButtonVisibilityHandler(button: QtWidgets.QPushButton, selectedItems: list[QListWidgetItem]):
    if len(selectedItems) == 0:
        disableButton(button)
    else:
        enableButton(button)

def countButtonHandler():
    text = ""
    listWidget = ui.pdfListWidget
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
    QMessageBox.information(None,"Count","The PDFs were merged correctly")
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    disableButton(ui.deleteButton)
    ui.addButton.clicked.connect(lambda: addButtonHandler(ui))
    ui.deleteButton.clicked.connect(deleteButtonHandler)
    ui.countButton.clicked.connect(countButtonHandler)
    ui.pdfListWidget.itemSelectionChanged.connect(lambda: deleteButtonVisibilityHandler(ui.deleteButton, ui.pdfListWidget.selectedItems()))
    pdf_list: list[pdfpl.PDF] = []
    #ui.addButton.setEnabled(False)
    sys.exit(app.exec_())