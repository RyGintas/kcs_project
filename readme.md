Main purpose of this project is to build up a small basic website, where user would be able to upload a .pdf file with some kind of table in it and download that table in Excel file.
-------------------------------------------------------
This project consists o severals parts:
- creating a server with flask
- creating a small basic website, where user will be able to browse and attach .pdf file from his computer
- browser will send that .pdf file to server
- flask will call a labrary tabula (or similar one) and will extract the table
- table data will be sent back using json
- user will download Excel file from wthat website with table extracted from pdf

--------------------------------------------------------
A detailed recquirements for extracted table:


Aprašymas:
Yra dviejų tipų .pdf užsakymo failai: angliška versija ir lietuviška versija. Pavyzdžiai prikabinti.
Užsakymo .pdf failas turi būti nuskaitytas, konvertuotas į .xlsx, tuomet apdorotas pagal šiuos kriterijus:
LT atvejis
•	Pirma excel eilutė turi būti visuomet vienoda. Stulpelių antraštės (reikšmės):
1.	Warehouse
2.	Item
3.	Product name
4.	Purchase Qty
•	Stulpeliai turi būti užpildyti pagal šias reikšmes iš .pdf failo:
1.	Warehouse stulpelio užpildymo reikšmės imamos pagal nurodytą reikšmę šalia „Perkelti į sandėlį:“ (pavyzdžio atveju V0198);
2.	Item stulpelio reikšmės imamos iš lentelės pirmo stulpelio „kodas“
3.	Product name stulpelio reikšmės imamos iš stulpelio „Pavadinimas“
4.	Purchase Qty stuklpleio reikšmės imamos iš stulpelio „Kiekis“
*Pastaba
Jei užsakymo faile yra antra lentelė užsakyti aksesuarus, ji ignoruojama ir į .xlsx failą neįkeliama 
LV atvejis
•	Pirma excel eilutė turi būti visuomet vienoda. Stulpelių antraštės (reikšmės):
1.	Warehouse
2.	Item
3.	Product name
4.	Purchase Qty
•	Stulpeliai turi būti užpildyti pagal šias reikšmes iš .pdf failo:
1.	Warehouse stulpelio užpildymo reikšmės imamos pagal nurodytą reikšmę šalia „Move to warehouse:“ (pavyzdžio atveju V0020LV);
2.	Item stulpelio reikšmės imamos iš lentelės pirmo stulpelio „kodas“
3.	Product name stulpelio reikšmės imamos iš stulpelio „Pavadinimas“
4.	Purchase Qty stuklpleio reikšmės imamos iš stulpelio „Kiekis“
*Pastaba
Jei užsakymo faile yra antra lentelė užsakyti aksesuarus, ji ignoruojama ir į .xlsx failą neįkeliama 

