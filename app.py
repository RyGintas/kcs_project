from flask import Flask

UPLOAD_FOLDER = 'C:\kcs_project\uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER