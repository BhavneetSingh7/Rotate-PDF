from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from modify import modify_pdf
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
    FILENAME = secure_filename('pdf-.pdf')
    pdf.save(os.path.join(app.config['UPLOAD_FOLDER'],FILENAME))

    #Specified pages and page angles
    pages = request.form['page-angles']
    pages = pages.split(',')
    for i in range(len(pages)):
        pages[i] = pages[i].split(':')
    pdf_file_meta = {
        'filename':FILENAME,
        'page_data':pages,
    }

    return_pdf_file = modify_pdf(pdf_file_meta)
    return send_file('tmp/o1.pdf')

# flask --app rotate_pdf run