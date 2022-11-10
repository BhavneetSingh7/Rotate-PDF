from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOADED_FILE_PATH = 'tmp'
app.config['UPLOAD_FOLDER'] = UPLOADED_FILE_PATH
ALLOWED_EXTENSIONS = ('pdf')
i = 1

@app.get('/')
def index():
    return render_template('index.html',)

@app.post('/')
def pdf_post():
    print(request.files['pdf-file'])
    pdf = request.files['pdf-file']
    FILENAME = secure_filename('pdf-'+str(i))
    pdf.save(os.path.join(app.config['UPLOAD_FOLDER'],FILENAME))
    return 'Uploaded pdf'

i += 1

# flask --app rotate_pdf run