import camelot
import pandas as pd
from pandas import ExcelWriter

def prepear_file(path):
    tables = camelot.read_pdf(path)
    t1 = tables[0].df
    t1= t1.T.set_index(0).T
    t1.drop(['Comments', 'Ordered by' ], axis=1, inplace=True)
    t1.insert(0, "Warehouse", "V0020LV")
    t1.to_excel(os.path.join(app.config['UPLOAD_FOLDER'], 'Exported_file.xlsx'))
