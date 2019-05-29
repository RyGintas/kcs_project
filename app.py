import os
import camelot
from openpyxl import load_workbook
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    send_from_directory,
)
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/uploads/"
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/downloads/"
ALLOWED_EXTENSIONS = set(["pdf"])
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_url_path="/static")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            file_name_pdf = secure_filename(file.filename)
            file_path_pdf = os.path.join(app.config["UPLOAD_FOLDER"], file_name_pdf)

            file_name_xlsx = file_name_pdf.replace("pdf", "xlsx")
            file_path_xlsx = os.path.join(app.config["UPLOAD_FOLDER"], file_name_xlsx)

            file.save(file_path_pdf)

            tables = camelot.read_pdf(file_path_pdf)
            table = tables[0].df
            table = table.T.set_index(0).T
            table.drop(["Comments", "Ordered by"], axis=1, inplace=True)
            table.insert(0, "Warehouse", "V0020LV")

            table.to_excel(file_path_xlsx)

            return send_from_directory(
                app.config["UPLOAD_FOLDER"], file_name_xlsx, as_attachment=True
            )
    return render_template("home.html")

app.run(debug=True)
