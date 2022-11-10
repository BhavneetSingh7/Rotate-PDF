from PyPDF2 import PdfFileReader, PdfFileWriter

def modify_pdf(pdf_meta:dict):
    pdf_file = PdfFileReader('tmp/'+pdf_meta['filename'])
    return_pdf_file = PdfFileWriter()
    page_data = pdf_meta['page_data']
    return pdf_file