import camelot
import pandas as pd
from pandas import ExcelWriter

def prepear_file(path, filename):
tables = camelot.read_pdf('Goods_Order_en.pdf')
tables[0].to_csv('failiukas.csv')
lentele = pd.read_csv('failiukas.csv')
lentele.drop(['Comments', 'Ordered by'], axis=1, inplace=True)
lentele.insert(0, "Warehouse", "V0020LV")
writer = ExcelWriter('Order_EXPORTED.xlsx')
lentele.to_excel(writer,'Sheet1', index=False)
writer.save()