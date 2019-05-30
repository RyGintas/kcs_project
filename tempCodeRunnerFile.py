def return_file(path):
    file_name = 'Exported_file.xlsx'
    wb = load_workbook('Exported_file.xlsx')
    wb.save(file_name)
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], file_name, as_attachment=True)