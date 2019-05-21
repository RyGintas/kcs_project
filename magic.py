##temporary failiukas kodu .pdf failo apdorojimui
## NEORITAIKYTAS DARBUI SERVERYJE SO FAR

## Aidi, klausimas tau. Ar gera ideja yra ta kad as exportinu lentele i failiuka, o tada ta failiuka nuskaitau su pandas ? 
## problema yra ta kad poto kai  camelot biblioteka nuskaito mano lentele, pandas jos nesupranta ir neapdoroja (neistrina stulpeliu ir tt), 
## o kai padarau nuskaityma is .csv - viskas eina puikiai.


import camelot
import pandas as pd
from pandas import ExcelWriter

tables = camelot.read_pdf('Goods_Order_en.pdf')
tables[0].to_csv('failiukas.csv')
lentele = pd.read_csv('failiukas.csv')
lentele.drop(['Comments', 'Ordered by'], axis=1, inplace=True)
lentele.insert(0, "Warehouse", "V0020LV")
writer = ExcelWriter('Order_EXPORTED.xlsx')
lentele.to_excel(writer,'Sheet1', index=False)
writer.save()