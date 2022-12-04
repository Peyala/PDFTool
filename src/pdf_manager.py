import pdfplumber as pdfpl
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter 
import datetime as dt
import zipfile as zip
import os

def open_pdf(path) -> pdfpl.PDF:
    return pdfpl.open(path)

def export_plain_txt(pdf):
    time = dt.date.today()
    with open(str(time)+'_plain.txt', 'w', encoding='utf-8') as f:
        for page in pdf.pages:
            f.write(page.extract_text())
            f.write('\n')
    f.close()

def to_plain_text(pdf):
    text = ""
    for page in pdf.pages:
        text = text + page.extract_text()
    return text

def word_counter(pdf: pdfpl.PDF):
    words = 0
    for page in pdf.pages:
        words = words + len(page.extract_words())
    return words

def char_counter(pdf: pdfpl.PDF):
    return len(pdf.chars)

def line_counter(pdf: pdfpl.PDF):
    text = to_plain_text(pdf)
    return text.count("\n") + page_counter(pdf)

def page_counter(pdf: pdfpl.PDF):
    return len(pdf.pages)

def remove_pages_pdf(pdf, i_pages: list):
    pdfreader = PdfFileReader(pdf.stream)
    pdfwriter = PdfFileWriter()
    for i in range(page_counter(pdf)):
        if i not in i_pages:
            pdfwriter.addPage(pdfreader.getPage(i))
    time = dt.date.today()
    pdfwriter.write(str(time)+"_removed.pdf")

def merge_pdfs(pdfs):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf.stream.name)
    time = dt.date.today()
    merger.write(str(time) + "_merged.pdf")
    merger.close()

def split_pdfs(pdf: pdfpl.PDF, pages_range):
    pdfreader = PdfFileReader(pdf.stream)
    pdfwriter = PdfFileWriter()
    for i in range(pages_range[0],pages_range[1]+1):
        pdfwriter.addPage(pdfreader.getPage(i))
    time = dt.date.today()
    pdfwriter.write(str(time)+"_splitted.pdf")

def extract_pdfs(pdf, i_pages=None):
    pdf_names = []
    pdfreader = PdfFileReader(pdf.stream)
    name = 1
    title = ""
    if i_pages is None:
        i_pages=[]
        i_pages.extend(range(0, pdfreader.getNumPages()))
    for i_page in i_pages:
        pdfwriter = PdfFileWriter()
        pdfwriter.addPage(pdfreader.getPage(i_page))
        title = "page_" + str(i_page+1)+".pdf"
        pdfwriter.write(title)
        pdf_names.append(title)
        name += 1
    try:
        compression = zip.ZIP_DEFLATED
    except:
        compression = zip.ZIP_STORED
        
    time = dt.date.today()
    zf = zip.ZipFile(str(time)+"_extracted.zip", mode="w")
    try:
        for p in pdf_names:
            zf.write(p, compress_type=compression)
            os.remove(p)
    finally:
        zf.close()