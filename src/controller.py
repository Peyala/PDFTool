import pdfplumber as pdfpl
import pdf_manager as model

pdf1 = model.open_pdf('examples/21.pdf')
pdf2 = model.open_pdf('examples/soda.pdf')
pdf3 = model.open_pdf('examples/plan.pdf')
n_words = model.word_counter(pdf1)
n_chars = model.char_counter(pdf1)
n_lines = model.line_counter(pdf1)
n_pages = model.page_counter(pdf1)
model.export_plain_txt(pdf1)
model.merge_pdfs([pdf1,pdf2])
model.split_pdfs(pdf3,(2,3));
model.remove_pages_pdf(pdf3,[2,3]);
model.extract_pdfs(pdf3,[0,1,3]);

print(n_words)
print(n_chars)
print(n_lines)
print(n_pages)