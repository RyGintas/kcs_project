<p align="center">
   <img src="https://github.com/RyGintas/kcs_project/blob/master/img/logo.jpg" width="200">
</p>


# My first python pject "PDF2X"

pakeiciau eilute

Main purpose of this project is to build up a small basic website, where user would be able to upload a specific .pdf file (sample attached Goods_Order_EN.pdf) and receive it back in .xlsx format with a table extracted and modified by specific needs.

> *Note: this is a specific project, it is only suitable for limed group of users, that works with such orders.*

> *Another note: if there are two tables in .pdf file, only first one is extracted*

-------------------------------------------------------

## This project consists of severals parts:

- creating a server with flask
- creating a small basic HTML website, where user will be able to browse and attach .pdf file from his computer
- browser will send that .pdf file to server
- server will call a library "Camelot" for extracting a table
- server will call a library "pandas" for modifying a table
- table data will be sent back using json
- user will download Excel.xlsx file from that website with table extracted from pdf

--------------------------------------------------------

A detailed recquirements for extracted table:

-	First line in table stays always the same with such headers:
1.	Warehouse
2.	Code
3.	Name
4.	Quantity

-	First column is filled with same value - "V0020LV"

-   Excel file format .xlsx

**Please do not use without my permission!**
