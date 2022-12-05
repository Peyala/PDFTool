from controller import *

if __name__ == "__main__":
    pdf1 = open_pdf('examples/21.pdf')
    pdf2 = open_pdf('examples/plan.pdf')
    pdf3 = open_pdf('examples/soda.pdf')
    n_words = word_counter(pdf1)
    n_chars = char_counter(pdf1)
    n_lines = line_counter(pdf1)
    n_pages = page_counter(pdf1)
    export_plain_txt(pdf1)
    merge_pdfs([pdf1,pdf2])
    split_pdfs(pdf2,[2,3]);
    remove_pages_pdf(pdf2,[2,3]);
    extract_pdfs(pdf2,[0,1,3]);