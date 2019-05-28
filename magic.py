import camelot
import pandas as pd
from pandas import ExcelWriter

def prepear_file(path, filename):
    tables = camelot.read_pdf('/uploads/<filename>')
    t1 = tables[0].df
    t1= t1.T.set_index(0).T
    t1.drop(['Comments', 'Ordered by' ], axis=1, inplace=True)
    t1.insert(0, "Warehouse", "V0020LV")
    return t1.to_html()
    #from pandas import ExcelWriter
    #writer = ExcelWriter('PythonExport.xlsx')
    #t1.to_excel(writer,'Sheet1', index=False)
    #writer.save()