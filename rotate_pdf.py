from flask import Flask, render_template
app = Flask(__name__)

UPLOADED_FILE_PATH = '/tmp/'
ALLOWED_EXTENSIONS = ('pdf')

@app.get('/')
def index():
    return render_template('index.html',)

@app.post('/')
def pdf_post():
    return 'Upload pdf'

# flask --app rotate_pdf run