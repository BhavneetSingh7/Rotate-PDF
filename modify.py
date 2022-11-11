from PyPDF2 import PdfFileReader, PdfFileWriter
from flask import send_file

#  Resolves batches in individual pages
def resolve_batch(s:str):
    """
    Resolves batches in individual pages

    for e.g. input is 1:90,3-5:180,8-10:90
    1 -> [1]
    3-5 -> [3,4,5]
    8-10 -> [8,9,10]

    Used to organize in pages dictionary to take action(rotate pages) for specified pages only and to iterate and checking over whole pdf

    """
    s = s.split('-')
    if len(s)==1:
        return [int(s[0])]
    if len(s)==2:
        return list(range(int(s[0]),int(s[1])+1))

def modify_pdf(pdf_meta:dict):
    """
    Takes input meta data of pdf i.e. filename and pages specification
    """

    pdf_file = PdfFileReader('tmp/'+pdf_meta['filename'])
    return_pdf_file = PdfFileWriter()

    page_data = pdf_meta['page_data']
    pages = {'90':[],'180':[],'270':[],}
    for e in page_data:
        if e[1]=="90":
            pages['90'] += resolve_batch(e[0])
        if e[1]=="180":
            pages['180'] += resolve_batch(e[0])
        if e[1]=="270":
            pages['270'] += resolve_batch(e[0])
    all_pages = {i+1:0 for i in range(pdf_file.getNumPages())}
    for i in pages['90']:
        all_pages[i] = 90
    for i in pages['180']:
        all_pages[i] = 180
    for i in pages['270']:
        all_pages[i] = 270
    
    for i in range(pdf_file.getNumPages()):
        page = pdf_file.getPage(i)
        if all_pages[i+1] != 0:
            page.rotateClockwise(all_pages[i+1])
        return_pdf_file.addPage(page)

    with open('tmp/o1.pdf',mode='wb') as output_file:
        return_pdf_file.write(output_file)
    return 'o1.pdf'

