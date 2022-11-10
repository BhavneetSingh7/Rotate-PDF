from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOADED_FILE_PATH = 'tmp'
app.config['UPLOAD_FOLDER'] = UPLOADED_FILE_PATH
ALLOWED_EXTENSIONS = ('pdf')

@app.get('/')
def index():
    return render_template('index.html',)

@app.post('/')
def pdf_post():
    #Saving file in server
    pdf = request.files['pdf-file']
    FILENAME = secure_filename('pdf-')
    pdf.save(os.path.join(app.config['UPLOAD_FOLDER'],FILENAME))

    #Specified pages and page angles
    pages = request.form['page-angles']
    pages = pages.split(',')
    for i in range(len(pages)):
        pages[i] = pages[i].split(':')
    print(pages)
    pdf_file_meta = {
        'filename':FILENAME,
        'page_data':pages,
    }
    return pdf_file_meta

# flask --app rotate_pdf run