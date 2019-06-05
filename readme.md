<p align="center">
   <img src="https://github.com/RyGintas/kcs_project/blob/master/static/images/logo.png" width="200">
</p>


# My first python pject "PDF2X"

Main purpose of this project is to build up a small basic website, where user would be able to upload a specific .pdf file (sample attached Goods_Order_EN.pdf) and receive it back in .xlsx format with a table extracted and modified by specific needs. Python 3.7 is required to run this app.


> *Note: this is a specific project, it is only suitable for limed group of users, that works with such orders.*

> *Another note: if there are two tables in .pdf file, only first one is extracted*

-------------------------------------------------------

## This project consists of severals parts:

- creating a server with flask
- creating a small basic HTML website, where user will be able to browse and attach .pdf file from his computer
- browser will send that .pdf file to server
- server will call a library "Camelot" for extracting a table
- server will call a library "pandas" for modifying a table and writng data to Excel file
- Exported_file.xlsx file with extracted table from pdf will download automatically
- whole process will be logged with logging library

--------------------------------------------------------

## What this converter basically does:

It reads a PDF file and makes an XLSX file with such formatting:

-	First line in table stays always the same with such headers:

Warehouse   | Code  | Name  | Quantity

-	Column A is filled with same value - "V0020LV"
-   Column B is filled with item codes
-   Column C is filled with item names
-   Column D is filled with ordered quantity
-   Exporterl file format .xlsx

## How to run:

first install necessary libraries:
```shell
pip install -r requirements.txt
```
then just run app.py

**Please do not spread this app without my permission!**
