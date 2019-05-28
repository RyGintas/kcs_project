import os
import camelot
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__, static_url_path='/static')
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('upload_file', filename=filename))
    return render_template('home.html')

def process_file(path, filename):
        prepear_file(path, filename)

def prepear_file(path, filename):
    tables = camelot.read_pdf('/uploads/<filename>')
    tables[0].to_csv('/uploads/<filename>')
    input_file = pd.read_csv('/uploads/<filename>')
    input_file.drop(['Comments', 'Ordered by'], axis=1, inplace=True)
    input_file.insert(0, "Warehouse", "V0020LV")
    writer = ExcelWriter['DOWNLOAD_FOLDER' + filename ]
    input_file.to_excel(writer,'Sheet1', index=False)
    writer.save()

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


app.run(debug=True)